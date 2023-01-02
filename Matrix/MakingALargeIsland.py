'''

  827. Making a Large Island

  1. Encode each island
  2. Map each encoding to island size

  Considerations/Edge Cases:
  1. Entire grid is 1s (set maxSize on first scan)
  2. When attaching a bridge to landmasses, include bridge value to size
'''

from base64 import encode
from collections import defaultdict
from itertools import product



class SolutionRef:
  def largestIsland(self, grid):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
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
  
  
class Solution1:
  def largestIsland(self, grid):
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
  
  
class Solution:
  
  '''
  
    Time Complexity
    O(n) Iterate through all cells
    
    Space Complexity
    O(n) Dict to hold island sizes
  
  '''
  
  
  dirs = [(0,1),(1,0),(-1,0),(0,-1)]
  
  def largestIsland(self, grid):
    self.rows, self.cols, self.grid = len(grid), len(grid[0]), grid
    self.sizeMap = defaultdict(int)
    self.largest = 0
    
    self.encodeIslands(grid)
    self.makeIslands(grid)
    
    return self.largest
    
  
  def makeIslands(self, grid):
    for row, col in product(range(self.rows), range(self.cols)):
      if grid[row][col] != 0: continue
      
      seen = set()
      size = 1
      
      for xDir, yDir in self.dirs:
        adjRow, adjCol = row + xDir, col + yDir
        if self.outOfBounds(adjRow, adjCol) or grid[adjRow][adjCol] == 0: continue
        
        code = grid[adjRow][adjCol]
        if code in seen: continue
        
        seen.add(code)
        size += self.sizeMap[code]

      self.largest = max(self.largest, size)
  
    
  def encodeIslands(self, grid):
    currCode = 2
    
    def encodeDFS(row, col, code):
      if self.outOfBounds(row, col): return
      if grid[row][col] != 1: return
      
      self.sizeMap[code] += 1
      grid[row][col] = code
      
      for xDir, yDir in self.dirs:
        nextRow, nextCol = row + xDir, col + yDir
        encodeDFS(nextRow, nextCol, code)
      
    
    for row, col in product(range(self.rows), range(self.cols)):
      if grid[row][col] == 1: 
        encodeDFS(row, col, currCode)
        self.largest = max(self.largest, self.sizeMap[currCode])
        currCode += 1
        
  
  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False
  
  
    
    
  
def runSolution():
  solution = SolutionRef()
  print(solution.largestIsland([
    [1,0,1,1],
    [0,1,0,0],
    [0,1,0,1],
    [0,1,0,1]
  ]))
  print(solution.largestIsland([
    [1,0],
    [0,1]
  ]))
  print(solution.largestIsland([
    [1,1],
    [1,1]
  ]))
  print(solution.largestIsland([
    [1,1],
    [1,0]
  ]))
  pass
runSolution()
