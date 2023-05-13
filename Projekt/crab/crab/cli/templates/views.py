from crab.response.generic import JsonResponse
from crab.utiles.register import ErrorHandler
import json


def home(request):
    response_data = {'message': 'Hello, world!'}
    return JsonResponse(json.dumps(response_data))

def request(request):
    return JsonResponse(json.dumps({
        'status_code': request.status_code,
        'current_path': request.current_path,
    }))

def hello(request, name):
    response_data = {'message': f'Hello {name}'}
    return JsonResponse(json.dumps(response_data))

def return_error(request, name):
    response_data = {'message': f'Hello {name}'}
    return JsonResponse(response_data)


@ErrorHandler
def error_view(request):
    return JsonResponse(json.dumps(
        {
            'status_code': request.status_code,
            'api': '1.0.0',
        }
    ), status_code=request.status_code)