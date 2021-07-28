from os import environ
import sys
import json
from flask import Flask, request

##  LOCAL LIBRARIES
from env_vars import *
from db_config import *
from sql import *
from version import *
from stress import *

app = Flask(__name__)

@app.route("/")
def hello():

  #response.content_type = "text/plain"
  response = ""
  response += "Hello yeah from acpytest! <br/> \n"
  response += "version: " + version + " <br/> \n"
  response += "<br/> \n"
  response += db_config_html(environ)
  response += sqlalchemy_db_test_html(environ,app)
  response += env_var_list_html(environ)
  return response

@app.route('/stress', methods=['GET'])
def index():
  response  = ""
  response += "acpystress, version: " + version + " <br/> \n"
  response += "URI request args: "
  for key, value in request.args.items():
    response += '{0}={1}, '.format(key, value)
  response += "<br/> \n"
  #response += stress() ##  FIXED ARGS
  response += stress(
    cpu=request.args.get('cpu'),
    #vm=request.args.get('vm')
    timeout=request.args.get('timeout')
  )
  return response

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)

