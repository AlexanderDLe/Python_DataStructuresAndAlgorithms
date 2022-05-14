'''

  1905. Count Sub Islands

'''

from collections import deque
from itertools import product

class Solution:
  def maxDistance(self, grid):
    self.rows, self.cols = len(grid), len(grid[0])
    self.grid = grid
    queue = self.getLandmass(grid)
    
    n = len(queue)
    if n == self.rows * self.cols or n == 0: return -1
    
    maxDistance = self.calculateDistance(queue)
    return maxDistance
    
  def calculateDistance(self, queue):
    distance = 0

    while queue:
      for _ in range(len(queue)):
        row, col = queue.popleft()
        
        for xDir, yDir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
          nextRow, nextCol = row + xDir, col + yDir
          if self.invalidCell(nextRow, nextCol): continue
          self.grid[nextRow][nextCol] = 1
          queue.append((nextRow, nextCol))
        
      distance += 1
    
    return distance - 1
    
  def invalidCell(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if self.grid[row][col] != 0   : return True
    return False

  def getLandmass(self, grid):
    queue = deque([(row, col) for row, col in product(range(self.rows), range(self.cols)) if grid[row][col] == 1])
    return queue
  
def runSolution():
  solution = Solution()
  print(solution.maxDistance(grid = [
    [1,0,1],
    [0,0,0],
    [1,0,1]
  ]))
  print(solution.maxDistance(grid = [
    [1,0,0],
    [0,0,0],
    [0,0,0]
  ]))
  print(solution.maxDistance([
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
  ]))
  pass
runSolution()