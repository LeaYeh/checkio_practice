import re

def checkio(data):
  if re.match(".*[a-z]+", data) and len(data) >= 10 \
     and re.match(".*[A-Z]+", data) and re.match(".*[0-9]+", data) \
     and re.match("^[A-Za-z0-9]", data):
    return True
  else: 
    return False
  '''
  if re.match(".*[a-z]+", data): print "[a-z]+ == true"
  else: print "[a-z]+ == false"
  if re.match(".*[A-Z]+", data): print "[A-Z]+ == true"
  else: print "[A-Z]+ == false"
  if re.match(".*[0-9]+", data): print "[0-9]+ == true"
  else: print "[0-9]+ == false"
  '''
print checkio('aaaaaaaaaaaaaaaaaaaaa')
