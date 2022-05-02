'''

  74. Search a 2D Matrix

'''

class Solution:
  def searchMatrix(self, matrix, target):
    self.rows, self.cols = len(matrix), len(matrix[0])
    L, R = 0, self.rows * self.cols - 1

    while L <= R:
      M = L + (R - L)//2
      row, col = self.numToCell(M)
      val = matrix[row][col]
      
      if val == target: return True
      if val >  target: R = M - 1
      else            : L = M + 1
    
    return False
  
  def numToCell(self, num):
    row = num // self.cols
    col = num %  self.cols
    return (row, col)
  
def runSolution():
  solution = Solution()
  print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
  print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
  pass
runSolution()
