from crab.response.generic import BaseResponse, JsonResponse, XmlResponse, PDFResponse, ImageResponse
from crab.utiles.register import Error404Handler, Error403Handler, Error500Handler
from crab.utiles.register import post, get

import json
from datetime import datetime, timedelta

import models

def home(request):
    response = JsonResponse(json.dumps({'message': f'Hello World!'}))
    expiration_time = datetime.now() + timedelta(days=7)
    response.set_cookie('username', 'john', expires=expiration_time)

    return response

def hello(request, name):
    response_data = {'message': f'Hello {name}'}
    return JsonResponse(json.dumps(response_data))

def request(request):
    return JsonResponse(json.dumps({
        'status_code': request.status_code,
    }))


def xml(request):
    return XmlResponse('<?xml version="1.0" encoding="ISO-8859-1"?><catalog><title>Empire Burlesque</title></catalog>')

# Nie działa naprawić
# def pdf(request):
#     pdf_path = 'example.pdf'
#     return PDFResponse(pdf_path)

def image(request):
    image_path = 'example.png'
    return ImageResponse(image_path)

# Sprawdzić czy działa 
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