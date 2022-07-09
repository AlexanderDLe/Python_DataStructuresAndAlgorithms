'''

  934. Shortest Bridge

'''


from collections import deque
from itertools import product


class Solution:
  dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  
  def shortestBridge(self, grid):
    self.rows, self.cols = len(grid), len(grid[0])
    queue, seen = self.init(grid)
    moves = 0
    
    while queue:
      for _ in range(len(queue)):
        row, col = queue.popleft()
        
        if grid[row][col] == 1: return moves - 1
        
        for xDir, yDir in self.dirs:
          nextRow, nextCol = row + xDir, col + yDir
          
          if self.outOfBounds(nextRow, nextCol): continue
          if (nextRow, nextCol) in seen: continue
          seen.add((nextRow, nextCol))
          
          queue.append((nextRow, nextCol))
      
      moves += 1
    
    return -1
    
    
  def init(self, grid):
    cells = deque()
    seen = set()
    
    def DFS(row, col):
      grid[row][col] = '-'
      cells.append((row, col))
      seen.add((row, col))
      
      for xDir, yDir in self.dirs:
        nextRow, nextCol = row + xDir, col + yDir
        
        if self.outOfBounds(nextRow, nextCol): continue
        if (nextRow, nextCol) in seen: continue
        if grid[nextRow][nextCol] == 0: continue
        
        DFS(nextRow, nextCol)
    
    for row, col in product(range(self.rows), range(self.cols)):
      if grid[row][col] == 1: 
        DFS(row, col)
        break
    
    return cells, seen
  
  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False
  
  
def runSolution():
  solution = Solution()
  print(solution.shortestBridge(grid = [[0,1],[1,0]]))
  print(solution.shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))
  print(solution.shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
  pass
runSolution()