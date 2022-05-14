'''

  212. Word Search II

'''

from collections import defaultdict
from itertools import product

class Solution:
  def findWords(self, board, words):
    trie = self.buildTrie(words)
    self.board = board
    self.rows, self.cols = len(board), len(board[0])
    
    result = []
    for row, col in product(range(self.rows), range(self.cols)):
      self.DFS(row, col, trie, result)
      
    return result
      
  def DFS(self, row, col, node, result):
    if self.invalidCell(row, col, node): return
    
    char = self.board[row][col]
    node = node[char]
    
    if 'word' in node:
      result.append(node['word'])
      del node['word']
    
    self.board[row][col] = '#'
    for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      nextRow, nextCol = row + xDir, col + yDir
      self.DFS(nextRow, nextCol, node, result)
    self.board[row][col] = char
      
      
  def buildTrie(self, words):
    trie = {}
    for word in words:
      node = trie
      for char in word:
        node = node.setdefault(char, {})
      node['word'] = word
    return trie
  
  def invalidCell(self, row, col, node):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if self.board[row][col] not in node: return True
    return False
  

def runSolution():
  solution = Solution()
  print(solution.findWords(
    board = [
      ["o","a","a","n"],
      ["e","t","a","e"],
      ["i","h","k","r"],
      ["i","f","l","v"]
    ], 
    words = ["oath","pea","eat","rain"]
  ))
  print(solution.findWords(
    board = [
      ["a","b"],
      ["c","d"]
    ], 
    words = ["abcb"]
  ))
  pass
runSolution()

