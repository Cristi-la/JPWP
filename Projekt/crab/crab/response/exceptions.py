from crab.server.handlers.LoggerHandler import CrabLogger

import importlib

class BaseError(Exception):
    MESSAGE='Base Exception'

    def __init__(self):
        super().__init__(self.MESSAGE)
        self.settings = importlib.import_module("settings")
        self.logger = CrabLogger(__name__, self.settings)
        self.logger.warning(self.MESSAGE)

    def __init__(self, message):
        super().__init__(self.MESSAGE)
        self.settings = importlib.import_module("settings")
        self.logger = CrabLogger(__name__, self.settings)
        self.logger.warning(str(message))

    @staticmethod
    def log_error(message):
        settings = importlib.import_module("settings")
        logger = CrabLogger(__name__, settings)
        logger.warning(str(message))

class InvalidDataError(BaseError):
    MESSAGE = 'The view data is inavlid!'


class IncorectResponseObject(BaseError):
    MESSAGE = 'This response object is incorect'
