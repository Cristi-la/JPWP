from crab.response.mixins import FileMixin
from crab.response.exceptions import InvalidDataError

import json
from xml.etree import ElementTree
from PyPDF2 import PdfReader

class BaseResponse:
    CONTENT_TYPE = 'text/html'

    def __init__(self, data, status_code=202):
        if not self.is_valid_data(data):
            raise InvalidDataError('Invalid data')
        self.data = data
        self.status_code = status_code
        self.cookies = {}

    def is_valid_data(self, data):
        return True  # Implement your data validation logic here

    def get_content(self):
        return self.data.encode('utf-8')
    
    def get_status_code(self):
        return self.status_code
    
    def get_header(self):
        header = {
            'Content-type': self.CONTENT_TYPE,
            'Content-Length': str(len(self.data))
        }
        for cookie_name, cookie_data in self.cookies.items():
            cookie_str = f'{cookie_name}={cookie_data["value"]}; Path=/'
            if cookie_data.get("expires"):
                cookie_str += f'; Expires={str(cookie_data["expires"])}'
            header['Set-Cookie'] = cookie_str
        return header

    def set_cookie(self, name, value, expires=None):
        self.cookies[name] = {"value": value, "expires": expires}


class JsonResponse(BaseResponse):
    CONTENT_TYPE = 'application/json'

    def __init__(self, *args, **kwatgs):
        super().__init__(*args, **kwatgs)

class XmlResponse(BaseResponse):
    CONTENT_TYPE = 'application/xml'

    def __init__(self, *args, **kwatgs):
        super().__init__(*args, **kwatgs)

class ImageResponse(FileMixin, BaseResponse):
    CONTENT_TYPE = 'image/jpeg'

    def __init__(self, *args, **kwatgs):
        super().__init__(*args, **kwatgs)

    def is_valid_data(self, data):
        # Check that data is a valid image file
        try:
            from PIL import Image
            Image.open(data)
            return True
        except InvalidDataError:
            return False


class PDFResponse(FileMixin, BaseResponse):
    CONTENT_TYPE = 'application/pdf'

    def __init__(self, *args, **kwatgs):
        super().__init__(*args, **kwatgs)

    def is_valid_data(self, data):
        # Check that data is a valid PDF file
        try:
            PdfReader(data)
            return True
        except InvalidDataError:
            return False