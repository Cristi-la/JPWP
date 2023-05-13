from crab.server.handlers.LoggerHandler import CrabLogger
from crab.utiles.register import ErrorHandler


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
        self.query = request
        self.client_address = client_address
        self.server = server

        super().__init__(request, client_address, server)

    
    def handle_request(self):
        try:
            for url_pattern in self.url_patterns:
                if isinstance(url_pattern[0], str):
                    self.logger.debug(f"Test str path: {self.path}")
                    if url_pattern[0] == self.path:
                        self.logger.debug(f"Path Match: {self.path}")
                        response = url_pattern[1](self)
                        self.send_headers(response)
                        self.write_content(response)
                        break
                else:
                    self.logger.debug(f"Test regex path: {self.path}")
                    match = url_pattern[0].match(self.path)
                    if match:
                        self.logger.debug(f"Path Match: {self.path}")
                        params = match.groupdict()
                        self.logger.debug(f"URL params: {params}")
                        response = url_pattern[1](self, **params)
                        self.send_headers(response)
                        self.write_content(response)
                        break
            else:
                self.status_code = http.HTTPStatus.NOT_FOUND
                self.logger.debug(f"GET {self.path}:{self.status_code}")
                response = ErrorHandler._error_handler(self)
                self.logger.debug(f"Returned Error: {ErrorHandler._error_handler}:{self.status_code} \n, {str(response)}, {type(response)}")
                self.send_headers(response)
                self.write_content(response)
                
        except Exception as error:
            self.status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR
            self.logger.error(f"GET {self.path}:{self.status_code}, ERROR: {error}")
            response = ErrorHandler.error(self)
            self.logger.debug(f"Returned Error: {str(response)}, {type(response)}")
            self.send_headers(response)
            self.write_content(response)
           

    def send_headers(self, response):
        self.send_response(response.status_code)

        headers = dict(response.get_header().items())
        for key, value in headers.items():
            self.send_header(key, value)

    def write_content(self, response):
        self.end_headers()
        self.wfile.write(response.get_content().encode("utf-8"))
        self.status_code = response.status_code
    
    def do_GET(self):
        self.logger.debug(f'User request path: {self.path}')
        self.handle_request()