from views import home, hello, request, return_error, database, xml, image, only_post
import re


url_patterns = [
    ('/', home),
    ('/xml', xml),
    ('/only_post', only_post),
    ('/image', image),
    ('/request', request),
    ('/error_500', return_error),
    ('/database', database),
    (re.compile(r'^/hello/(?P<name>\w+)/$'), hello),
]