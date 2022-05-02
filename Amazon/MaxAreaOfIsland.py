'''

  695. Max Area of Island

'''


from itertools import product


class Solution:
  def maxAreaOfIsland(self, grid):
    self.size = 0
    self.grid = grid
    self.rows = len(grid)
    self.cols = len(grid[0])
    
    for row, col in product(range(self.rows), range(self.cols)):
      if grid[row][col] == 1: self.sinkAndCount(row, col)
      
    return self.size    
    
  def sinkAndCount(self, row, col):
    currSize = 0
    
    def DFS(R, C):
      nonlocal currSize
      if self.isValidLand(R, C) == False: return
      currSize += 1
      self.grid[R][C] = 0
      
      for xDir, yDir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nextRow = R + xDir
        nextCol = C + yDir        
        DFS(nextRow, nextCol)
        
    DFS(row, col)
    self.size = max(self.size, currSize)

  def isValidLand(self, row, col):
    if row < 0 or row == self.rows: return False
    if col < 0 or col == self.cols: return False
    if self.grid[row][col] == 0   : return False
    return True
  
  
def runSolution():
  solution = Solution()
  print(solution.maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
  ]))
  pass
runSolution()
