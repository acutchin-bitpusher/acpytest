from flask import Flask
from os import environ
import json
#from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
#import sqlalchemy

app = Flask(__name__)

#DB_VARS = [
#  "ENGINE",
#  "HOSTNAME",
#  "PORT",
#  "NAME",
##  "CREDENTIALS",
#  "USERNAME",
#  "PASSWORD",
#]
#
#DB_CONFIG = {}
#for DB_VAR in DB_VARS:
#  DB_CONFIG[DB_VAR] = environ.get( ( "DB_" + DB_VAR ), "##ENV_VAR_ABSENT##" )
#DB_CONFIG["DB_PASSWORD"] = DB_CONFIG["DB_PASSWORD"][1:-1]
#DB_CONFIG["DB_USERNAME"] = DB_CONFIG["DB_USERNAME"][1:-1]

DB_CONFIG = {}
DB_CONFIG["ENGINE"]   = environ.get("DB_ENGINE")
DB_CONFIG["HOSTNAME"] = environ.get("DB_HOSTNAME")
DB_CONFIG["PORT"]     = environ.get("DB_PORT")
DB_CONFIG["NAME"]     = environ.get("DB_NAME")
DB_CONFIG["USERNAME"] = environ.get("DB_USERNAME")[1:-1]
DB_CONFIG["PASSWORD"] = environ.get("DB_PASSWORD")[1:-1]
DB_URI = DB_CONFIG["ENGINE"] + '://' + DB_CONFIG["USERNAME"] + ':' + DB_CONFIG["PASSWORD"] + '@' + DB_CONFIG["HOSTNAME"] + ':' + DB_CONFIG["PORT"] + '/' + DB_CONFIG["NAME"]

#db_username = json.loads(environ["DB_CREDENTIALS"])["username"]
#db_password = json.loads(environ["DB_CREDENTIALS"])["password"]
#db_hostname = json.loads(environ["DB_HOSTNAME"])
#db_port     = json.loads(environ["DB_PORT"])
#db_name     = json.loads(environ["DB_NAME"])

#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{master username}:{db password}@{endpoint}/{db instance name}'
#application.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
#db = salalchemy(app)

@app.route("/")
def hello():
  #response.content_type = "text/plain"
  response = ""
  response += "Hello from actest! <br/> "
  response += "<br/>"
  response += "DB_CONFIG: <br/>"
  for DB_VAR in DB_CONFIG.keys():
    response += DB_VAR + ": " + DB_CONFIG[DB_VAR] + " <br/>"
  response += "<br/>"
  response += "DB URI: " + DB_URI + " <br/>"
  response += "<br/>"
  response += "ENVIRONMENT: <br/>"
  for k, v in sorted(environ.items()):
    response += ( str(k) + ': ' + str(v) + " <br/>" )
  return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

