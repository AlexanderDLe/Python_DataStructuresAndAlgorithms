'''

  1091. Shortest Path in Binary Matrix

'''

def isValid(n, row, col, grid):
  if row < 0 or row == n: return False
  if col < 0 or col == n: return False
  if grid[row][col] == 1: return False
  return True

def shortestPathInBinaryMatrix(grid):
  if grid[0][0] == 1: return -1

  dirs = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1 ],          [0,  1],
    [1,  -1], [ 1, 0], [1,  1]
  ]
  n = len(grid)
  queue = [(0, 0)]
  seen  = {(0, 0)}

  distance = 1
  count = 1
  
  while queue:
    while count:
      row, col = queue.pop(0)
      if row == n - 1 and col == n - 1: return distance
      
      for x, y in dirs:
        nextRow = row + x
        nextCol = col + y

        if isValid(n, nextRow, nextCol, grid) == False: continue
        if (nextRow, nextCol) in seen: continue
        seen.add((nextRow, nextCol))
        queue.append((nextRow, nextCol))

      count -= 1
    distance += 1
    count = len(queue)

  return -1

print(shortestPathInBinaryMatrix([
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 0],
]))

print(shortestPathInBinaryMatrix([
  [0,1],
  [1,0]
]))