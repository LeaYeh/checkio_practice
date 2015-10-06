def checkio(data):
  lines = [ [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)] ]
  cross = [ [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)] ]
  for i in lines:
    countx = 0
    counto = 0
    for j in i:
      if data[j[0]][j[1]] == 'X':
        countx += 1
      elif data[j[0]][j[1]] == 'O':
        counto += 1 
    if countx == 3:
      return 'X'
    elif counto == 3:
      return 'O'
    countx = 0
    counto = 0
    for j in i:
      if data[j[1]][j[0]] == 'X':
        countx += 1
      elif data[j[1]][j[0]] == 'O':
        counto += 1
  
    if countx == 3:
      return 'X'
    elif counto == 3:
      return 'O'
  for i in cross:
    countx = 0
    counto = 0
    for j in i:
      if data[j[0]][j[1]] == 'X':
        countx += 1
      elif data[j[0]][j[1]] == 'O':
        counto += 1
    if countx == 3:
      return 'X'
    elif counto == 3:
      return 'O'  
  
  return 'D'




print checkio([
    "X.O",
    "XX.",
    "XOO"])
