import socket
import pathlib
import termcolor
from urllib.parse import urlparse, parse_qs

IP = "127.0.0.1"
PORT = 8080
HTML_ASSETS = "./html/"

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')

    req_line = lines[0]
    request = req_line.split(' ')[1]
    o = urlparse(request)
    path_name = o.path
    arguments = parse_qs(o.query)

    print("Resource requested: ", path_name)
    print("Parameters: ", arguments)

    termcolor.cprint(req_line), 'green'

    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"
    if path_name == "/":
        body = read_html_file(HTML_ASSETS + "index.html")
    elif "/info/" in path_name:
        try:
            body = read_html_file(HTML_ASSETS + path_name.split('/')[-1] + '.html')
        except FileNotFoundError:
            body = read_html_file(HTML_ASSETS + 'Error.html')
    else:
        body = read_html_file(HTML_ASSETS + 'Error.html')

    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()