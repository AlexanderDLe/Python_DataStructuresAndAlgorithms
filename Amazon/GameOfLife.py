'''

  289. Game of Life


  0 = Dead
  1 = Alive
  2 = Was alive - will be dead
  3 = Was dead  - will be alive
  
  [0,2,0]
  [0,0,1]
  [1,1,1]
  [0,0,0]
'''

from itertools import product


class Solution:
  dirs = [
    (-1,-1), (-1, 0), (-1, 1),
    ( 0,-1),          ( 0, 1),
    ( 1,-1), ( 1, 0), ( 1, 1)
  ]
  
  def gameOfLife(self, board):
    self.rows, self.cols = len(board), len(board[0])
    
    for row, col in product(range(self.rows), range(self.cols)):
      liveAdjacentCells = self.adjacentLiveCells(board, row, col)
      currCell = board[row][col]
      
      if currCell == 1:
        if liveAdjacentCells < 2 or liveAdjacentCells > 3:
          board[row][col] = 2
          
      if currCell == 0:
        if liveAdjacentCells == 3:
          board[row][col] = 3
          
    for row, col in product(range(self.rows), range(self.cols)):
      if board[row][col] == 2: board[row][col] = 0
      if board[row][col] == 3: board[row][col] = 1
      
    return board
      
  
  def adjacentLiveCells(self, board, row, col):
    liveCells = 0
    
    for xDir, yDir in self.dirs:
      nextRow, nextCol = row + xDir, col + yDir
      if self.outOfBounds(nextRow, nextCol): continue
      cell = board[nextRow][nextCol]
      if cell == 1 or cell == 2: liveCells += 1
    
    return liveCells

  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False
  
def runSolution():  
  solution = Solution()
  print(solution.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
  print(solution.gameOfLife(board = [[1,1],[1,0]]))
runSolution()