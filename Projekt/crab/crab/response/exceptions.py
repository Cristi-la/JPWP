from crab.server.handlers.LoggerHandler import CrabLogger

import importlib


class InvalidDataError(Exception):
    MESSAGE = 'The view data is inavlid!'

    def __init__(self):
        super().__init__(InvalidDataError.MESSAGE)
        self.settings = importlib.import_module("settings")
        self.logger = CrabLogger(__name__, self.settings)
        self.logger.warning(InvalidDataError.MESSAGE)

    def __init__(self, message):
        super().__init__(str(message))
        self.settings = importlib.import_module("settings")
        self.logger = CrabLogger(__name__, self.settings)
        self.logger.warning(str(message))

    @staticmethod
    def log_error(message):
        settings = importlib.import_module("settings")
        logger = CrabLogger(__name__, settings)
        logger.warning(str(message))
