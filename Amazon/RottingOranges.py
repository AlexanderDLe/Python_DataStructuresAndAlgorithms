'''

  994. Rotting Oranges

  Note: Remember to subtract 1 to the end minute result if valid.
  
'''

from itertools import product


class Solution:
  def orangesRotting(self, grid):
    self.rows = len(grid)
    self.cols = len(grid[0])
    queue, totalOranges = self.initOrangesAndRotting(grid)
    return self.getMinutesUntilAllRot(queue, grid, totalOranges)
  
  def getMinutesUntilAllRot(self, queue, grid, totalOranges):
    freshOranges = totalOranges - len(queue)
    minutes = 0
    
    while queue and freshOranges:
      minutes += 1
      
      for _ in range(len(queue)):
        row, col = queue.pop(0)
        
        for dirX, dirY in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
          nextRow = row + dirX
          nextCol = col + dirY
          
          if self.freshOrange(nextRow, nextCol, grid) == False: continue
          grid[nextRow][nextCol] = 2
          freshOranges -= 1
          queue.append((nextRow, nextCol))    

    if freshOranges == 0: return minutes
    else: return -1
  
  def freshOrange(self, row, col, grid):
    if row < 0 or row == self.rows: return False
    if col < 0 or col == self.cols: return False
    if grid[row][col] != 1        : return False
    return True
  
  def initOrangesAndRotting(self, grid):
    queue = []
    totalOranges = 0
    
    for row, col in product(range(self.rows), range(self.cols)):
      if grid[row][col] == 2: queue.append((row, col))
      if grid[row][col] != 0: totalOranges += 1
    
    return (queue, totalOranges)
  
  

def runSolution():
  solution = Solution()
  print(solution.orangesRotting([
    [2,1,1],
    [1,1,0],
    [0,1,1]
  ]))
  print(solution.orangesRotting([
    [2,1,1],
    [0,1,1],
    [1,0,1]
  ]))
  print(solution.orangesRotting([
    [0,2],
  ]))
  print(solution.orangesRotting([
    [1,2],
  ]))
  print(solution.orangesRotting([
    [0],
  ]))
  print(solution.orangesRotting([
    [1],
  ]))
  
runSolution()