'''

  931. Minimum Falling Path Sum

'''

class Solution:  
  def minFallingPathSum(self, matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    for row in range(1, rows):
      for col in range(cols):
        prev = matrix[row - 1][col - 1] if col > 0 else float('inf')
        curr = matrix[row - 1][col]
        next = matrix[row - 1][col + 1] if col < cols - 1 else float('inf')
        matrix[row][col] += min(prev, curr, next)
    
    return min(matrix[-1])
    
  
def runSolution():
  solution = Solution()
  print(solution.minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))
  print(solution.minFallingPathSum(matrix = [[-19,57],[-40,-5]]))
  pass
runSolution()