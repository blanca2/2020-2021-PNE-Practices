import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su
import Seq1
import json

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

PORT = 8081

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

        context = {}
        content_type = 'text/html'

        try:
            if path_name == '/':
                context['list'] = gene_dict.keys()
                contents = su.read_template_html_file('./html/index.html').render(context=context)

            elif path_name == '/listSpecies':
                ENDPOINT = '/info/species'
                l_species = []
                try:
                    limit = arguments['limit'][0]
                except ValueError:
                    contents = su.read_template_html_file('./html/error.html').render(context=context)

                if limit.isdigit():
                    for specie in (su.get_dict(ENDPOINT)['species'][0:int(limit)]):
                        l_species.append(specie['name'])
                    context = {"num_species": limit, "total_species": l_species, "length": len(su.get_dict(ENDPOINT)['species'])}
                    contents = su.read_template_html_file('./html/species.html').render(context=context)
                else:
                    contents = su.read_template_html_file('./html/error.html').render(context=context)

                # if 'json' in arguments:
                # contents = json.dumps(context)
                # content_type = "application/json"
                # else:
                # contents = su.read_template_html_file('./html/error.html').render(context=context)

            elif path_name == '/karyotype':
                ENDPOINT = "/info/assembly/"
                specie = arguments['specie'][0].replace(' ', '_')
                dict_response = su.get_dict(ENDPOINT + specie)
                k_list = []
                for i in dict_response['karyotype']:
                    k_list.append(i)
                context = {'karyotype': k_list}
                contents = su.read_template_html_file('./html/karyotype.html').render(context=context)

               # if 'json' in arguments:
                   # contents = json.dumps(context)
                    #content_type = "application/json"
                # else:
                    # contents = su.read_template_html_file('./html/error.html').render(context=context)

            elif path_name == '/chromosome':
                ENDPOINT = "/info/assembly/"
                specie = arguments['specie'][0].replace(' ', '_')
                dict_response = su.get_dict(ENDPOINT + specie)
                chromosomes = arguments['chromosome'][0]
                for dictionary in dict_response['top_level_region']:
                    if dictionary['name'] == chromosomes:
                        context = {"chromosome": chromosomes, "length": dictionary['length']}
                        contents = su.read_template_html_file('./html/chromosome.html').render(context=context)
                        break
                    else:
                        pass
                # if 'json' in arguments:
                # contents = json.dumps(context)
                # content_type = "application/json"
                # else:
                # contents = su.read_template_html_file('./html/error.html').render(context=context)

            elif path_name == "/geneSeq":
                ENDPOINT = "/sequence/id/"
                gene = arguments['gene'][0]
                ID = gene_dict[arguments['gene'][0]]
                dict_response = su.get_dict(ENDPOINT + ID)
                context = {'gene_name': gene, 'seq': dict_response['seq']}
                contents = su.read_template_html_file('./html/geneSeq.html').render(context=context)
                # if 'json' in arguments:
                # contents = json.dumps(context)
                # content_type = "application/json"
                # else:
                # contents = su.read_template_html_file('./html/error.html').render(context=context)

            elif path_name == "/geneInfo":
                ENDPOINT = "/sequence/id/"
                gene = arguments['gene'][0]
                ID = gene_dict[gene]
                dict_response = su.get_dict(ENDPOINT + ID)
                info = dict_response['desc']
                length = str(int(info.split(":")[4]) - int(info.split(":")[3]))
                context = {'gene_name': gene, 'length': length, 'start': info.split(":")[3], 'end': info.split(":")[4], 'name': info.split(":")[2]}
                contents = su.read_template_html_file('./html/geneInfo.html').render(context=context)
                # if 'json' in arguments:
                # contents = json.dumps(context)
                # content_type = "application/json"
                # else:
                # contents = su.read_template_html_file('./html/error.html').render(context=context)

            elif path_name == "/geneCalc":
                ENDPOINT = "/sequence/id/"
                gene = arguments['gene'][0]
                ID = gene_dict[gene]
                dict_response = su.get_dict(ENDPOINT + ID)
                sequence = Seq1.Seq(dict_response["seq"])
                s_length = sequence.len()
                percentages = sequence.percentages(sequence.count_bases(), s_length)
                context = {"gene_name": gene, "length": s_length, "percentages": percentages.items()}
                contents = su.read_template_html_file('./html/geneCalc.html').render(context=context)
                # if 'json' in arguments:
                # contents = json.dumps(context)
                # content_type = "application/json"
                # else:
                # contents = su.read_template_html_file('./html/error.html').render(context=context)

            else:
                contents = su.read_template_html_file("html/error.html").render()

        except (KeyError, IndexError, ValueError):
            contents = su.read_template_html_file('./html/error.html').render()

        self.send_response(200)
        self.send_header('Content-Type', content_type)
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