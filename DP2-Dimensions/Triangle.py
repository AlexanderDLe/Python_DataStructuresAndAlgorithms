'''

  120. Triangle

'''

class Solution:  
  def minimumTotal(self, triangle):
    rows = len(triangle)
    
    for row in range(1, rows):
      cols = len(triangle[row])
      
      for col in range(cols):
        prev = triangle[row - 1][col - 1] if col > 0 else float('inf')
        curr = triangle[row - 1][col] if col < cols - 1 else float('inf')
        triangle[row][col] += min(prev, curr)
    
    return min(triangle[-1])
    
  
def runSolution():
  solution = Solution()
  print(solution.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
  print(solution.minimumTotal(triangle = [[-10]]))
  pass
runSolution()