from flask import Flask, jsonify, request
import re
import random
from Bot import Bot

app = Flask(__name__)
app.config["DEBUG"] = True
myBot = Bot() #instance of bot class from Bot.py file

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
  return response

@app.route('/fortune', methods=['GET'])
def fortune():
    return jsonify({
        'data':'How many of you believe?',
        'status' : 'awesome'
    }), 200

@app.route('/hello', methods=['GET'])
def routeHere():
    myBot.check()
    print(request.args.get('question', default='*', type=str))
    return jsonify('Hello, how are doing today? Is there anything I can help with? '), 200

@app.route('/convo', methods=['GET'])
def convoRoute():
    myBot.check()
    returner = myBot.chat(request.args.get('question', default='N/A', type=str))
    return jsonify(returner), 200

@app.route('/', methods=['GET'])
def checkServer():
    return jsonify('this is your server'), 200

# run using following command: FLASK_APP=app.py flask run