from crab.response.generic import JsonResponse

import http
import json


class ErrorHandler:
    _error_handler = []

    def __init__(self, error_fn):
        self.error_fn = error_fn
        ErrorHandler._error_handler = self.error_fn

    def __call__(self, *args, **kwargs):
        return self.error_fn(*args, **kwargs)

    @staticmethod
    def error(request):
        return JsonResponse(json.dumps(
            {
                'status_code': request.status_code,
                'api': '1.0.0',
            }
        ), status_code=request.status_code)