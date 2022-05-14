'''

  62. Unique Paths

'''

from itertools import product


class Solution:
  def uniquePaths(self, m, n):
    matrix = [[0]*n for _ in range(m)]
    
    for i in range(m):
      matrix[i][0] = 1
    
    for i in range(n):
      matrix[0][i] = 1
      
    for row, col in product(range(1, m), range(1, n)):
      matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]
    
    return matrix[m - 1][n - 1]
  
def runSolution():
  solution = Solution()
  print(solution.uniquePaths(m = 3, n = 7))
  print(solution.uniquePaths(m = 3, n = 2))
  pass
runSolution()