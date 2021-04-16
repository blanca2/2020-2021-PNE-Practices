import socket
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("Ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up")
        except ConnectionRefusedError:
            print("Could not connect to server. Is it running? Check your IP and PORT")

    def __str__(self):
        return "Connection to SERVER at" + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        #--Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.ip, self.port))
        print("To Server:", msg)
        s.send(msg.encode())
        response = s.recv(2840).decode("utf-8")
        s.close()
        return "From server: " + response
    def debug_talk (self, msg):
        response = self.talk(msg)
        color_response = colored(response, "green")
        print("From server: ", color_response)