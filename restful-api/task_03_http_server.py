#!/usr/bin/python3
"""
Simple HTTP Server

This script sets up a basic HTTP server using the http.server module.
It handles different endpoints and serves text or JSON responses depending
on the path requested by the client, as well as static files from the
current directory.
"""

import http.server
import socketserver
import json
import logging

logging.basicConfig(level=logging.INFO)

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


class CustomHTTPRequestHandler(Handler):
    """
    A custom HTTP request handler that extends SimpleHTTPRequestHandler
    to handle specific endpoints.
    """

    def set_headers(self, status_code, content_type):
        """Set response headers."""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """Handles GET requests and returns different responses based on the
        requested path."""
        logging.info(f"Request path: {self.path}")

        if self.path == '/':
            self.set_headers(200, 'text/plain')
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.set_headers(200, 'application/json')
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.set_headers(200, 'application/json')
            status_data = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status_data).encode('utf-8'))

        elif self.path == '/info':
            self.set_headers(200, 'application/json')
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode('utf-8'))

        else:
            # Gestion des erreurs pour les endpoints non définis
            self.set_headers(404, 'application/json')
            error_data = {
                "error": "Endpoint not found"
            }
            self.wfile.write(json.dumps(error_data).encode('utf-8'))


def run(
        server_class=http.server.HTTPServer,
        handler_class=CustomHTTPRequestHandler
        ):
    """Starts the HTTP server."""
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting http server on port {PORT}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server is shutting down.")
        httpd.server_close()


if __name__ == "__main__":
    run()
