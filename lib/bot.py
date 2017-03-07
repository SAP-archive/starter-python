from webob import Response
import recastai

from config import config
from message import replyMessage

def bot(request):
    connect = recastai.Connect(config['recast']['token'], config['recast']['language'])

    return connect.connect.handleMessage(request, Response(), replyMessage)
