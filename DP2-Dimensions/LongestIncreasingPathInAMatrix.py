'''

  329. Longest Increasing Path in a Matrix           

'''

from itertools import product

class SolutionMyDPStillTooLong:
  def longestIncreasingPath(self, matrix):
    self.rows, self.cols = len(matrix), len(matrix[0])
    self.matrix = matrix
    
    self.DP = [[-1]*self.cols for _ in range(self.rows)]
    maxPath = 0

    for row, col in product(range(self.rows), range(self.cols)):
      currMax = self.DFS(row, col, 1, float('-inf'))
      self.DP[row][col] = currMax
      maxPath = max(maxPath, currMax)
    
    return maxPath

  def DFS(self, row, col, len, prev):
    if self.invalid(row, col): return len - 1
    if self.matrix[row][col] <= prev: return len - 1
    if self.DP[row][col] != -1: return len + self.DP[row][col] - 1
    
    curr = self.matrix[row][col]
    self.matrix[row][col] = '#'
    maxLen = len
    
    for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      nextRow, nextCol = row + xDir, col + yDir
      maxLen = max(maxLen, self.DFS(nextRow, nextCol, len + 1, curr))
      
    self.matrix[row][col] = curr
      
    return maxLen
  
  def invalid(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if self.matrix[row][col] == '#': return True
    return False

class Solution:
  def longestIncreasingPath(self, matrix):
    self.rows, self.cols = len(matrix), len(matrix[0])
    self.matrix = matrix
    
    self.DP = [[-1]*self.cols for _ in range(self.rows)]
    maxPath = 0

    for row, col in product(range(self.rows), range(self.cols)):
      maxPath = max(maxPath, self.DFS(row, col, float('-inf')))
    
    return maxPath

  def DFS(self, row, col, prev):
    if self.invalid(row, col, prev): return 0
    if self.DP[row][col] != -1: return self.DP[row][col]
    
    res = 1
    for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      nextRow, nextCol = row + xDir, col + yDir
      res = max(res, 1 + self.DFS(nextRow, nextCol, self.matrix[row][col]))
      
    self.DP[row][col] = res
    return res
  
  def invalid(self, row, col, prev):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if self.matrix[row][col] <= prev: return True
    return False



def runSolution():
  solution = Solution()
  print(solution.longestIncreasingPath(matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]]))
  print(solution.longestIncreasingPath(matrix = [
    [3,4,5],
    [3,2,6],
    [2,2,1]]))
  print(solution.longestIncreasingPath(matrix = [
    [1]]))
  pass
runSolution()