'''

  939. Minimum Area Rectangle

'''


from collections import Counter, defaultdict


class Solution:
  def minAreaRect(self, points):
    xMap = defaultdict(lambda: set())
    for x, y in points:
      xMap[x].add(y)
      
    minArea = float('inf')
    xCoords = list(xMap.keys())

    for i in range(len(xCoords) - 1):
      x1 = xCoords[i]
      y1Coords = list(xMap[x1])
      
      for j in range(i + 1, len(xCoords)):
        x2 = xCoords[j]
        y2Coords = xMap[x2]
        
        for a in range(len(y1Coords) - 1):
          for b in range(a + 1, len(y1Coords)):
            y1, y2 = y1Coords[a], y1Coords[b]
            if y1 not in y2Coords or y2 not in y2Coords: continue
            
            vertLen = abs(y1 - y2)
            horiLen = abs(x1 - x2)
            minArea = min(minArea, vertLen * horiLen)
    
    return minArea if minArea != float('inf') else 0
    
    
  
def runSolution():
  solution = Solution()
  print(solution.minAreaRect(
    points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
  ))
  print(solution.minAreaRect(
    points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
  ))
  pass
runSolution()