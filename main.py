from os import environ
import sys
import json
from flask import Flask, request

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

@app.route('/stress', methods=['GET'])
def index():
  #response  = "<br/> \n"
  response  = ""
  response += "acpystress, version: " + version + " <br/> \n"
  #response += "<br/> \n"
  response += "URI request args: "
  #response += uri_request_args_html(request)
  for key, value in request.args.items():
    response += '{0}={1}, '.format(key, value)
  #response += "Stressing out... <br/> \n"
  response += "<br/> \n"
#  stress(
#    request.args.get('cores_to_stress', ''),
#    request.args.get('memory_to_allocate', '')
#  )
#  response += stress()
  response += stress(
    cpu=request.args.get('cpu'),
    #vm=request.args.get('vm')
    timeout=request.args.get('timeout')
  )
  return response

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)

