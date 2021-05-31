import http.server
import http.client
import socketserver
import termcolor
import pathlib
import jinja2
from urllib.parse import urlparse, parse_qs
import json
import server_utils as su
import Seq1

gene_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}


def read_template_html_file(filename):

    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content


PORT = 8081


def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_post(self):
        print(self)

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)

        SERVER = "rest.ensembl.org"
        PARAMS = "?content-type=application/json"
        connection = http.client.HTTPConnection(SERVER)

        context = {}
        if path_name == '/':
            contents = read_template_html_file('./html/index.html').render(context=context)

        elif path_name == '/listSpecies':
            try:
                ENDPOINT = "/info/species"
                connection.request("GET", ENDPOINT + PARAMS)
                response = connection.getresponse()
                dict_response = json.loads(response.read().decode())
                species = dict_response['species']
                num_species = int(arguments['specie'][0])
                num_total_species = len(species)
                l_species = []
                i = 0
                while i <= num_species:
                    l_species.append(species[i])
                    i += 1

                context = {'num_total_species': num_total_species, 'num_regs': num_species, 'species': l_species}
                contents = read_template_html_file('./html/species.html').render(context=context)
            except ValueError:
                contents = read_template_html_file('html/error.html').render()
        elif path_name == '/karyotype':
            try:
                ENDPOINT = "/info/assembly/"
                specie = arguments['specie'][0]
                connection.request("GET", ENDPOINT + specie + PARAMS)
                response = connection.getresponse()
                dict_response = json.loads(response.read().decode())
                k_list = []
                for i in dict_response['karyotype']:
                    k_list.append(i)
                context = {'karyotype': k_list}
                contents = read_template_html_file('./html/karyotype.html').render(context=context)
            except KeyError:
                contents = read_template_html_file('html/error.html').render()

        elif path_name == '/chromosome':
            try:
                ENDPOINT = "/info/assembly/"
                specie = arguments['specie'][0]
                connection.request("GET", ENDPOINT + specie + PARAMS)
                response = connection.getresponse()
                dict_response = json.loads(response.read().decode())
                chromosomes = arguments['chromosome'][0]
                for i in range(0, len(dict_response['top_level_region'])):
                    if dict_response['top_level_region'][i]['name'] == chromosomes:
                        length = dict_response['top_level_region'][i]['length']
                        context = {'length': length}
                    else:
                        pass
                contents = read_template_html_file('./html/chromosome.html').render(context=context)
            except KeyError:
                contents = read_template_html_file('html/error.html').render()

        elif path_name == "/geneSeq":
            try:
                ENDPOINT = "/sequence/id/"
                gene = arguments['gene'][0]
                ID = gene_dict[gene]
                connection.request("GET", ENDPOINT + ID + PARAMS)
                response = connection.getresponse()
                dict_response = json.loads(response.read().decode())
                context = {'gene_name': gene, 'seq': dict_response['seq']}
                contents = read_template_html_file('./html/geneSeq.html').render(context=context)
            except KeyError:
                contents = read_template_html_file('html/error.html').render()

        elif path_name == "/geneInfo":
            try:
                ENDPOINT = "/sequence/id/"
                gene = arguments['gene'][0]
                ID = gene_dict[gene]
                connection.request("GET", ENDPOINT + ID + PARAMS)
                response = connection.getresponse()
                dict_response = json.loads(response.read().decode())
                length = str(int(dict_response['desc'].split(":")[4]) - int(dict_response['desc'].split(":")[3]))
                context = {"gene_name": gene, "length": length, "start": dict_response['desc'].split(":")[3], "end": dict_response['desc'].split(":")[4], "name": dict_response["desc"].split(":")[1]}
                contents = read_template_html_file('./html/geneInfo.html').render(context=context)
            except KeyError:
                contents = read_template_html_file('html/error.html').render()

        elif path_name == "/geneCalc":
            try:
                ENDPOINT = "/sequence/id/"
                gene = arguments['gene'][0]
                ID = gene_dict[gene]
                connection.request("GET", ENDPOINT + ID + PARAMS)
                response = connection.getresponse()
                dict_response = json.loads(response.read().decode())
                sequence = Seq1.Seq(dict_response["seq"])
                s_length = sequence.len()
                percentages = sequence.percentages(sequence.count_bases(), s_length)
                context = {"gene_name": gene, "length": s_length, "percentages": percentages.items()}
                contents = read_template_html_file('./html/geneCalc.html').render(context=context)
            except KeyError:
                contents = read_template_html_file('html/error.html').render()

        else:
            contents = su.read_template_html_file("html/error.html").render()

        self.send_response(200)  # -- Status line: OK!

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()