#coding: utf-8

from __future__ import print_function

from simplerouter import Router
from wsgiref.simple_server import make_server

from .config import config
from .bot import bot

def run():
    router = Router()

    router.add_route('/', bot, method='POST')

    application = router.as_wsgi

    httpd = make_server('', config['port'], application)

    print('Bot running on port', config['port'])

    httpd.serve_forever()
