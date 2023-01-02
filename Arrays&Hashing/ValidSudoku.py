'''

  36. Valid Sudoku

'''

from itertools import product


class SolutionRef:
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
      
  
class Solution:
  def isValidSudoku(self, board):
    for row, col in product(range(9), range(9)):
      if board[row][col] == '.': continue
      if self.invalid(board, row, col): return False
      
    return True
      
  
  def invalid(self, board, row, col):
    currVal = board[row][col]
    
    # Check current row
    for c in range(9):
      if c == col: continue
      if currVal == board[row][c]: return True
    
    # Check current row
    for r in range(9):
      if r == row: continue
      if currVal == board[r][col]: return True
      
    # Check submatrix
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    
    for r in range(startRow, startRow + 3):
      for c in range(startCol, startCol + 3):
        if r == row and c == col: continue
        if currVal == board[r][c]: return True
    
    return False
  
  
  
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
  print(solution.isValidSudoku(board = 
  [["8","3",".",".","7",".",".",".","."]
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
