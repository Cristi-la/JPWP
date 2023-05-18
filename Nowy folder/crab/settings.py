import logging

# Server settings
HOST = "localhost"  # Leave empty for all available network interfaces
PORT = 8000  # Change this to any port you want
USE_SSL = False  # Set to True to enable HTTPS support
CERT_FILE = "cert.pem"  # Path to SSL certificate file
KEY_FILE = "key.pem"  # Path to SSL key file

# Logging settings
LOG_TO_CONSOLE = True  # Set to True to log messages to console
LOG_FILE = "server.log"  # Path to log file
LOG_LEVEL = logging.DEBUG  # Set the log level: DEBUG, INFO, WARNING, ERROR, CRITICAL

DATABASE = {
    'local': {
        'database_name': 'mydatabase.db',
        'engine': 'sqlite:///',
    },
    'user': {
        'ip': '',
        'username': '',
        'password': '',
        'engine': '',
    }
}