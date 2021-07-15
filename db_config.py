def db_config_html(environ):
  
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

  html = "DB_CONFIG <br/> \n"
  html += "--------- <br/> \n"
  for DB_VAR in DB_CONFIG.keys():
    html += DB_VAR + ": " + DB_CONFIG[DB_VAR] + " <br/> \n"
  html += "<br/> \n"
  return html
