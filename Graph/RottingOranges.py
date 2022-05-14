'''

  994. Rotting Oranges

'''
from collections import deque
from itertools import product


class Solution:
  def orangesRotting(self, grid):
    self.rows, self.cols = len(grid), len(grid[0])
    rottingOJs, totalCount = self.collectRottingOJs(grid)
    rotCount = len(rottingOJs)
    days = 0
    
    while rottingOJs and rotCount < totalCount:
      days += 1
      for _ in range(len(rottingOJs)):
        row, col = rottingOJs.popleft()
        
        for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
          nextRow, nextCol = row + xDir, col + yDir
          
          if self.invalid(nextRow, nextCol, grid): continue
          rottingOJs.append((nextRow, nextCol))
          grid[nextRow][nextCol] = 2
          rotCount += 1
    
    print(rotCount, totalCount)
    return days if rotCount == totalCount else -1
  
  
  
  def invalid(self, row, col, grid):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if grid[row][col] != 1: return True
    return False


  def collectRottingOJs(self, grid):
    rottingOJs = deque()
    totalCount = 0
    for row, col in product(range(self.rows), range(self.cols)):
      if grid[row][col] == 2: rottingOJs.append((row, col))
      if grid[row][col] != 0: totalCount += 1
    return rottingOJs, totalCount
  
  
  
  
  
  
  
def runSolution():
  solution = Solution()
  
  print(solution.orangesRotting(grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]]))
  print(solution.orangesRotting(grid = [
    [2,1,1],
    [0,1,1],
    [1,0,1]]))
  pass
runSolution()