
def checkio(data):
  return [n for n in data if data.count(n) > 1]


print checkio([1, 2, 3, 2, 5, 7, 2, 1, 4, 3])
