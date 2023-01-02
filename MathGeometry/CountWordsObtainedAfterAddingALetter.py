'''

  1401. Circle and Rectangle Overlapping
  
'''

from collections import defaultdict

class Solution:
  def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
    # Find the nearest point on the rectangle to the center of the circle
    x_nearest = max(x1, min(xCenter, x2))
    y_nearest = max(y1, min(yCenter, y2))
    
    # Find the distance between the nearest point and the center of the circle
    # Distance between 2 points, (x1,y1) & (x2,y2) in 2D Euclidean space = ((x1-x2)**2 + (y1-y2)**2)**0.5
    distance_x = x_nearest - xCenter
    distance_y = y_nearest - yCenter
    return (distance_x**2 + distance_y**2) <= radius**2

  
def runSolution():
  solution = Solution()
  print(solution.checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))
  print(solution.checkOverlap(radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))
  pass
runSolution()