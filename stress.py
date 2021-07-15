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
    #print ("%s == %s" %(key, value))
    cmd += ( "--%s %s " %( key, value ) )
  response  = ""
#  response += "<br/> \n"
  response += "cmd: " + cmd + " <br/> \n"
#  response += "<br/> \n"
#  response += str(subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8"))

  try:
    cmd_output = subprocess.check_output(
      cmd,
      stderr=subprocess.STDOUT,
      shell=True,
      #timeout=3,
      universal_newlines=True
    )
  except subprocess.CalledProcessError as exc:
    #print("Status : FAIL", exc.returncode, exc.output)
    response += "ERROR: " + str(exc.returncode) + " <br/> \n" + str(exc.output) + " <br/> \n"
  else:
    #print("Output: \n{}\n".format(output))
    response += str(cmd_output) + " <br/> \n"

  response += "<br/> \n"
  return response
