import socket
PORT = 52123
IP = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode("HELLO FROM THE CLIENT!!!"))
s.close()