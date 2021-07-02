import json
import http.client

PORT = 8081
SERVER = "127.0.0.1"
conn = http.client.HTTPConnection(SERVER, PORT)

def client(ARGUMENTS, PATH_NAME):
        conn.request("GET", PATH_NAME + ARGUMENTS)
        # -- Read the response message from the server
        r1 = conn.getresponse()

        # -- Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # -- Read the response's body
        data1 = r1.read().decode("utf-8")
        print(data1)
        # -- Print the received data
        data = json.loads(data1)
        return data


try:
    PATH_NAME = "/listSpecies"
    ARGUMENTS = "?limit=4&json=1"
    data = client(ARGUMENTS, PATH_NAME)
    list_names = " "
    for name in data['total_species']:
        list_names = list_names + name + ', '
    print("The total number of species is;", data['length'])
    print("The limit selected is:", data['num_species'])
    print("Names of the species:", list_names)
except ConnectionRefusedError:
    print('ERROR! Cannot connect to the server')
    exit()

try:
    PATH_NAME = "/karyotype"
    ARGUMENTS = "?specie=mouse&jason=1"
    data = client(ARGUMENTS, PATH_NAME)
    print('Names of chromosomes:', data['karyotype'])
except ConnectionRefusedError:
    print('ERROR! Cannot connect to the server')
    exit()

try:
    PATH_NAME = "/chromosome"
    ARGUMENTS = "?specie=mouse&chromosome=18&json=1"
    data = client(ARGUMENTS, PATH_NAME)
    print("Length: ", data['length'])
except ConnectionRefusedError:
    print('ERROR! Cannot connect to the server')
    exit()

try:
    PATH_NAME = "/geneSeq"
    ARGUMENTS = "?gene=FRAT1&json=1"
    data = client(ARGUMENTS, PATH_NAME)
    print('Sequence: ', data['seq'])
except ConnectionRefusedError:
    print('ERROR! Cannot connect to the server')
    exit()

try:
    PATH_NAME = "/geneInfo"
    ARGUMENTS = "?gene=FRAT1&json=1"
    data = client(ARGUMENTS, PATH_NAME)
    print('The start is:', data['start'])
    print('The end is: ', data['end'])
    print('The total length is: ', data['length'])
    print('The ID is: ', data['gene_name'])
    print('The gene is in: ', data['name'])
except ConnectionRefusedError:
    print('ERROR! Cannot connect to the server')
    exit()

try:
    ARGUMENTS = "?gene_calculations=FRAT1&json=1"
    PATH_NAME = "/geneCalc"
    data = client(ARGUMENTS, PATH_NAME)
    print("The length of this gene is: ", data['length'])
    print("The % of bases is: ", data['percentages'])
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
