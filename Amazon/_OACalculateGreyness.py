'''

  You are given a black & white image in form of m*n pixel matrix grid.

  if pixel[i][j] = 0 then pixel is black
  if pixel[i][j] = 1 then pixel is white
  Calculate maximum greyness of image.

  Where greyness of a pixel[i][j] = 
  (number of 1s in ith row + number of 1s in jth column) -
  (number of 0s in ith row + number of 0s in jth column)

  -----------------------------------------------------------

  0 is black
  1 is white

  [0 1 0 1]
  [1 1 0 0]
  [0 1 0 1]
  [0 1 0 1]
  
  Maximum Greyness:
  All 1s in current row and column - All 0s in current row and column
  
  Greyness in pixel [0,0] = 3 - 3 = 0
  Greyness in pixel [0,1] = 5 - 2 = 3
  
  -----------------------------------------------------------
  
  Idea: precompute number of 1s in each row and column.
  Time: O(n*m)
  
  
  [0 1 0 1]
  [0 1 0 0]
  [0 0 1 1]
  [0 1 0 1]

  rows = [2, 1, 2, 2]
  cols = [0, 3, 1, 3]
  
  Despite there being multiple 2s in rows and multiple 3 in cols,
  the row is row 3 and col 2 (1-indexed) because their intersection
  does not include a 1 (which means they would have to share a 1).
  
  To determine the best combination, we can create a indexMap that shows
  where the max rows/cols are located.
  
  rowsIndices: [0, 2, 3]
  colsIndices: [1, 3]
  
  These indicate the indexes of the 2s in rows and 3s in cols.
  
  Next, get totalPossibleOnes = rows + cols - 1 (subtract 1 for intersection)
  totalOnes = maxRowOnes + maxColOnes - pixels[bestCombination]
  totalZeroes = totalPossibleOnes - totalOnes
  
  result = totalOnes - totalZeroes

'''

from itertools import product


def calculateGreyness(pixels):
  rows = len(pixels)
  cols = len(pixels[0])

  totalPossibleOnes = rows + cols - 1
  maxOnesInRows = 0
  maxOnesInCols = 0
  maxRow = 0
  maxCol = 0

  # Assuming nxn matrix, we can iterate n*m once, otherwise iterate twice
  for row in range(rows):
    currOnesInRow = 0
    for col in range(cols):
      currOnesInRow += pixels[row][col]

    if currOnesInRow > maxOnesInRows: 
      maxOnesInRows = currOnesInRow
      maxRow = row

  for col in range(cols):
    currOnesInCol = 0
    for row in range(rows):
      currOnesInCol += pixels[row][col]

    if currOnesInCol > maxOnesInCols: 
      maxOnesInCols = currOnesInCol
      maxCol = col

  
  totalOnes = maxOnesInRows + maxOnesInCols - pixels[maxRow][maxCol]
  totalZeroes = totalPossibleOnes - totalOnes

  return totalOnes - totalZeroes
  
class Solution:  
  def calculateGreyness(self, pixels):
    rows, cols = len(pixels), len(pixels[0])
    maxRowIndices, maxColIndices = [], []
    maxRowOnes = maxColOnes = 0
    
    for i, row in enumerate(pixels):
      onesInCurrRow = row.count(1)
      
      if onesInCurrRow > maxRowOnes:
        maxRowOnes = onesInCurrRow
        maxRowIndices = [i]
      elif onesInCurrRow == maxRowOnes:
        maxRowIndices.append(i)
    
    for col in range(cols):
      onesInCurrCol = 0
      
      for row in range(rows): 
        onesInCurrCol += pixels[row][col]
      
      if onesInCurrCol > maxColOnes:
        maxColOnes = onesInCurrCol
        maxColIndices = [col]
      elif onesInCurrCol == maxColOnes:
        maxColIndices.append(col)
    
    # Search for a pair of (maxRow, maxCol) such that
    # the intersection pixel is 0 (if possible). Otherwise use any.
    bestCombo = (maxRowIndices[0], maxColIndices[0])
    for row, col in product(maxRowIndices, maxColIndices):
      if pixels[row][col] == 0:
        bestCombo = (row, col)
        break
    
    totalPossibleOnes = rows + cols - 1
    totalOnes = maxRowOnes + maxColOnes - pixels[bestCombo[0]][bestCombo[1]]
    totalZeroes = totalPossibleOnes - totalOnes
    return totalOnes - totalZeroes
      
      
  
def runSolution():
  solution = Solution()
  print(solution.calculateGreyness([
    [0 ,1 ,0 ,1],
    [0 ,1 ,0 ,0],
    [0 ,0 ,1 ,1],
    [0 ,1 ,0 ,1]
  ]))
  pass
runSolution()


