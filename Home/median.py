def checkio(data):
  data.sort()
  if len(data)%2:
    return data[int(len(data)/2)]
  else: 
    return (data[int(len(data)/2)-1]+data[int(len(data)/2)])/2

if __name__ == '__main__':
  print(checkio([3, 6, 20, 99, 10, 15]))
