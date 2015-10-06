
def count_neighbours(data, row, col):
  count = 0
  bound_col = len(data[0])
  bound_row = len(data)
  for i in range(-1, 2):
    for j in range(-1, 2):
      if not (i ==j == 0) and i+row > -1 and i+row < bound_row \
        and j+col > -1 and j+col < bound_col and data[i+row][j+col]:
        count += 1;
     
  return count  
print count_neighbours(((1,0,1,0,1),
     (0,1,0,1,0),
     (1,0,1,0,1),
     (0,1,0,1,0),
     (1,0,1,0,1),
     (0,1,0,1,0),), 5, 4)
