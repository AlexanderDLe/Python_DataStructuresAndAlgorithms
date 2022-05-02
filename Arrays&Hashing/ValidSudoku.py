'''

  36. Valid Sudoku

'''

from itertools import product


class Solution:
  def isValidSudoku(self, board):
    for row, col in product(range(9), range(9)):
      if board[row][col] != '.':
        if self.isValid(row, col, board) == False: return False
  
    return True

    
  def isValid(self, row, col, board):
    digit = board[row][col]
    
    for i in range(0, 9):
      if i == col: continue
      if board[row][i] == digit: return False
      
    for i in range(0, 9):
      if i == row: continue
      if board[i][col] == digit: return False
      
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    
    for R in range(startRow, startRow + 3):
      for C in range(startCol, startCol + 3):
        if R == row and C == col: continue
        if board[R][C] == digit: return False
    
    return True
      
  
  
  
def runSolution():
  solution = Solution()
  print(solution.isValidSudoku([
   ["5","3",".",".","7",".",".",".","."]
  ,["6",".",".","1","9","5",".",".","."]
  ,[".","9","8",".",".",".",".","6","."]
  ,["8",".",".",".","6",".",".",".","3"]
  ,["4",".",".","8",".","3",".",".","1"]
  ,["7",".",".",".","2",".",".",".","6"]
  ,[".","6",".",".",".",".","2","8","."]
  ,[".",".",".","4","1","9",".",".","5"]
  ,[".",".",".",".","8",".",".","7","9"]
  ]))
  pass
runSolution()
