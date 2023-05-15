from crab.server.handlers.ViewHandler import ViewHandler 
from crab.server.handlers.ServerHandler import ThreadedHTTPServer
from crab.server.handlers.LoggerHandler import CrabLogger

import importlib
import os
import ssl

def run_crab(path):

    settings = importlib.import_module('settings')
    logger = CrabLogger("Web", settings)

    with ThreadedHTTPServer((settings.HOST, settings.PORT), ViewHandler) as httpd:
        if settings.USE_SSL and os.path.isfile(settings.CERT_FILE) and os.path.isfile(settings.KEY_FILE):
            httpd.socket = ssl.wrap_socket(
                httpd.socket,
                certfile=settings.CERT_FILE,
                keyfile=settings.KEY_FILE,
                server_side=True
            )
            logger.info(f"Serving HTTPS at https://{settings.HOST}:{settings.PORT}")
        else:
            logger.info(f"Serving HTTP at http://{settings.HOST}:{settings.PORT}")
        httpd.serve_forever()