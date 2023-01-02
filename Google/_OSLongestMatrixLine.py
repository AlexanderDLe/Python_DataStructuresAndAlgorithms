'''
  
  Given an image binary matrix n * m , pixel denotes 1 , We have to calculate the longest straight line which we can draw. (you can go each direction.)

  ex =  [ 
    [0,1,0,0,0]
		[0,1,0,0,0]
		[1,1,1,0,0]
		[0,0,1,0,0]
		[0,0,0,1,0]
		[0,0,0,0,1]
  ]
  output :-   4

	explanation :- indexes (2,1) -> (3,2) -> (4,3) -> (5,4) able to make straight line with length 4.
	
		I was able to solve this question during interview by DFS + DP (3D).(dp[x][y][direction]).
		
	Open for suggestion or improvisation.
  
'''


from itertools import product
import time


class Solution:
  def main(self, matrix):
    H, V, D1, D2 = 0, 1, 2, 3
    self.matrix = matrix
    self.rows, self.cols = len(matrix), len(matrix[0])
    result = 0
    DP = {}
    
    def DFS(row, col, dir):
      if self.invalid(row, col): return 0
      if (row, col, dir) in DP: return DP[row, col, dir]
      
      temp = matrix[row][col]
      matrix[row][col] = '#'
      currLen = 1
      
      if dir == V: 
        currLen += DFS(row + 1, col, dir) + DFS(row - 1, col, dir)
      if dir == H: 
        currLen += DFS(row, col + 1, dir) + DFS(row, col - 1, dir)
      if dir == D1:
        currLen += DFS(row + 1, col + 1, dir) + DFS(row - 1, col - 1, dir)
      if dir == D2:
        currLen += DFS(row + 1, col - 1, dir) + DFS(row - 1, col + 1, dir)
      
      matrix[row][col] = temp
      DP[(row, col, dir)] = currLen
      return currLen      
    
    
    for row, col in product(range(self.rows), range(self.cols)):
      if matrix[row][col] == 0: continue      
      for dir in [H, V, D1, D2]:
        result = max(result, DFS(row, col, dir))
        
    return result
        
  def invalid(self, row, col):
    if row < 0 or row == self.rows : return True
    if col < 0 or col == self.cols : return True
    if self.matrix[row][col] == 0  : return True
    if self.matrix[row][col] == '#': return True
    return False

def runSolution():
  solution = Solution()
  print(solution.main(matrix = [
    [0,1,0,0,0],
    [0,1,0,0,0],
    [1,1,1,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1],
 ]))
  pass
runSolution()