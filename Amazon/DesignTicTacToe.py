'''

  348. Design Tic-Tac-Toe

  Down diagonals = [0, 0], [1, 1], [2, 2], [3, 3]
  Up diagonals   = [3, 0], [2, 1], [1, 2], [0, 3]

  0  0  0  0
  0  0  0  0
  0  0  0  0
  0  0  0  0
  

'''


class TicTacToe:
  def __init__(self, n):
    self.n = n
    self.rows = [0] * n
    self.cols = [0] * n
    self.upDiagonal = 0
    self.downDiagonal = 0
      
  def move(self, row, col, player):
    self.rows[row] += 1 if player == 1 else -1
    self.cols[col] += 1 if player == 1 else -1
    
    if row == col           : self.downDiagonal += 1 if player == 1 else -1
    if row + col == self.n - 1: self.upDiagonal += 1 if player == 1 else -1

    if abs(self.rows[row])    == self.n: return 1 if player == 1 else 2
    if abs(self.cols[col])    == self.n: return 1 if player == 1 else 2
    if abs(self.upDiagonal)   == self.n: return 1 if player == 1 else 2
    if abs(self.downDiagonal) == self.n: return 1 if player == 1 else 2
    
    return 0
  
  def print(self):
    print('--------------')
    print('hello')
    print(self.n)
    print(self.rows)
    print(self.cols)
    print(self.upDiagonal)
    print(self.downDiagonal)
    pass
      

def runSolution():
  ticTacToe = TicTacToe(3)
  print(ticTacToe.move(0, 0, 1)) # return 0 (no one wins)
  # |X| | |
  # | | | |    Player 1 makes a move at (0, 0).
  # | | | |

  print(ticTacToe.move(0, 2, 2)) # return 0 (no one wins)
  # |X| |O|
  # | | | |    Player 2 makes a move at (0, 2).
  # | | | |

  print(ticTacToe.move(2, 2, 1)) # return 0 (no one wins)
  # |X| |O|
  # | | | |    Player 1 makes a move at (2, 2).
  # | | |X|

  print(ticTacToe.move(1, 1, 2)) # return 0 (no one wins)
  # |X| |O|
  # | |O| |    Player 2 makes a move at (1, 1).
  # | | |X|

  print(ticTacToe.move(2, 0, 1)) # return 0 (no one wins)
  # |X| |O|
  # | |O| |    Player 1 makes a move at (2, 0).
  # |X| |X|

  print(ticTacToe.move(1, 0, 2)) # return 0 (no one wins)
  # |X| |O|
  # |O|O| |    Player 2 makes a move at (1, 0).
  # |X| |X|

  print(ticTacToe.move(2, 1, 1)) # return 1 (player 1 wins)
  # |X| |O|
  # |O|O| |    Player 1 makes a move at (2, 1).
  # |X|X|X|
  ticTacToe.print()
  
  ticTacToe2 = TicTacToe(2)
  print(ticTacToe2.move(0, 0, 2))
  print(ticTacToe2.move(1, 1, 1))
  print(ticTacToe2.move(0, 1, 2))
  ticTacToe2.print()
  # |2|2|
  # | |1|
  
  

runSolution()