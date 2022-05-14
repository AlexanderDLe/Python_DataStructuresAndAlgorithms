'''

  79. Word Search

'''

from collections import defaultdict
from itertools import product

class Solution:
  def exist(self, board, word):
    trie = self.buildTrie(word)
    self.rows, self.cols = len(board), len(board[0])
    
    for row, col in product(range(self.rows), range(self.cols)):
      if board[row][col] == word[0] and self.DFS(row, col, trie, board):
        return True

    return False
        
  def DFS(self, row, col, node, board):
    if self.invalid(row, col, node, board): return False
    
    char = board[row][col]
    node = node[char]
    board[row][col] = '#'
    if 'word' in node: return True
    
    valid = False
    for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      nextRow,nextCol = row + xDir, col + yDir
      valid = valid or self.DFS(nextRow, nextCol, node, board)
    board[row][col] = char
    
    return valid
  
  def invalid(self, row, col, node, board):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if board[row][col] == '#'     : return True
    if board[row][col] not in node: return True
    return False
  
  def buildTrie(self, word):
    trie = {}
    node = trie
    for char in word:
      node = node.setdefault(char, {})
    node['word'] = True
    return trie
  

def runSolution():
  solution = Solution()
  print(solution.exist(
    board = [
      ["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]], 
    word = "ABCCED"
  ))
  print(solution.exist(
    board = [
      ["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]], 
    word = "SEE"
  ))
  print(solution.exist(
    board = [
      ["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]], 
    word = "ABCB"
  ))
  pass
runSolution()

