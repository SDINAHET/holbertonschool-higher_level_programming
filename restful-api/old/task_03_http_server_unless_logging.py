#!/usr/bin/python3
"""
Simple HTTP Server Module

Ce module implémente un serveur HTTP simple en utilisant le module http.server de la bibliothèque standard de Python.
Le serveur gère différents points de terminaison (endpoints) et répond en fonction du chemin demandé par le client.
Il sert également des fichiers statiques depuis le répertoire courant.

Fonctionnalités :
- Répond à des requêtes GET sur différents endpoints.
- Sert des réponses en texte brut ou en JSON selon le chemin demandé.
- Gère les erreurs pour les endpoints non définis avec un statut 404.

Usage :
    python3 task_03_http_server.py

Endpoints disponibles :
- `/` : Retourne un message de bienvenue en texte brut.
- `/data` : Retourne un objet JSON contenant des informations de base.
- `/status` : Retourne l'état de l'API.
- `/info` : Retourne les informations de version.
- Toute autre route : Retourne une erreur 404 avec un message approprié.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Gestionnaire de requêtes HTTP personnalisé.

    Cette classe gère les requêtes HTTP entrantes et répond en fonction du chemin demandé.
    Elle hérite de BaseHTTPRequestHandler et surcharge la méthode do_GET pour traiter les requêtes GET.
    """

    def do_GET(self):
        """
        Gère les requêtes GET.

        En fonction du chemin de la requête, cette méthode répond avec :
        - Un message de bienvenue en texte brut pour la racine (`/`).
        - Un objet JSON avec des données spécifiques pour `/data`.
        - Un message de statut pour `/status`.
        - Des informations de version pour `/info`.
        - Une erreur 404 pour les chemins non définis.
        """
        # Analyse du chemin de la requête
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            response = 'Hello, this is a simple API!'
            self.wfile.write(response.encode('utf-8'))

        elif path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response = json.dumps(data)
            self.wfile.write(response.encode('utf-8'))

        elif path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            response = 'OK'
            self.wfile.write(response.encode('utf-8'))

        elif path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            # Gestion des endpoints non définis
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'error': 'Endpoint not found'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def log_message(self, format, *args):
        """
        Override de la méthode de logging par défaut pour désactiver les messages de log.

        Cela empêche les messages de log par défaut d'être affichés dans la console.
        """
        pass  # Ne rien faire pour désactiver les logs par défaut


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Démarre le serveur HTTP.

    Args:
        server_class (HTTPServer, optional): Classe du serveur à utiliser. Par défaut, HTTPServer.
        handler_class (BaseHTTPRequestHandler, optional): Classe du gestionnaire de requêtes. Par défaut, SimpleHTTPRequestHandler.
        port (int, optional): Port sur lequel le serveur écoutera. Par défaut, 8000.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serveur HTTP démarré sur le port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Serveur HTTP arrêté.')


if __name__ == "__main__":
    run()
