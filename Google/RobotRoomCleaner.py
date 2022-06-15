'''

  489. Robot Room Cleaner

'''



class Solution:
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  
  def cleanRoom(self, robot):
    self.DFS(robot, 0, 0, 0, 1, set())
    
  def DFS(self, robot, x, y, dirX, dirY, visited):
    robot.clean()
    visited.add((x, y))
    
    for k in range(4):
      neighborX = x + dirX
      neighborY = y = dirY
      
      if (neighborX, neighborY) not in visited and robot.move():
        self.DFS(robot, neighborX, neighborY, dirX, dirY, visited)
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
        
      robot.turnLeft()
      dirX, dirY = -dirY, dirX
        
def runSolution():
  solution = Solution()
  print(solution.cleanRoom(None))
  pass
runSolution()