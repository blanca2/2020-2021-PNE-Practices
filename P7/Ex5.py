import http.client
import json
import Seq1

def print_colored(message, data, color):
    from termcolor import cprint, colored
    print(colored(message, color), end="")
    print(data)

gene_dict = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMETERS = '?content-type=application/json'

connection = http.client.HTTPConnection(SERVER)
try:
    for key, id in gene_dict.items():
        connection.request("GET", ENDPOINT + id + PARAMETERS)
        response = connection.getresponse()
        if response.status == 200:
            response_dict = json.loads(response.read().decode())
            sequence = Seq1.Seq(response_dict['seq'])
            s_length = sequence.len()
            all_percentages = sequence.percentages(sequence.count_bases(), s_length)
            most_frequent_bases = sequence.frequent_base(sequence.count())
            print_colored("Gene:", key, "yellow")
            print_colored("Total length: ", s_length, "yellow")
            for key, value in all_percentages.items():
                print_colored(key + ": ", value, "blue")
            print_colored("Most frequent base: ", most_frequent_bases, "yellow")
except KeyError:
    print("The gene is not inside the dictionary. Please choose one of the following:", list(gene_dict.keys()))
