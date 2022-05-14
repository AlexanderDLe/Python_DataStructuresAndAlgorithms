'''

  1254. Number of Closed Islands

'''


from itertools import product


class Solution:
  def closedIsland(self, grid):
    self.rows, self.cols = len(grid), len(grid[0])
    self.grid = grid
    count = 0
    
    for row, col in product(range(self.rows), range(self.cols)):
      if grid[row][col] == 0 and self.checkAndSinkIsland(row, col):
        count += 1
    
    return count
  
  def checkAndSinkIsland(self, row, col):
    if self.outOfBounds(row, col): return False
    if self.grid[row][col] == 1: return True
    
    self.grid[row][col] = 1
    
    isClosed = True
    for xDir, yDir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
      nextRow, nextCol = row + xDir, col + yDir
      if self.checkAndSinkIsland(nextRow, nextCol) == False: isClosed = False
      
    return isClosed    
  
  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False
  

  
def runSolution():
  solution = Solution()
  
  print(solution.closedIsland(grid = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
  ]))
  print(solution.closedIsland(grid = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0]
  ]))
  pass
runSolution()