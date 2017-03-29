# coding: utf-8

import os
import recastai

from flask import jsonify

def bot(payload):
  connect = recastai.Connect(token=os.environ['REQUEST_TOKEN'], language=os.environ['LANGUAGE'])
  request = recastai.Request(token=os.environ['REQUEST_TOKEN'])

  message = connect.parse_message(payload)

  response = request.converse_text(message.content, conversation_token=message.sender_id)

  replies = [{'type': 'text', 'content': r} for r in response.replies]
  connect.send_message(replies, message.conversation_id)

  return jsonify(status=200)
