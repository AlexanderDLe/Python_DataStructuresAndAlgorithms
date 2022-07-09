'''

  304. Range Sum Query 2D - Immutable
  
'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from _utils import printMatrix



class NumMatrix:
  def __init__(self, matrix):
    if matrix is None or not matrix: return
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    
    for row in range(1, rows + 1):
      for col in range(1, cols + 1):
        currVal = matrix[row-1][col-1]
        prefixLeft = prefix[row][col-1]
        prefixTop = prefix[row-1][col]
        overlap = prefix[row-1][col-1]
        
        prefix[row][col] = currVal + prefixLeft + prefixTop - overlap
    
    printMatrix(prefix)
    self.prefix = prefix
    

  def sumRegion(self, row1, col1, row2, col2):
    pass
      
def runSolution():
  numMatrix = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
  ]);
  numMatrix.sumRegion(2, 1, 4, 3)   # return 8 (i.e sum of the red rectangle)
  numMatrix.sumRegion(1, 1, 2, 2)   # return 11 (i.e sum of the green rectangle)
  numMatrix.sumRegion(1, 2, 2, 4)   # return 12 (i.e sum of the blue rectangle)
  pass
runSolution()