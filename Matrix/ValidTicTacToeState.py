'''

  794. Valid Tic-Tac-Toe State

'''


class Solution:
  def validTicTacToe(self, board):
    xTotal = 0
    oTotal = 0
    
    for row in board:
      xTotal += list(row).count('X')
      oTotal += list(row).count('O')
    
    # First player always places X
    if oTotal > xTotal: return False
    
    # Players take turns
    if abs(xTotal - oTotal) > 1: return False
    
    # There can be only one winning row/col
    wins = 0
    
    for row in range(3): board[row] = list(board[row])
    for B in board, zip(*board):
      for row in B:
        if list(row).count('X') == 3: wins += 1
        if list(row).count('O') == 3: wins += 1
    
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]: wins += 1
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]: wins += 1
    
    if wins > 1: return False
    return True
    
    
    
  
def runSolution():
  solution = Solution()
  # print(solution.validTicTacToe(
  #   board = ["O  ","   ","   "]
  # ))
  # print(solution.validTicTacToe(
  #   board = ["XOX"," X ","   "]
  # ))
  # print(solution.validTicTacToe(
  #   board = ["XOO","X O","XOX"]
  # ))
  # print(solution.validTicTacToe(
  #   board = ["XXX","   ","OOO"]
  # ))
  print(solution.validTicTacToe(
    [
      "XXX",
      "OOX",
      "OOX"]
  ))
  pass
runSolution()