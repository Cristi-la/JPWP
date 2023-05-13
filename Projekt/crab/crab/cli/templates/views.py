from crab.response.generic import JsonResponse
from crab.utiles.register import Error404Handler, Error403Handler, Error500Handler
from crab.utiles.register import post, get
import json

import models

def home(request):
    response_data = {'message': 'Hello, world!'}
    return JsonResponse(json.dumps(response_data))

def request(request):
    return JsonResponse(json.dumps({
        'status_code': request.status_code,
    }))

def hello(request, name):
    response_data = {'message': f'Hello {name}'}
    return JsonResponse(json.dumps(response_data))


@post
def return_error(request, name):
    response_data = {'message': f'Hello {name}'}
    return JsonResponse(response_data)


# Error handlers
@Error404Handler
def error404_view(request):
    return JsonResponse(json.dumps({'status_code': 'test404'}))

@Error403Handler
def error403_view(request):
    return JsonResponse(json.dumps({'status_code': 'test403'}))

@Error500Handler
def error500_view(request):
    return JsonResponse(json.dumps({'status_code': 'test500'}))