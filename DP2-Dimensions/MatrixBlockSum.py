'''

  1314. Matrix Block Sum

  1  2  3
  4  5  6
  7  8  9
  
'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from _utils import printMatrix



class Solution:  
  def matrixBlockSum(self, mat, k):
    rows, cols = len(mat), len(mat[0])
    prefixSums = self.buildPrefixSums(mat)
    
    for row in range(1, rows + 1):
      for col in range(1, cols + 1):
        row1, row2 = max(1, row - k), min(rows, row + k)
        col1, col2 = max(1, col - k), min(cols, col + k)
        
        blanketSum = prefixSums[row2][col2]
        leftSum = prefixSums[row2][col1 - 1]
        topSum  = prefixSums[row1 - 1][col2]
        overlap = prefixSums[row1 - 1][col1 - 1]
        
        mat[row - 1][col - 1] = blanketSum - leftSum - topSum + overlap
    
    return mat
  
  def buildPrefixSums(self, mat):
    rows, cols = len(mat), len(mat[0])
    prefixSums = [[0]*(cols + 1) for _ in range(rows + 1)]
    
    for row in range(1, rows + 1):
      for col in range(1, cols + 1):
        currVal    = mat[row - 1][col - 1]
        leftPrefix = prefixSums[row][col - 1]
        topPrefix  = prefixSums[row - 1][col]
        overlap    = prefixSums[row - 1][col - 1]
        prefixSums[row][col] = currVal + leftPrefix + topPrefix - overlap
      
    return prefixSums
    
    
  
def runSolution():
  solution = Solution()
  print(solution.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
  print(solution.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2))
  pass
runSolution()