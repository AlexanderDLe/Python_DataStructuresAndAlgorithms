'''

  130. Surrounded Regions

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from _utils import printMatrix
from itertools import product


class Solution1:
  def solve(self, board):
    self.rows, self.cols = len(board), len(board[0])    
    for row, col in product(range(self.rows), range(self.cols)):
      if board[row][col] == 'O': self.process(row, col, board)
    print(board)
  
  
  def process(self, row, col, board):
    surrounded = True
    
    def preProcess(R, C):
      if self.outOfBounds(R, C):
        nonlocal surrounded
        surrounded = False
        return
      if board[R][C] != 'O': return
      board[R][C] = '-'
      
      for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nextRow, nextCol = R + xDir, C + yDir
        preProcess(nextRow, nextCol)
    
    def postProcess(R, C):
      if self.outOfBounds(R, C): return
      if board[R][C] != '-': return
      
      if surrounded: board[R][C] = 'X'
      else         : board[R][C] = 'O'
      
      for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nextRow, nextCol = R + xDir, C + yDir
        postProcess(nextRow, nextCol)
    
    preProcess(row, col)
    postProcess(row, col)        
  
  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False
    
class Solution:
  def solve(self, board):
    self.rows, self.cols = len(board), len(board[0])
    
    for row, col in product([0, self.rows - 1], range(self.cols)):
      self.DFS(row, col, board)
    
    for row, col in product(range(self.rows), [0, self.cols - 1]):
      self.DFS(row, col, board)
    
    for row, col in product(range(self.rows), range(self.cols)):
      if board[row][col] == '-': board[row][col] = 'O'
      elif board[row][col] == 'O': board[row][col] = 'X'
    
  def DFS(self, row, col, board):
    if self.invalid(row, col, board): return
    
    board[row][col] = '-'    
    for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      nextRow, nextCol = row + xDir, col + yDir
      self.DFS(nextRow, nextCol, board)
  
  def invalid(self, row, col, board):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if board[row][col] != 'O': return True
    return False
    
    
class SolutionRef:
  def solve(self, board):
    if not board or not board[0]:
      return 
    
    # Set land on top/bottom edges to '.'
    for i in [0, len(board)-1]:
      for j in range(len(board[0])):
        self.dfs(board, i, j)   
          
    # Set land on left/right edges to '.'
    for i in range(len(board)):
      for j in [0, len(board[0])-1]:
        self.dfs(board, i, j)
          
    printMatrix(board)
          
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == '.':
          board[i][j] = 'O'
                
  def dfs(self, board, i, j):
    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
      board[i][j] = '.'
      self.dfs(board, i+1, j)
      self.dfs(board, i-1, j)
      self.dfs(board, i, j+1)
      self.dfs(board, i, j-1)

  
def runSolution():
  solution = Solution()
  
  print(solution.solve(
    board = [
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","X","O","X"],
      ["X","O","X","X"]]))
  print(solution.solve(
    board = [
      ["X"]]))
  pass
runSolution()