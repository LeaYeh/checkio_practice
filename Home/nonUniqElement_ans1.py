
def checkio(data):
  newlist = []
  for num in data:
    if data.count(num) > 1:
      newlist.append(num)
  return newlist


print checkio([1, 2, 3, 2, 5, 7, 2, 1, 4, 3])
