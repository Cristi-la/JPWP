from views import home, hello, request, return_error
import re


url_patterns = [
    ('/', home),
    ('/request', request),
    ('/error_500', return_error),
    (re.compile(r'^/hello/(?P<name>\w+)/$'), hello),
]