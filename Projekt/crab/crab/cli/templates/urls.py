from views import home, hello, request, return_error, xml, pdf, image
import re


url_patterns = [
    ('/', home),
    ('/xml', xml),
    ('/image', image),
    ('/pdf', pdf),
    ('/request', request),
    ('/error_500', return_error),
    (re.compile(r'^/hello/(?P<name>\w+)/$'), hello),
]