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

    def do_POST(self):
        """Handle POST requests."""
        logging.info(f"POST request for path: {self.path}")
        path, _ = self.parse_path()

        if path == '/items':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                item = json.loads(post_data)
                if 'id' not in item:
                    self.set_headers(400)
                    self.wfile.write(json.dumps(
                        {"error": "Item must have an 'id' field"})
                                     .encode('utf-8'))
                    return
                self.data_store['items'].append(item)
                self.set_headers(201)
                self.wfile.write(json.dumps(
                    {"message": "Item created", "item": item}).encode('utf-8'))
            except json.JSONDecodeError:
                self.set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid JSON data"})
                                 .encode('utf-8'))
        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"})
                             .encode('utf-8'))

    def do_PUT(self):
        """Handle PUT requests."""
        logging.info(f"PUT request for path: {self.path}")
        path, _ = self.parse_path()

        if path.startswith('/items/'):
            item_id = path.split('/')[-1]
            content_length = int(self.headers.get('Content-Length', 0))
            put_data = self.rfile.read(content_length)
            try:
                new_item = json.loads(put_data)
                for idx, item in enumerate(self.data_store['items']):
                    if item['id'] == item_id:
                        self.data_store['items'][idx] = new_item
                        self.set_headers(200)
                        self.wfile.write(json.dumps(
                            {"message": "Item updated", "item": new_item})
                                         .encode('utf-8'))
                        return
                # If item not found, create it
                self.data_store['items'].append(new_item)
                self.set_headers(201)
                self.wfile.write(json.dumps(
                    {"message": "Item created", "item": new_item})
                                 .encode('utf-8'))
            except json.JSONDecodeError:
                self.set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid JSON data"})
                                 .encode('utf-8'))
        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"})
                             .encode('utf-8'))

    def do_PATCH(self):
        """Handle PATCH requests."""
        logging.info(f"PATCH request for path: {self.path}")
        path, _ = self.parse_path()

        if path.startswith('/items/'):
            item_id = path.split('/')[-1]
            content_length = int(self.headers.get('Content-Length', 0))
            patch_data = self.rfile.read(content_length)
            try:
                updates = json.loads(patch_data)
                for item in self.data_store['items']:
                    if item['id'] == item_id:
                        item.update(updates)
                        self.set_headers(200)
                        self.wfile.write(json.dumps(
                            {"message": "Item updated", "item": item})
                                         .encode('utf-8'))
                        return
                self.set_headers(404)
                self.wfile.write(json.dumps(
                    {"error": "Item not found"}).encode('utf-8'))
            except json.JSONDecodeError:
                self.set_headers(400)
                self.wfile.write(json.dumps(
                    {"error": "Invalid JSON data"}).encode('utf-8'))
        else:
            self.set_headers(404)
            self.wfile.write(json.dumps(
                {"error": "Endpoint not found"}).encode('utf-8'))

    def do_DELETE(self):
        """Handle DELETE requests."""
        logging.info(f"DELETE request for path: {self.path}")
        path, _ = self.parse_path()

        if path.startswith('/items/'):
            item_id = path.split('/')[-1]
            for idx, item in enumerate(self.data_store['items']):
                if item['id'] == item_id:
                    del self.data_store['items'][idx]
                    self.set_headers(200)
                    self.wfile.write(json.dumps(
                        {"message": "Item deleted"}).encode('utf-8'))
                    return
            self.set_headers(404)
            self.wfile.write(json.dumps(
                {"error": "Item not found"}).encode('utf-8'))
        else:
            self.set_headers(404)
            self.wfile.write(json.dumps(
                {"error": "Endpoint not found"}).encode('utf-8'))

    def do_HEAD(self):
        """Handle HEAD requests."""
        logging.info(f"HEAD request for path: {self.path}")
        path, _ = self.parse_path()

        if path == '/':
            self.set_headers(200, 'text/plain')
        elif path == '/items':
            self.set_headers(200)
        elif path.startswith('/items/'):
            self.set_headers(200)
        else:
            self.set_headers(404)

    def do_OPTIONS(self):
        """Handle OPTIONS requests."""
        logging.info(f"OPTIONS request for path: {self.path}")
        self.send_response(200)
        self.send_header(
            'Allow',
            'GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, CONNECT, TRACE'
            )
        self.send_header('Content-Length', '0')
        self.end_headers()

    def do_CONNECT(self):
        """Handle CONNECT requests."""
        logging.info(f"CONNECT request for path: {self.path}")
        # Pour des raisons de sécurité, on ne supporte pas CONNECT
        self.set_headers(501, 'text/plain')
        self.wfile.write(b"CONNECT method not implemented.\n")

    def do_TRACE(self):
        """Handle TRACE requests."""
        logging.info(f"TRACE request for path: {self.path}")
        # Echo back the received request
        self.set_headers(200, 'message/http')
        self.wfile.write(self.requestline.encode('utf-8'))
        for header in self.headers:
            header_line = f"{header}: {self.headers[header]}"
            self.wfile.write(header_line.encode('utf-8') + b'\r\n')
        self.wfile.write(b'\r\n')

    def log_message(self, format, *args):
        """Override to prevent default logging."""
        logging.info("%s - - [%s] %s\n" % (
                    self.client_address[0], self.log_date_time_string(),
                    format % args))


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
