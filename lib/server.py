from simplerouter import Router
from wsgiref.simple_server import make_server

from config import config
from bot import bot

router = Router()
# view names are composed of modulename:function
router.add_route('/', bot, method='GET')

application = router.as_wsgi

if __name__=='__main__':
    make_server('', config['port'], application).serve_forever()
