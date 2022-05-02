'''

  1275. Find Winner on a Tic Tac Toe Game

'''

from turtle import down


class Solution:
  def tictactoe(self, moves):
    rows = [0, 0, 0]
    cols = [0, 0, 0]
    upDiag   = 0
    downDiag = 0
    
    for i in range(len(moves)):
      player = 'A' if i % 2 == 0 else 'B'
      row, col = moves[i]
      
      rows[row] += 1 if player == 'A' else -1
      cols[col] += 1 if player == 'A' else -1
      if row == col:   downDiag += 1 if player == 'A' else -1
      if row + col == 2: upDiag += 1 if player == 'A' else -1
      
      if abs(rows[row]) == 3 or abs(cols[col]) == 3 or abs(upDiag) == 3 or abs(downDiag) == 3:
        return player
    
    return 'Draw' if len(moves) == 9 else 'Pending'
  
  
def runSolution():
  solution = Solution()
  print(solution.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
  print(solution.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
  print(solution.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
  pass
runSolution()
