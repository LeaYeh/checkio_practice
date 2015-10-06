
def checkio(arr):
  result = []
  dup = [0]*len(arr)
  for i in range(len(arr)):
    if dup[i] == 0: 
      if i < len(arr):
        for j in range(i+1, len(arr)):
          if arr[i] == arr[j]:
            dup[i] = dup[j] = 1
  for i in range(len(dup)):
    if dup[i]:
      result.append(arr[i])
  return result

print checkio([1, 2, 3, 1, 4, 5, 1, 2, 2])




  
