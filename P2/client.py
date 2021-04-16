import socket
PORT = 8080
IP = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode("HELLO FROM THE CLIENT!!!"))
s.close()