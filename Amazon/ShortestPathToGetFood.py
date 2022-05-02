'''

  1730. Shortest Path to Get Food

'''
class Solution:
  
  def getFood(self, grid):
    self.rows = len(grid)
    self.cols = len(grid[0])
    self.grid = grid
    
    startRow, startCol = self.findStartPosition()
    return self.searchBFS(startRow, startCol)

  def searchBFS(self, startRow, startCol):
    grid = self.grid
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    queue = [(startRow, startCol)]
    seen = set()
    seen.add((startRow, startCol))
    
    count = 1
    moves = 0
    
    while queue:
      while count:
        row, col = queue.pop(0)
        if grid[row][col] == '#': return moves
        
        for x, y in dirs:
          nextRow = row + x
          nextCol = col + y
          
          if self.invalidCell(nextRow, nextCol, seen): continue
          seen.add((nextRow, nextCol))
          queue.append((nextRow, nextCol))
        
        count -= 1
      count = len(queue)
      moves += 1
    
    return -1
    
  def invalidCell(self, row, col, seen):
    rows, cols, grid = self.rows, self.cols, self.grid
    
    if row < 0 or row == rows: return True
    if col < 0 or col == cols: return True
    if grid[row][col] == 'X' : return True
    if (row, col) in seen    : return True
    return False
    
  def findStartPosition(self):
    rows, cols, grid = self.rows, self.cols, self.grid  
    
    for row, col in product(range(rows), range(cols)):
      if grid[row][col] == '*': return (row, col)
      
    return -1
  

        
        
def runSolution():  
  solution = Solution()
  print(solution.getFood([
    ["X","X","X","X","X","X"],
    ["X","*","O","O","O","X"],
    ["X","O","O","#","O","X"],
    ["X","X","X","X","X","X"]
  ]))
  print(solution.getFood([
    ["X","X","X","X","X"],
    ["X","*","X","O","X"],
    ["X","O","X","#","X"],
    ["X","X","X","X","X"]
  ]))
  print(solution.getFood([
    ["X","X","X","X","X","X","X","X"],
    ["X","*","O","X","O","#","O","X"],
    ["X","O","O","X","O","O","X","X"],
    ["X","O","O","O","O","#","O","X"],
    ["X","X","X","X","X","X","X","X"]
  ]))

runSolution()