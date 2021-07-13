def env_var_list_html(environ):
  #from os import environ
  html = "ENV VARS <br/> \n"
  html += "-------- <br/> \n"
  for k, v in sorted(environ.items()):
    html += ( str(k) + ': ' + str(v) + " <br/> \n" )
  html += "<br/> \n"
  return html
