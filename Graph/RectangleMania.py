'''

  AlgoExpert Rectangle Mania

'''


from collections import Counter, defaultdict


class Solution:
  def rectangleMania(self, coords):
    xMap = defaultdict(lambda: Counter())
    
    # Build dict that maps yCoords and its frequencies to xCoords
    # We store frequencies because some rectangles may overlap and
    # may need to be counted more than once
    for x, y in coords:
      xMap[x][y] += 1
    
    # Use the x coordinates - not the indices
    xCoords = list(xMap.keys())
    lenX = len(xCoords)
    result = 0
    
    # x1 - Loop through all xCoords except last because
    # last rectangle can't have area of 0
    for x1 in range(lenX - 1):
      x1Val = xCoords[x1]
      yCoords = list(xMap[x1Val].keys())
      
      # x2 - Loop through potential xCoords
      for x2 in range(x1 + 1, lenX):
        x2Val = xCoords[x2]
        
        for i in range(len(yCoords) - 1):
          yI = yCoords[i]
          
          for j in range(i + 1, len(yCoords)):
            yJ = yCoords[j]
            
            # If the map has corresponding matching corners,
            # then add the product to the result.
            
            # Add Product because there may be multiple coords
            # in the same position.
            result += xMap[x2Val][yI] * xMap[x2Val][yJ]
        
    return result
    
    
  
def runSolution():
  solution = Solution()
  # print(solution.rectangleMania(coords = [
  #   [0, 0], [0, 1], [1, 1], [1, 0],
  #   [2, 1], [2, 0], [3, 1], [3, 0],
  # ]))
  # print(solution.rectangleMania(coords = [
  #   [0, 0],[0, 1],[1, 1],[1, 0],[2, 1],
  #   [2, 0],[3, 1],[3, 0],[1, 3],[3, 3]
  # ]))
  print(solution.rectangleMania(coords = [
    [0, 0],[0, 1],[1, 1],[1, 0],[2, 1],[2, 0],
    [3, 1],[3, 0],[1, 3],[3, 3],[0, -4],[3, -4],
    [1, -3],[3, -3],[-1, 0],[-10, 0],[-1, -1],
    [2, -2],[0, -1],[1, -4],[-10, -4]
  ]))
  pass
runSolution()