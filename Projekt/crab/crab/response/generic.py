import json



class JsonResponse:
    def __init__(self, data, status_code=202):
        self.data = data
        self.status_code = status_code

    def get_header(self):
        headers = {
            'Content-type': 'application/json',
            'Content-Length': str(len(self.data))
        }
        return headers

    def get_content(self):
        return self.data

    
    def get_status_code(self):
        return self.status_code