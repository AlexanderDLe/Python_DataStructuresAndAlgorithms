'''

  2013. Detect Squares

  To make a square:
  
  2,5       5,5
  
  2,1       5,1   

  When given a point, ex. (2,1), we have to search for parallel y value.
  
  In the case of (2,1):
  x = 2
  y = 1
  
  1. Search for all matching x values.
     In this case, (2,5 is a matching x value) - that means 2,1 and 2,5 make
     a vertical line.
  
  2. For each vertical line, we have to find a parallel vertical line.
     That means we have to iterate over all the possible vertical lines.
     
     To speed this process, we can store vertical lines via a x-keyed dictionary.
     
     for example:
       
     dict: {
       2: [1, 5],   -> (2,1) and (2,5) create a line
       5: [1, 5]    -> (5,1) and (5,5) create a line
     }
'''

from collections import Counter, defaultdict


class DetectSquaresMyAttempt:
  def __init__(self):
    self.xToYPoints = defaultdict(list)

  def add(self, point):
    self.xToYPoints[point[0]].append(point[1])

  def count(self, point):
    currX, currY = point
    result = 0
    pointsOnSameVerticalLine = self.xToYPoints[currX]
    
    for otherY in pointsOnSameVerticalLine:
      if currY == otherY: continue
      
      for candidateX, candidateYs in self.xToYPoints.items():
        if currX == candidateX: continue
        
        for i in range(0, len(candidateYs) - 1):
          for j in range(i + 1, (len(candidateYs))):
            y1, y2 = candidateYs[i], candidateYs[j]
            if   y1 == currY and y2 == otherY: result += 1
            elif y2 == currY and y1 == otherY: result += 1
    
    return result
    
    
class DetectSquares:
  def __init__(self):
    self.d = Counter()
    self.x_coord = defaultdict(Counter) # x -> all y coordinates with freqs

  def add(self, point):
    x, y1 = point
    self.d[(x, y1)] += 1
    self.x_coord[x][y1] += 1

  def count(self, point):
    x, y1 = point
    res = 0
    
    for y2 in self.x_coord[x]:
      if y1 == y2: continue
      
      sideLen = y2 - y1
      RightX = x + sideLen  # x2 option 1
      leftyX = x - sideLen  # x2 option 2
      
      res += self.d[x, y2] * self.d[RightX, y1] * self.d[RightX, y2]
      res += self.d[x, y2] * self.d[leftyX, y1] * self.d[leftyX, y2]
    
    return res
    
    
  
def runSolution():
  detectSquares = DetectSquares() 
  detectSquares.add([3, 10]) 
  detectSquares.add([11, 2]) 
  detectSquares.add([3, 2]) 
  
  print(detectSquares.count([11, 10]))  # return 1. You can choose:
                                 #   - The first, second, and third points
  print(detectSquares.count([14, 8]))   # return 0. The query point cannot form a square with any points in the data structure.
  detectSquares.add([11, 2])     # Adding duplicate points is allowed.
  print(detectSquares.count([11, 10]))  # return 2. You can choose:
                                 #   - The first, second, and third points
                                 #   - The first, third, and fourth points
  pass
runSolution()