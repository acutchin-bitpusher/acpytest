from os import environ
import sys
import json
from flask import Flask, request
from flask_socketio import SocketIO

##  LOCAL LIBRARIES
from env_vars import *
from db_config import *
from uri_request import *
from sql import *
from version import *
from stress import *

#import psutil

app = Flask(__name__)

@app.route("/")
def hello():

  #response.content_type = "text/plain"
  response = ""
  response += "Hello from acpytest! <br/> \n"
  response += "version: " + version + " <br/> \n"
  response += "<br/> \n"
  response += db_config_html(environ)
  response += sqlalchemy_db_test_html(environ,app)
  response += env_var_list_html(environ)
  return response

@app.route('/stress/', methods=['GET'])
def index():
  response = ""
  response += "Welcome to Stress! <br/> \n"
  response += "version: " + version + " <br/> \n"
  response += "<br/> \n"
  response += uri_request_args_html(request)
  response += "Stressing out..."
  stress(
    request.args.get('cores_to_stress', ''),
    request.args.get('memory_to_allocate', '')
  )
  return response

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=80)
    ##  PER: https://stackoverflow.com/questions/53522052/flask-app-valueerror-signal-only-works-in-main-thread
    socketio.run(app)

