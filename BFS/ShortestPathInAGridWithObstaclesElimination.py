'''

  1293. Shortest path in a Grid with Obstacles Elimination

'''

from collections import deque

class SolutionRef:
  def shortestPath(self, grid, k):
    self.rows = len(grid)
    self.cols = len(grid[0])
    
    seen = set([(0, 0, k)])
    queue = deque([(0, 0, k)])
    moves = 0
    
    while queue:
      for _ in range(len(queue)):
        row, col, breaks = queue.popleft()
        
        if row == self.rows - 1 and col == self.cols - 1: return moves
         
        for nextRow, nextCol in [[row-1, col], [row, col + 1], [row + 1, col], [row, col -1 ]]:
          if self.invalidCell(nextRow, nextCol, grid, breaks): continue
          
          nextBreaks = breaks if grid[nextRow][nextCol] == 0 else breaks - 1
          if (nextRow, nextCol, nextBreaks) in seen: continue
          seen.add((nextRow, nextCol, nextBreaks))
          queue.append((nextRow, nextCol, nextBreaks))
          
      moves += 1
    
    return -1
  
  def invalidCell(self, row, col, grid, breaks):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if grid[row][col] == 1 and breaks <= 0: return True
    
    return False



class Solution:
  def shortestPath(self, grid, k):
    self.rows, self.cols = len(grid), len(grid[0])
    seen, self.grid = set(), grid
    
    if grid[0][0] == 1: k -= 1
    if k < 0: return -1
    
    queue = deque([(0, 0, k)])
    moves = 0
    
    while queue:
      for _ in range(len(queue)):
        row, col, breaksLeft = queue.popleft()
        print(moves)
        
        if row == self.rows - 1 and col == self.cols - 1: return moves
        
        for xDir, yDir in [(0,1), (0,-1), (1,0), (-1,0)]:
          nextRow, nextCol = row + xDir, col + yDir
          
          if self.invalid(nextRow, nextCol, breaksLeft): continue
          
          nextBreaks = breaksLeft - 1 if grid[nextRow][nextCol] == 1 else breaksLeft
          if (nextRow, nextCol, nextBreaks) in seen: continue
          
          seen.add((nextRow, nextCol, nextBreaks))
          queue.append((nextRow, nextCol, nextBreaks))
        
      moves += 1
    
    return -1

  def invalid(self, row, col, breaksLeft):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if self.grid[row][col] == 1 and breaksLeft == 0: return True
    return False

def runSolution():
  solution = Solution()
  print(solution.shortestPath([
    [0,0,0],
    [1,1,0],
    [0,0,0],
    [0,1,1],
    [0,0,0]
  ], 1))
  # print(solution.shortestPath([
  #   [0,1,1],
  #   [1,1,1],
  #   [1,0,0]
  # ], 1))
  pass
runSolution()