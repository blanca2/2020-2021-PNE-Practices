from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 4

print(f"------| Practice {PRACTICE}, Exercise {EXERCISE} |-----")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)

print(c)
c.debug_talk('"Message 1---")
c.debug_talk("Message 2: Testing !!!")
