'''

  733. Flood Fill

'''


class Solution:
  def floodFill(self, image, sr, sc, newColor):
    if sr < 0 or sr >= len(image)   : return image
    if sc < 0 or sc >= len(image[0]): return image
    
    self.rows, self.cols = len(image), len(image[0])
    self.image = image
    orig = image[sr][sc]
    self.newColor = newColor
    
    def DFS(row, col):
      if self.invalidCell(row, col, orig): return 
      image[row][col] = newColor
      
      for xDir, yDir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nextRow, nextCol = row + xDir, col + yDir
        DFS(nextRow, nextCol)
        
    
    DFS(sr, sc)
    return image
  
  def invalidCell(self, row, col, orig):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if self.image[row][col] != orig: return True
    if self.image[row][col] == self.newColor: return True
    return False
    
  
def runSolution():
  solution = Solution()
  print(solution.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))
  print(solution.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2))
  print(solution.floodFill([[0,0,0],[0,1,1]],1,1,1))
  pass
runSolution()