from Client0 import Client

l_seqs = ['AACCGTAAACCGTAAACCGTA', 'TAAACCGTATAAACCGTA', 'AACTABCCAATC', 'AAGGTCGATGCAGCCCCAAA', 'GGTACCTAAAGGC']
l_genes = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6']

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print('Connection to SERVER. Client ip, port: ', str(IP) + ',', str(PORT))

print("*Testing PING...")
print(c.talk("OK!"))

print("Testing GET:")
for n in range(0, len(l_seqs)):
    response = c.talk("GET " + str(n))
    print(f"{response}")

print("Testing INFO:")
response = c.talk("INFO " + l_seqs[1])
print(f"{response}")

print("Testing COMP:")
response = c.talk("COMP " + l_seqs[1])
print(f"{response}")

print("Testing REV:")
response = c.talk("REV " + l_seqs[1])
print(f"{response}")

print("Testing GENE:")
for g in l_genes:
    response = str(c.talk("GENE " + g))
    print(f"{response}")