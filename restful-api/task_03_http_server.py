#!/usr/bin/python3
"""
Simple HTTP Server

This script sets up a basic HTTP server using the http.server module.
It handles different endpoints and serves
text or JSON responses depending on the path requested by the client.

Classes:
    SimpleHTTPRequestHandler: Subclass of BaseHTTPRequestHandler that
    implements GET request handling.

Functions:
    run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
    port=8000):
        Starts the HTTP server using the provided handler and server class on
        the specified port.
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that handles GET requests for various
    endpoints.

    Methods:
        do_GET(self):
            Handles GET requests and routes them to specific endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests and returns different responses based on the
        requested path.

        Supported paths:
            - '/': Returns a plain text message "Hello, this is a simple API!".
            - '/data': Returns a JSON object with sample data.
            - '/status': Returns a JSON object indicating the API status as
            "OK".
            - '/info': Returns a JSON object with version information and a
            description of the API.
            - Any other path: Returns a 404 error with a JSON message
            indicating that the endpoint is not found.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Sample JSON data
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status_data = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status_data).encode('utf-8'))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_data = {
                "error": "Endpoint not found"
            }
            self.wfile.write(json.dumps(error_data).encode('utf-8'))


def run(
    server_class=HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
    port=8000
):
    """
    Starts the HTTP server.

    Args:
        server_class (type): The HTTP server class to use (default is
        HTTPServer).
        handler_class (type): The request handler class to use (default is
        SimpleHTTPRequestHandler).
        port (int): The port number to run the server on (default is 8000).

    This function sets up the server and keeps it running to handle incoming
    requests.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting http server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
