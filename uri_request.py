def uri_request_args_html(request):
  html  = "URI REQUEST ARGS <br/> \n"
  html += "---------------- <br/> \n"
  for key, value in request.args.items():
    html += '{0}={1}<br/>'.format(key, value)
  html += "<br/> \n"
  return html
