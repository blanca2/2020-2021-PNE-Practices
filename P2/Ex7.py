from Client0 import Client

from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"------| Practice {PRACTICE}, Exercise {EXERCISE} |-----")

IP = "127.0.0.1"
PORT = 52123
c = Client(IP, PORT)
c2 = Client(IP, PORT_2)

s1 = Seq()
s1.read_fasta("::/Session 4/FRAT1")

count = 0
i = 0
while i < len(s1.strbases) and count < 5:
    fragment = s1.strbases[i:i+10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    if count % 2 == 0:
        print(c2.talk("Fragment" + str(count) + ":" + fragment))
    else:
        print(c.talk("Fragment" + str(count) + ":" + fragment))