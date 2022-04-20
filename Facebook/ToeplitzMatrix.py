'''

  766. Toeplitz Matrix

'''

def isToeplitz(matrix):
  rows = len(matrix)
  cols = len(matrix[0])

  def validDiagonal(row, col):
    while row + 1 < rows and col + 1 < cols:
      curr = matrix[row][col]
      next = matrix[row + 1][col + 1]
      
      if curr != next: return False
      row += 1
      col += 1 
      
    return True

  for col in range(cols):
    if validDiagonal(0, col) == False: return False

  for row in range(rows):
    if validDiagonal(row, 0) == False: return False

  return True


print(isToeplitz([
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]))

print(isToeplitz([
  [1,2],
  [2,2]
]))