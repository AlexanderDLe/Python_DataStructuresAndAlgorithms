'''

  286. Walls and Gates

'''

from collections import deque
from itertools import product


class Solution:
  INF = 2147483647
  
  def wallsAndGates(self, rooms):
    self.rows, self.cols = len(rooms), len(rooms[0])
    queue = deque([(R, C) for R, C in product(range(self.rows), range(self.cols)) if rooms[R][C] == 0])
    distance = 0
    
    while queue:
      distance += 1
      
      for _ in range(len(queue)):
        row, col = queue.popleft()
        
        for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
          nextRow, nextCol = row + xDir, col + yDir
          
          if self.invalid(nextRow, nextCol, rooms): continue
          queue.append((nextRow, nextCol))
          rooms[nextRow][nextCol] = distance

  
  def invalid(self, row, col, rooms):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if rooms[row][col] != self.INF: return True
    return False

  
def runSolution():
  solution = Solution()
  
  print(solution.wallsAndGates(
    rooms = [
      [2147483647,          -1,           0,  2147483647],
      [2147483647,  2147483647,  2147483647,          -1],
      [2147483647,          -1,  2147483647,          -1],
      [         0,          -1,  2147483647,  2147483647]]))
  pass
runSolution()