'''
  
  Let's define a kind of message called "Broadcast & Shut Down."

  When a router receives this message, it broadcasts the same message 
  to all other routers within its wireless range.
  
  Then, that router shuts down, and can no longer send or receive messages.

  For example 
  Router A is at (0, 0); 
  Router B is at (0, 8); 
  Router C is at (0, 17); 
  Router D is at (11, 0). 

  If the wireless range is 10, when Router A sends a message, it could first 
  reach B; the message from Router B would further reach Router C but Router D 
  would never receive this message.

  Given a list of routers' locations (their names and the corresponding 2D coordinates), 
  tell me whether a message from Router A can reach Router B. 
  
  Write a method / function with appropriate input and output arguments.
  
  Write test case's. Also, mention the Time and Space complexity for the same.
  
  sqrt((x2 - x1)^2 + (y2 - y1)^2)
  
'''


from collections import deque
from math import sqrt


class Solution:
  def main(self, points, start, target):
    maxDistance = 10
    visited = set([start])
    queue = deque([start])
    
    while queue:
      curr = queue.popleft()
      if curr == target: return True
      
      for next in range(len(points)):
        if next in visited: continue
        
        distanceToNextNode = self.calculateDistance(points[curr], points[next])
        if distanceToNextNode <= maxDistance:
          queue.append(next)
          visited.add(next)     
      
    return False
    
    
  def calculateDistance(self, pointA, pointB):
    xVal = (pointA[0] - pointB[0])**2
    yVal = (pointA[1] - pointB[1])**2
    return sqrt(xVal + yVal)
    
  
def runSolution():
  solution = Solution()
  print(solution.main(
    points = [(0, 0), (0, 8), (0, 17), (11, 0)],
    start = 0,
    target = 1
  ), ': Expect True')
  print(solution.main(
    points = [(0, 0), (0, 8), (0, 17), (11, 0)],
    start = 0,
    target = 3
  ), ': Expect False')
  pass
runSolution()