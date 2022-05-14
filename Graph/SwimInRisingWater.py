'''

  778. Swim in Rising Water

'''

from collections import defaultdict, deque
import heapq


class Solution:
  def swimInWater(self, grid):
    self.rows, self.cols = len(grid), len(grid[0])
    seen = set([0, 0])
    minHeap = [(grid[0][0], 0, 0)] # (height, row, col)
    time = 0
    
    while minHeap:
      height, row, col = heapq.heappop(minHeap)
      time = max(time, height)
      
      if row == self.rows - 1 and col == self.cols - 1: break
      
      for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nextRow, nextCol = row + xDir, col + yDir
        
        if self.outOfBounds(nextRow, nextCol): continue
        if (nextRow, nextCol) in seen: continue
        
        seen.add((nextRow, nextCol))
        heapq.heappush(minHeap, (grid[nextRow][nextCol], nextRow, nextCol))
    
    return time
  
  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False

  
def runSolution():
  solution = Solution()
  
  print(solution.swimInWater(
    grid = [
      [0,2],[1,3]]))
  print(solution.swimInWater(
    grid = [
      [0 ,  1,  2,  3,  4],
      [24, 23, 22, 21,  5],
      [12, 13, 14, 15, 16],
      [11, 17, 18, 19, 20],
      [10,  9,  8,  7,  6]
    ]))
  pass
runSolution()