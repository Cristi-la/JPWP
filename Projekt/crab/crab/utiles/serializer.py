from crab.response.exceptions import IncorectResponseObject
from crab.response.generic import JsonResponse
from crab.server.handlers.LoggerHandler import CrabLogger
from crab.utiles.register import Error404Handler, Error403Handler, Error500Handler, Error400Handler
import importlib
import time
from functools import wraps

def add_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        if not isinstance(result, JsonResponse):
            raise IncorectResponseObject('Invalid response for this decorator')

        result.set_cookie('execution_time', execution_time)

        return result

    return wrapper

def fun_execution_logger(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        settings = importlib.import_module("settings")
        logger = CrabLogger(__name__, settings)

        logger.info(f"Calling function: '{fun.__name__}''")
        result = fun(*args, **kwargs)
        logger.info(f"Function '{fun.__name__}' completed")

        return result

    return wrapper

def validate_arguments(*arg_types, **kwarg_types):
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            settings = importlib.import_module("settings")
            logger = CrabLogger(__name__, settings)

            for arg, arg_type in zip(args, arg_types):
                if not isinstance(arg, arg_type):
                    logger.error(f"Fun {fun.__name__}: expected {arg_type.__name__}, but got {type(arg).__name__}")

            for arg_name, arg_type in kwarg_types.items():
                if arg_name in kwargs and not isinstance(kwargs[arg_name], arg_type):
                    logger.error(f"Fun {fun.__name__}: expected {arg_type.__name__} for '{arg_name}', but got {type(kwargs[arg_name]).__name__}")

            return fun(*args, **kwargs)

        return wrapper

    return decorator