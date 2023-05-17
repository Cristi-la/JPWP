from crab.server.handlers.LoggerHandler import CrabLogger
from crab.utiles.register import Error404Handler, Error403Handler, Error500Handler
from crab.server.handlers.constans import Methods

from http.server import BaseHTTPRequestHandler

import http
from http.server import BaseHTTPRequestHandler
import importlib




class ViewHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.urls = importlib.import_module("urls")
        self.settings = importlib.import_module("settings")
        self.logger = CrabLogger("ViewHandler", self.settings)

        self.url_patterns = self.urls.url_patterns
        self.status_code = http.HTTPStatus.ACCEPTED
        self.request = request
        self.client_address = client_address
        self.server = server
        self.method = None


        # This data will be passed to each view
        self.data = {
            'url_patterns': self.url_patterns,
            'status_code': self.status_code,
            'client_address': self.client_address,
            'server': self.server,
            'logger': self.logger,
        }

        super().__init__(request, client_address, server)

    
    def handle_request(self):
        self.method = self.command
        self.logger.debug(f"Test HTTPS method: {self.command}")

        if self.method != 'GET' and self.method != 'POST':
            self.status_code = http.HTTPStatus.NOT_FOUND
            response = Error404Handler.run(self)
            self.logger.debug(f"Handler404 {self.path}:{self.status_code}")
            self.get(response)
            return

        try:
            for url_pattern in self.url_patterns:
                if isinstance(url_pattern[0], str):
                    self.logger.debug(f"Test str path: {self.path}")
                    if url_pattern[0] == self.path:
                        self.logger.debug(f"Path Match: {self.path}")
                        response = url_pattern[1](self)
                        self.logger.debug(f"{self.method} {self.path}:{self.status_code}")
                        self.get(response)
                        break
                else:
                    self.logger.debug(f"Test regex path: {self.path}")
                    match = url_pattern[0].match(self.path)
                    if match:
                        self.logger.debug(f"Path Match: {self.path}")
                        params = match.groupdict()
                        self.logger.debug(f"URL params: {params}")
                        response = url_pattern[1](self, **params)
                        self.logger.debug(f"{self.method} {self.path}:{self.status_code}")
                        self.get(response)
                        break
            else:
                self.status_code = http.HTTPStatus.NOT_FOUND
                response = Error404Handler.run(self)
                self.logger.debug(f"Handler404 {self.path}:{self.status_code}")
                self.get(response)
                
        except Exception as error:
            self.status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR
            self.logger.error(f"Handler500 {self.path}:{self.status_code}, ERROR: {error}")
            response = Error500Handler.run(self)
            self.get(response)
           

    def get(self, response):
        self.send_response(response.status_code)

        headers = dict(response.get_header().items())
        for key, value in headers.items():
            self.logger.debug(f'Set header, key: {key}, value: {value}')
            self.send_header(str(key), str(value))
        self.end_headers()
        self.wfile.write(response.get_content())
        self.status_code = response.status_code
    

    # Supported html metods
    def do_GET(self):
        self.logger.debug(f'User `GET` request path: {self.path}')
        self.handle_request()
        self.method = Methods.GET

    def do_POST(self):
        self.logger.debug(f'User `POST` request path: {self.path}')
        self.handle_request()
        self.method = Methods.POST