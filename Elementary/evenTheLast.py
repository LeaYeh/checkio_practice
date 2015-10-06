def checkio(array):
  """
    sums even-indexes elements and multiply at the last
  """
  sum = 0
  if len(array) == 0:
    return sum
  for i in range(0, len(array), 2):
    sum += array[i]
  return sum * array[len(array)-1]




print checkio([0, 1, 2, 3, 4, 5])
