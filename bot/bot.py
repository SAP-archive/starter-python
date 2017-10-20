# coding: utf-8

import os
import recastai

from flask import jsonify

def bot(payload):
  connect = recastai.Connect(token=os.environ['REQUEST_TOKEN'], language=os.environ['LANGUAGE'])
  request = recastai.Request(token=os.environ['REQUEST_TOKEN'])

  message = connect.parse_message(payload)

  response = request.analyse_text(message.content)

  intent = response.intent

  if intent is None:
    reply = "I'm sorry but I don't understand what you are talking about"
  else:
    reply = 'I understand that you talk about {}'.format(intent.slug)

  replies = [{'type': 'text', 'content': reply}]
  connect.send_message(replies, message.conversation_id)

  return jsonify(status=200)
