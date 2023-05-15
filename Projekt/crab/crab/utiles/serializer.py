from crab.response.exceptions import IncorectResponseObject
from crab.response.generic import JsonResponse

import json
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