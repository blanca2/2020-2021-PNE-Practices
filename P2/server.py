import socket
PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUEST = 5
# counting the number of connections
number_con = 0
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    serversocket.listen(MAX_OPEN_REQUEST)

    while True:
        print("Waiting for connections at{}, {}".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        number_con += 1

        print("CONNECTION: {}. From the IP: {}".format(number_con, address))
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        message = "Hello world"
        send_bytes = str.encode(message)
        clientsocket.send(send_bites)
        clientsocket.close()

except socket.error:
    print("Problems using port{}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()