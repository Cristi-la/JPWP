from views import home, hello, request, return_error, xml, image
import re


url_patterns = [
    ('/', home),
    ('/xml', xml),
    ('/image', image),
    # ('/pdf', pdf), Not working correctly at the time being
    ('/request', request),
    ('/error_500', return_error),
    (re.compile(r'^/hello/(?P<name>\w+)/$'), hello),
]