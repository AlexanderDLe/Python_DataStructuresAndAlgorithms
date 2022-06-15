'''

  1240. Tiling a Rectangle with the Fewest Squares

  Two strategies are presented here: backtracking and A* search. They are both based on the following principle:

  Place squares in the order of bottom to top and left to right; 
  all possible tilings can form such unique ordering to avoid searching redundant cases.
  
  
'''

import heapq

class SolutionRef:
  def tilingRectangle(self, rows, cols):
    self.best = cols * rows    

    def DFS(height, moves):
      print(height, moves)
      
      # Checks if area is completed
      if all(h == rows for h in height):
        self.best = min(self.best, moves)
        return
      
      # No need to continue if past curr moves
      if moves >= self.best:
        return
      
      # Get lowest height in array and create index range.
      minHeight = min(height)
      L = height.index(minHeight)
      R = L + 1
      
      # Expand R pointer while height matches minHeight
      while R < cols and height[R] == minHeight:
        R += 1
        
      # Calculate maximum allowed length for a square
      maxLength = min(R - L, rows - minHeight)
        
      # Consider all cases
      for squareLength in range(min(maxLength), 0, -1):
        newHeights = height[:]
        
        # Place squares in new array
        for j in range(squareLength):
          newHeights[L + j] += squareLength
          
        # DFS
        DFS(newHeights, moves + 1) 

    DFS([0] * cols, 0)
    return self.best
  
class Solution:
  def tilingRectangle(self, rows, cols):
    pass
  

def runSolution():
  solution = Solution()
  print(solution.tilingRectangle(rows = 2, cols = 3))
  # print(solution.tilingRectangle(n = 5, m = 8))
  # print(solution.tilingRectangle(n = 11, m = 13))
  pass
runSolution()