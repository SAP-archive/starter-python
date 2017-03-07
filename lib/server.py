from simplerouter import Router
from wsgiref.simple_server import make_server

from config import config
from bot import bot

# TODO: think around that
# Maybe use another router
def handler(request):
    return bot(request.body)

def run():
    router = Router()

    router.add_route('/', handler, method='GET')

    application = router.as_wsgi

    httpd = make_server('', config['port'], application)

    print 'Bot running on port', config['port']

    httpd.serve_forever()
