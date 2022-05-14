'''

  1905. Count Sub Islands

'''


from itertools import product


class Solution:
  def countSubIslands(self, grid1, grid2):
    self.rows, self.cols = len(grid1), len(grid1[0])
    self.grid1, self.grid2 = grid1, grid2
    subIslands = 0
    
    for row, col in product(range(self.rows), range(self.cols)):
      if grid1[row][col] == 1 and grid2[row][col] == 1:
        if self.processSubIsland(row, col): subIslands += 1
        
    return subIslands
    
  def processSubIsland(self, R, C):
    isSubIsland = True
    
    def DFS(row, col):
      nonlocal isSubIsland
      if self.outOfBounds(row, col): return
      if self.grid2[row][col] == 0 : return
      if self.grid1[row][col] == 0 and self.grid2[row][col] == 1:
        isSubIsland = False
        
      self.grid1[row][col] = 0
      self.grid2[row][col] = 0
        
      for xDir, yDir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nextRow, nextCol = row + xDir, col + yDir
        DFS(nextRow, nextCol)
      
    DFS(R, C)
    return isSubIsland
    

  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False
    
  
def runSolution():
  solution = Solution()
  
  print(solution.countSubIslands(
    grid1 = [
      [1,1,1,0,0],
      [0,1,1,1,1],
      [0,0,0,0,0],
      [1,0,0,0,0],
      [1,1,0,1,1]], 
    grid2 = [
      [1,1,1,0,0],
      [0,0,1,1,1],
      [0,1,0,0,0],
      [1,0,1,1,0],
      [0,1,0,1,0]
  ]))
  print(solution.countSubIslands(
    grid1 = [
      [1,0,1,0,1],
      [1,1,1,1,1],
      [0,0,0,0,0],
      [1,1,1,1,1],
      [1,0,1,0,1]], 
    grid2 = [
      [0,0,0,0,0],
      [1,1,1,1,1],
      [0,1,0,1,0],
      [0,1,0,1,0],
      [1,0,0,0,1]
  ]))
  pass
runSolution()