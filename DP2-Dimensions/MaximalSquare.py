'''

  64. Minimum Path Sum

'''

from itertools import product


class Solution:  
  def maximalSquare(self, matrix):
    rows, cols = len(matrix), len(matrix[0])
    DP = [[0]*(cols + 1) for _ in range(rows + 1)]
    res = 0
    
    for row, col in product(range(rows), range(cols)):
      if matrix[row][col] == '0': continue
      
      topLeft = DP[row][col]
      top  = DP[row][col + 1]
      left = DP[row + 1][col]
      
      DP[row + 1][col + 1] = min(topLeft, top, left) + 1
      res = max(res, DP[row + 1][col + 1])
    
    return res * res
    
  
def runSolution():
  solution = Solution()
  print(solution.maximalSquare([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
  ]))
  print(solution.maximalSquare([
    ["0","1"],
    ["1","0"]
  ]))
  pass
runSolution()