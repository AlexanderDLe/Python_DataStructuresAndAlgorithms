'''

  64. Minimum Path Sum

'''

from itertools import product


class Solution:  
  def minPathSum(self, grid):
    rows, cols = len(grid), len(grid[0])
    
    for col in range(cols - 2, -1, -1):
      grid[rows - 1][col] += grid[rows - 1][col + 1]
    
    for row in range(rows - 2, -1, -1):
      grid[row][cols - 1] += grid[row + 1][cols - 1]
      
    for row in range(rows - 2, -1, -1):
      for col in range(cols - 2, -1, -1):
        grid[row][col] += min(grid[row + 1][col], grid[row][col + 1])
      
    return grid[0][0]
    
  
def runSolution():
  solution = Solution()
  print(solution.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
  print(solution.minPathSum(grid = [[1,2,3],[4,5,6]]))
  pass
runSolution()