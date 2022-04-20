'''

  827. Making a Large Island

  1. Encode each island
  2. Map each encoding to island size

  Considerations/Edge Cases:
  1. Entire grid is 1s (set maxSize on first scan)
  2. When attaching a bridge to landmasses, include bridge value to size
'''

from base64 import encode
from itertools import product

def largestIslandRef(grid):
  def outOfBounds(row, col, n):
    if row < 0 or row >= n: return True
    if col < 0 or col >= n: return True
    return False

  def validLand(row, col, n, grid):
    if outOfBounds(row, col, n): return False
    if grid[row][col] != 1     : return False
    return True

  def DFSEncode(row, col, code, grid, n):
    if validLand(row, col, n, grid) == False: return 0
    grid[row][col] = code

    sum = 1
    for x, y in dirs:
      sum += DFSEncode(row + x, col + y, code, grid, n)
    return sum


  n = len(grid)
  encodeToSize = {}
  maxSize = 0

  for row in range(n):
    for col in range(n):
      if grid[row][col] == 1: 
        code = f'{row}-{col}'
        size = DFSEncode(row, col, code, grid, n)
        encodeToSize[code] = size
        maxSize = max(maxSize, size)

  for row in range(n):
    for col in range(n):
      if grid[row][col] == 0:
        seen = set()
        currSize = 0

        for x, y in dirs:
          if outOfBounds(row + x, col + y, n): continue
          code = grid[row + x][col + y]
          if code in encodeToSize and code not in seen:
            currSize += encodeToSize[code]
            seen.add(code)

        maxSize = max(maxSize, currSize + 1)


  return maxSize


def largestIsland(grid):
  def outOfBounds(row, col, n):
    if row < 0 or row >= n: return True
    if col < 0 or col >= n: return True
    return False


  def encodeDFS(row, col, code, n):
    if outOfBounds(row, col, n): return 0
    if grid[row][col] != 1     : return 0
    grid[row][col] = code

    size = 1
    for x, y in dirs:
      size += encodeDFS(row + x, col + y, code, n)
    return size


  dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  n = len(grid)
  codeToSize = {}
  maxSize = 0

  for row, col in product(range(n), range(n)):
    if grid[row][col] == 1:
      code = f'{row}-{col}'
      size = encodeDFS(row, col, code, n)
      codeToSize[code] = size
      maxSize = max(maxSize, size)

  for row, col in product(range(n), range(n)):
    if grid[row][col] == 0:
      currSize = 0
      seen = set()

      for x, y in dirs:
        code = f'{row + x}-{col + y}'
        if outOfBounds(row + x, col + y, n): continue
        if code not in codeToSize or code in seen: continue
        currSize += codeToSize[code]
        seen.add(code)

      maxSize = max(maxSize, currSize + 1)

  print(codeToSize)
  return maxSize



print(largestIsland([
  [1,0,1,1],
  [0,1,0,0],
  [0,1,0,1],
  [0,1,0,1]
]))

# print(largestIsland([
#   [1,0],
#   [0,1]
# ]))
# print(largestIsland([
#   [1,1],
#   [1,1]
# ]))