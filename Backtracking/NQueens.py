'''

  51. N-Queens
  
'''

class Solution:
  cols = set()
  
  def solveNQueens(self, n):
    board = [['.' for x in range(n)] for y in range(n)]
    self.n = n
    result = []
    
    def backtrack(row, currBoard):
      if row == n:
        result.append(list(map(lambda x: ''.join(x), currBoard)))
        return

      for col in range(n):
        if self.isValid(row, col, currBoard):
          currBoard[row][col] = 'Q'
          self.cols.add(col)
          
          backtrack(row + 1, currBoard)
          
          currBoard[row][col] = '.'
          self.cols.discard(col)
    
    backtrack(0, board)
    return result
  
  def isValid(self, row, col, currBoard):
    if col in self.cols: return False
    
    r, c = row, col
    while r >= 0 and c >= 0:
      if currBoard[r][c] == 'Q': return False
      r -= 1
      c -= 1
    
    r, c = row, col
    while r >= 0 and c < self.n:
      if currBoard[r][c] == 'Q': return False
      r -= 1
      c += 1    
      
    return True
  
  
def runSolution():
  solution = Solution()
  print(solution.solveNQueens(4))
  print(solution.solveNQueens(1))
  pass
runSolution()
