'''

  490. The Maze

  From any spot, roll towards all 4 directions and find destination where you hit a wall (border or 1).
  If you hit a wall, that is the nextDestination.
  
  If you've already visited nextDestination, then no need to visit again (use set to keep track of visited cells).
  Continue to visit cells in all directions for all possible cells until you reach the final destination.
  
  If you can't reach final destination, then return -1.

'''

class Solution:
  def hasPath(self, maze, start, destination):
    self.rows, self.cols = len(maze), len(maze[0])
    self.maze = maze
    visited = set([(start[0], start[1])])
    
    def DFS(row, col):
      if row == destination[0] and col == destination[1]: return True
      reachedFinalDest = False
      
      for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nextDestination = self.getDestination(row, col, (xDir, yDir))
        if nextDestination in visited: continue
        visited.add(nextDestination)
        if DFS(nextDestination[0], nextDestination[1]): reachedFinalDest = True
    
      return reachedFinalDest
    
    return DFS(start[0], start[1])

  def getDestination(self, row, col, dir):
    while self.canMove(row, col, dir):
      row += dir[0]
      col += dir[1]
    return (row, col)
  
  def canMove(self, row, col, dir):
    nextRow = row + dir[0]
    nextCol = col + dir[1]
    if self.outOfBounds(nextRow, nextCol): return False
    if self.maze[nextRow][nextCol] == 1  : return False
    return True
  
  def outOfBounds(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    return False
  

def runSolution():
  solution = Solution()
  print(solution.hasPath(
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], 
    start = [0,4], 
    destination = [4,4]))
  
  print(solution.hasPath(
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], 
    start = [0,4], 
    destination = [3,2]))

  print(solution.hasPath(
    maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], 
    start = [4,3], 
    destination = [0,1]))
  pass
runSolution()