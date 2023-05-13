from crab.response.generic import JsonResponse

import http
import json
from functools import wraps

class BaseErrorHandler:
    _error_handler = None
    status_code = http.HTTPStatus.NOT_IMPLEMENTED

    def __init__(self, error_fn):
        self.error_fn = error_fn

    def __call__(self, *args, **kwargs):
        return self.error_fn(*args, **kwargs)

# 404 error page handler
class Error404Handler(BaseErrorHandler):
    status_code = http.HTTPStatus.NOT_FOUND

    def __init__(self, error_fn):
        super().__init__(error_fn)
        Error404Handler._error_handler = error_fn

    @staticmethod
    def run(request):
        return Error404Handler._error_handler(request) if Error404Handler._error_handler else Error404Handler.error(request)
    
    @staticmethod
    def error(request):
        return JsonResponse(json.dumps({'status_code': http.HTTPStatus.NOT_FOUND,'error': ''}))

# 500 error page handler
class Error500Handler(BaseErrorHandler):
    status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, error_fn):
        super().__init__(error_fn)
        Error500Handler._error_handler = error_fn

    @staticmethod
    def run(request):
        return Error500Handler._error_handler(request) if Error500Handler._error_handler else Error500Handler.error(request)
    
    @staticmethod
    def error(request):
        return JsonResponse(json.dumps({'status_code': http.HTTPStatus.NOT_FOUND,'error': ''}))


# 403 error page handler
class Error403Handler(BaseErrorHandler):
    status_code = http.HTTPStatus.FORBIDDEN

    def __init__(self, error_fn):
        super().__init__(error_fn)
        Error403Handler._error_handler = error_fn

    @staticmethod
    def run(request):
        return Error403Handler._error_handler(request) if Error403Handler._error_handler else Error403Handler.error(request)
    
    @staticmethod
    def error(request):
        return JsonResponse(json.dumps({'status_code': http.HTTPStatus.NOT_FOUND,'error': ''}))
   
    

def post(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method == "POST":
            return view_func(request, *args, **kwargs)
        else:
            return Error403Handler.run(request)
    return wrapper

def get(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method == "GET":
            return view_func(request, *args, **kwargs)
        else:
            return  Error403Handler.run(request)
    return wrapper