'''

  1293. Shortest path in a Grid with Obstacles Elimination

'''


from collections import deque


class Solution:
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
  

def runSolution():
  solution = Solution()
  print(solution.shortestPath([
    [0,0,0],
    [1,1,0],
    [0,0,0],
    [0,1,1],
    [0,0,0]
  ], 1))
  print(solution.shortestPath([
    [0,1,1],
    [1,1,1],
    [1,0,0]
  ], 1))
  pass
runSolution()