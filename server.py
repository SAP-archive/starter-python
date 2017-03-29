#coding: utf-8

import os

from flask import Flask, request

from bot.bot import bot


app = Flask(__name__)

@app.route("/", methods=['POST'])
def root():
  return bot(request)

app.run(port=os.environ['PORT'])
