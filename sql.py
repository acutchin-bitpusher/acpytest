def sqlalchemy_db_test_html(environ,app):

  from flask_sqlalchemy import SQLAlchemy
  from sqlalchemy.sql import text
  import pymysql

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

  html = ""
  html += "SQLALCHEMY CONFIG AND DB OBJECT CREATION <br/> \n"
  html += "---------------------------------------- <br/> \n"
  app.config['SQLALCHEMY_DATABASE_URI']        = DB_CONFIG["URI"]
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
  ##  DON'T DO THIS - CAUSES db.engine.execute ERROR: 'True'
  #app.config['SQLALCHEMY_ECHO'] = 'True'
  try:
    db = SQLAlchemy(app)
    html += '--> SUCCESS! <br/> \n'
  except Exception as e:
      html += '--> ERROR: ' + str(e) + ' <br/> \n'
  html += "<br/> \n"

  html += "TEST DB CONNECTION <br/> \n"
  html += "------------------ <br/> \n"
  try:
      db.engine.execute(text("SELECT 1"))
      html += '--> SUCCESS! <br/> \n'
  except Exception as e:
      html += '--> ERROR: ' + str(e) + ' <br/> \n'
  html += "<br/> \n"

  html += "LIST DB TABLES <br/> \n"
  html += "------------------ <br/> \n"
  try:
    tables = db.engine.table_names()
    html += "SUCCESS! DB TABLES:"
    html += str(tables)
  except Exception as e:
    tables = "FAILED" + str(e) + ' <br/> \n'
  html += "<br/> \n"

  return html
