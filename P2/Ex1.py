from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"------| Practice {PRACTICE}, Exercise {EXERCISE} |-----")

IP = "127.0.0.1"
PORT = 52123
c = Client(IP, PORT)
c.advanced_ping()
