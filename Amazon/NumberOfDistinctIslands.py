'''

  694. Number of Distinct Islands

'''

from itertools import product


class Solution:
  def numDistinctIslands(self, grid):
    self.grid = grid
    self.patterns = set()
    self.rows = len(grid)
    self.cols = len(grid[0])
    
    for row, col in product(range(self.rows), range(self.cols)):
      if grid[row][col] == 1:
        pattern = []
        self.DFS(row, col, 0, 0, pattern)
        self.patterns.add(tuple(pattern))
        
    return len(list(self.patterns))
  
  def DFS(self, row, col, eRow, eCol, pattern):
    if self.validCell(row, col) == False: return
    pattern.append((eRow, eCol))
    self.grid[row][col] = 0
    
    for xDir, yDir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
      nextRow, nextCol = row + xDir, col + yDir
      nextERow, nextECol = eRow + xDir, eCol + yDir
      self.DFS(nextRow, nextCol, nextERow, nextECol, pattern)
  
  def validCell(self, row, col):
    if row < 0 or row == self.rows: return False
    if col < 0 or col == self.cols: return False
    if self.grid[row][col] == 0   : return False
    return True

            
def runSolution():
  solution = Solution()
  print(solution.numDistinctIslands(grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))
  pass
runSolution()
