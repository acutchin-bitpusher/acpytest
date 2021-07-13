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

##  FOR SQL DB TESTING
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import text
#import pymysql

##  FOR STRESS
#import argparse
#import multiprocessing
#import psutil
#import signal
#import sys
#import time

app = Flask(__name__)

@app.route("/")
def hello():

  #response.content_type = "text/plain"
  response = ""
  response += "Hello from acpytest! <br/> \n"
  response += "version: " + version + " <br/> \n"
  response += "<br/> \n"
  response += db_config_html(environ)

#  response += "SQLALCHEMY CONFIG AND DB OBJECT CREATION <br/> \n"
#  response += "---------------------------------------- <br/> \n"
#  app.config['SQLALCHEMY_DATABASE_URI']        = DB_CONFIG["URI"]
#  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
#  ##  DON'T DO THIS - CAUSES db.engine.execute ERROR: 'True'
#  #app.config['SQLALCHEMY_ECHO'] = 'True'
#  try:
#    db = SQLAlchemy(app)
#    response += '--> SUCCESS! <br/> \n'
#  except Exception as e:
#      response += '--> ERROR: ' + str(e) + ' <br/> \n'
#  response += "<br/> \n"
#
#  response += "TEST DB CONNECTION <br/> \n"
#  response += "------------------ <br/> \n"
#  try:
#      db.engine.execute(text("SELECT 1"))
#      response += '--> SUCCESS! <br/> \n'
#  except Exception as e:
#      response += '--> ERROR: ' + str(e) + ' <br/> \n'
#  response += "<br/> \n"

#  response += "LIST DB TABLES <br/> \n"
#  response += "------------------ <br/> \n"
#  try:
#    tables = db.engine.table_names()
#    response += "SUCCESS! DB TABLES:"
#    response += str(tables)
#  except Exception as e:
#    tables = "FAILED" + str(e) + ' <br/> \n'
#  response += "<br/> \n"

  response += sqlalchemy_db_test_html(environ,app)
  response += env_var_list_html(environ)

  return response

##  STUFF FOR STRESS TESTING
#def _spin():
#    while True:
#        pass
#def stress_processes(num_processes):
#    for _ in range(num_processes):
#        multiprocessing.Process(target=_spin).start()
#def stress_ram(ram_to_allocate_mb):
#    """
#    Attempts to allocate the given amount of RAM to the running Python process.
#    :param ram_to_allocate_mb: the amount of RAM in megabytes to allocate
#    :return: None
#    """
#    try:
#        # Each element takes approx 8 bytes
#        # Multiply n by 1024**2 to convert from MB to Bytes
#        _ = [0] * int(((ram_to_allocate_mb / 8) * (1024 ** 2)))
#        while True:
#            # This is just to keep the process running until halted
#            time.sleep(1)
#    except MemoryError:
#        # We didn't have enough RAM for our attempt, so we will recursively try
#        # smaller amounts 10% smaller at a time
#        stress_ram(int(ram_to_allocate_mb * 0.9))


@app.route('/stress', methods=['GET'])
def index():
  response = ""
  response += "Welcome to Stress! <br/> \n"
  response += "<br/> \n"
  response += uri_request_args_html(request)
  response += env_var_list_html(environ)
  return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
