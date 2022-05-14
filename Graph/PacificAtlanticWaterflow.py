'''

  417. Pacific Atlantic Water Flow

'''


from collections import deque
from itertools import product


class Solution:
  def pacificAtlantic(self, heights):
    self.rows, self.cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()
    
    self.initializeSets(atlantic, pacific)
    self.populateSets(heights, pacific)
    self.populateSets(heights, atlantic)
    
    result = []
    for row, col in list(pacific):
      if (row, col) in atlantic: result.append((row, col))
    
    return result

  def populateSets(self, heights, set):
    queue = deque(list(set))
    
    while queue:
      row, col = queue.popleft()
      currHeight = heights[row][col]
      
      for xDir, yDir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nextRow, nextCol = row + xDir, col + yDir
        
        if self.outOfBounds(nextRow, nextCol): continue
        if (nextRow, nextCol) in set: continue
        
        nextHeight = heights[nextRow][nextCol]
        if currHeight > nextHeight: continue
        
        set.add((nextRow, nextCol))
        queue.append((nextRow, nextCol))
        
  
  def initializeSets(self, atlantic, pacific):
    for row in range(self.rows):
      pacific.add((row, 0))
      atlantic.add((row, self.cols - 1))

    for col in range(self.cols):
      pacific.add((0, col))
      atlantic.add((self.rows - 1, col))
      
  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False
    
    
  
def runSolution():
  solution = Solution()
  
  print(solution.pacificAtlantic(
    heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
  ]))
  print(solution.pacificAtlantic(
    heights = [
      [2,1],
      [1,2]
  ]))
  pass
runSolution()