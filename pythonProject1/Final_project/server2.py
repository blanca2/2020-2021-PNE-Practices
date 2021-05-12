import http.server
import socketserver
import termcolor
import pathlib
import jinja2  #for creating dynamic webpages, from it we import Template
from urllib.parse import urlparse, parse_qs
import server_utils as su
import requests
import json

def read_template_html_file(filename):
    #create template object, can't be directly sent to the browser as it only reads plain text, files or html (template is none of them), we transform it by render function
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content
# Define the Server's port
PORT = 8081

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_post(self):
        print(self)

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)
        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        # Message to send back to the client
        context = {}
        if path_name == '/':
            contents = read_template_html_file('./html/index.html').render(context=context)
        elif path_name == '/listSpecies':
            contents = requests.get('http://rest.ensembl.org/info/species?content-type=application/json')
            contents = contents.json()
            dict_contents = contents
            species = dict_contents['species']
            num_species = len(species)
            exit(0)
            pass
        else:
            contents = su.read_template_html_file("html/error.html").render()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()