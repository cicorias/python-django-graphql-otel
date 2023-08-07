#!/usr/bin/env python3
# importing all the functions
# from http.server module
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env


# creating a class which includes
class SimpleServer(BaseHTTPRequestHandler):

    # creating a function for Get Request
    def do_GET(self):
        # Success Response --> 200
        self.send_response(200)
        # Type of file that we are using for creating our
        # web server.
        self.send_header('content-type', 'text/html')
        self.end_headers()
        # what we write in this function it gets visible on our
        # web-server
        self.wfile.write('<h1>hello from SimpleServer</h1>'.encode())


# this is the object which take port
# number and the server-name
# for running the server
port = HTTPServer(('', 8000), SimpleServer)

# this is used for running our
# server as long as we wish
# i.e. forever
port.serve_forever()
