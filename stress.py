##  FIXED ARGS
#def stress():
#  import subprocess
#  response  = ""
#  response += "<br/> \n"
#  response += str(subprocess.Popen('stress -c 10 -t 1', shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8"))
#  response += "<br/> \n"
#  return response

def stress(**kwargs):
  import subprocess
  cmd = '/usr/bin/stress '
  for key, value in kwargs.items():
    cmd += ( "--%s %s " %( key, value ) )
  response  = ""
  response += "cmd: " + cmd + " <br/> \n"

  try:
    cmd_output = subprocess.check_output(
      cmd,
      stderr=subprocess.STDOUT,
      shell=True,
      universal_newlines=True
    )
  except subprocess.CalledProcessError as exc:
    response += "ERROR: " + str(exc.returncode) + " <br/> \n" + str(exc.output) + " <br/> \n"
  else:
    response += str(cmd_output) + " <br/> \n"

  response += "<br/> \n"
  return response
