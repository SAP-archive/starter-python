import recastai

from config import config

def replyMessage(message):
    request = recastai.Request(config['recast']['token'])

    text = message.content.attachment.content
    senderId = message.senderId

    response = request.converse.textConverse(text, senderId)

    for reply in response.replies:
        message.addReply({ 'type': 'text', 'content': reply })

    message.reply()
