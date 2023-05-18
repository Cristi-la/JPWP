from crab.response.generic import BaseResponse, JsonResponse, XmlResponse, PDFResponse, ImageResponse
from crab.utiles.register import Error404Handler, Error403Handler, Error500Handler
from crab.utiles.register import post, get
from crab.utiles.serializer import add_time

import json
from datetime import datetime, timedelta
from models import *

@add_time
def home(request):
    response = JsonResponse(json.dumps({'message': 'Hello World!'}))
    expiration_time = datetime.now() + timedelta(days=7)
    response.set_cookie('username', 'john', expires=expiration_time)

    return response

@get
def hello(request, name):
    response_data = {'message': f'Hello {name}'}
    return JsonResponse(json.dumps(response_data))

def request(request):
    return JsonResponse(json.dumps({
        'status_code': request.status_code,
    }))


def xml(request):
    return XmlResponse('<?xml version="1.0" encoding="ISO-8859-1"?><catalog><title>Empire Burlesque</title></catalog>')

def image(request):
    image_path = 'example.png'
    return ImageResponse(image_path)

@post
def only_post(request):
    response_data = {'message': 'Only user who post data can access this data'}
    return JsonResponse(response_data)

def return_error(request, name):
    response_data = {'message': f'Hello {name}'}
    return JsonResponse(response_data)

def database(request):

    def datetime_encoder(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()

    Addresses.create()
    Residents.create()
    if len(Addresses.read()) < 5:
        addresses_dict = [{'street': 'Krakowska', 'city': 'Krakow', 'province': 'Malopolska', 'zip_code': '30-320'},
                        {'street': 'Mazowiecka', 'city': 'Krakow', 'province': 'Malopolska', 'zip_code': '30-424'},
                        {'street': 'Zalewska', 'city': 'Krakow', 'province': 'Malopolska', 'zip_code': '30-333'},
                        {'street': 'Brzozowa', 'city': 'Krakow', 'province': 'Malopolska', 'zip_code': '30-222'},
                        {'street': 'Kremowa', 'city': 'Krakow', 'province': 'Malopolska', 'zip_code': '30-111'},]
        Addresses.bulk_create(addresses_dict)

    # Addresses.clear()
    data = Addresses.read()

    result = ''
    for i in data:
        data_dict = {'id': i.id, 'created_at': i.created_at, 'updated_at': i.updated_at, 'street': i.street,
                     'city': i.city, 'province': i.province, 'zip_code': i.zip_code}
        result += json.dumps(data_dict, default=datetime_encoder)

    return JsonResponse(json.dumps(result))

# Error handlers
#@Error404Handler
#def error404_view(request):
#    return JsonResponse(json.dumps({'status_code': 'test404'}))

@Error403Handler
def error403_view(request):
    return JsonResponse(json.dumps({'status_code': 'test403'}))

@Error500Handler
def error500_view(request):
    return JsonResponse(json.dumps({'status_code': 'test500'}))