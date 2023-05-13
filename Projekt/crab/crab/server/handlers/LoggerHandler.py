import logging

class CrabLogger(logging.Logger):
    def __init__(self, name, settings):
        super().__init__(name)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        if settings.LOG_TO_CONSOLE:
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            self.addHandler(handler)
        if settings.LOG_FILE:
            handler = logging.FileHandler(settings.LOG_FILE)
            handler.setFormatter(formatter)
            self.addHandler(handler)
        self.setLevel(settings.LOG_LEVEL)
