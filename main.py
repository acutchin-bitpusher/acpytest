from os import environ
import sys
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import pymysql

app = Flask(__name__)

@app.route("/")
def hello():

  #response.content_type = "text/plain"

  response = ""

  response += "Hello from acpytest! <br/> \n"
  response += "<br/> \n"

  response += "ENVIRONMENT <br/> \n"
  response += "----------- <br/> \n"
  for k, v in sorted(environ.items()):
    response += ( str(k) + ': ' + str(v) + " <br/> \n" )
  response += "<br/> \n"

  DB_CONFIG = {}
  DB_CONFIG["ENGINE"]   = environ.get("DB_ENGINE", "")
  DB_CONFIG["HOSTNAME"] = environ.get("DB_HOSTNAME", "")
  DB_CONFIG["PORT"]     = environ.get("DB_PORT", "")
  DB_CONFIG["NAME"]     = environ.get("DB_NAME", "")
  DB_CONFIG["USERNAME"] = environ.get("DB_USERNAME", "")[1:-1]
  DB_CONFIG["PASSWORD"] = environ.get("DB_PASSWORD", "")[1:-1]

  if DB_CONFIG["ENGINE"] == "mysql":
    DB_CONFIG["DIALECT_DRIVER"] = "mysql+pymysql"
  elif DB_CONFIG["ENGINE"] == "postgresql":
    DB_CONFIG["DIALECT_DRIVER"] = "???"
  else:
    DB_CONFIG["DIALECT_DRIVER"] = "???"

  DB_CONFIG["URI"] = DB_CONFIG["DIALECT_DRIVER"] + '://' + DB_CONFIG["USERNAME"] + ':' + DB_CONFIG["PASSWORD"] + '@' + DB_CONFIG["HOSTNAME"] + ':' + DB_CONFIG["PORT"] + '/' + DB_CONFIG["NAME"]

  response += "DB_CONFIG <br/> \n"
  response += "--------- <br/> \n"
  for DB_VAR in DB_CONFIG.keys():
    response += DB_VAR + ": " + DB_CONFIG[DB_VAR] + " <br/> \n"
  response += "<br/> \n"

  response += "SQLALCHEMY CONFIG AND DB OBJECT CREATION <br/> \n"
  response += "---------------------------------------- <br/> \n"
  app.config['SQLALCHEMY_DATABASE_URI']        = DB_CONFIG["URI"]
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
  ##  DON'T DO THIS - CAUSES db.engine.execute ERROR: 'True'
  #app.config['SQLALCHEMY_ECHO'] = 'True'
  try:
    db = SQLAlchemy(app)
    response += '--> SUCCESS! <br/> \n'
  except Exception as e:
      response += '--> ERROR: ' + str(e) + ' <br/> \n'
  response += "<br/> \n"

  response += "TEST DB CONNECTION <br/> \n"
  response += "------------------ <br/> \n"
  try:
      db.engine.execute(text("SELECT 1"))
      response += '--> SUCCESS! <br/> \n'
  except Exception as e:
      response += '--> ERROR: ' + str(e) + ' <br/> \n'
  response += "<br/> \n"

  response += "LIST DB TABLES <br/> \n"
  response += "------------------ <br/> \n"
  try:
    tables = db.engine.table_names()
    response += "SUCCESS! DB TABLES:"
    response += str(tables)
  except Exception as e:
    tables = "FAILED" + str(e) + ' <br/> \n'
  response += "<br/> \n"

  return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

