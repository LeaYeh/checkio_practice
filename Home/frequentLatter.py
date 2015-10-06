
def checkio(data):
  count = {}
  maxVal = -1
  maxKey = '{'
  data = data.lower()
  for i in range(len(data)):
    count[data[i]] = 0
  for i in range(len(data)):
    if data[i].isalpha():
      count[data[i]] += 1
  
  for key,val in count.items():
    if val > maxVal:
      maxKey = key
      maxVal = val
    elif val == maxVal and key < maxKey:
      maxKey = key
      maxVal = val
      
  return maxKey
      
  #return max(count, key=count.get)



print checkio("ACAaococo!!c!!");



