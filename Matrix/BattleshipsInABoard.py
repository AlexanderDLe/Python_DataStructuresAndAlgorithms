'''

  419. Battleships in a Board

'''

class Solution:
  def countBattleships(self, board):
    rows, cols = len(board), len(board[0])
    ships = 0
    
    for row in range(rows):
      for col in range(cols):
        if board[row][col] != 'X': continue
        top  = board[row - 1][col] if row > 0 else '.'
        left = board[row][col - 1] if col > 0 else '.'
        if top == '.' and left == '.': ships += 1
        
    return ships
    
    
  
def runSolution():
  solution = Solution()
  print(solution.countBattleships(
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
  ))
  print(solution.countBattleships(
    board = [["."]]
  ))
  pass
runSolution()