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
  [1 1 0 0]
  [0 1 1 1]
  [0 1 0 1]

  row 0: 2
  row 1: 2
  row 2: 3
  row 3: 2

  col 0: 1
  col 1: 4
  col 2: 0
  col 3: 3

  max 1s in rows: 3 (3 1s)
  max 1s in cols: 1 (4 1s)

  Save the highest for both row and col.
  Now add them together = 3 + 4 = 7

  Possible number of pixels per row + col = 4 + 4 -1 = 7

  Subtract possible 
'''

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

  



result = calculateGreyness([
  [0 ,1 ,0 ,1],
  [1 ,1 ,0 ,0],
  [0 ,1 ,1 ,1],
  [0 ,1 ,0 ,1]
])
print(result)