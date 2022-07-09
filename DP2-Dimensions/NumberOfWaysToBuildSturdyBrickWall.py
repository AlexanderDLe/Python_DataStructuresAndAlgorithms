'''

  2184. Number of Ways to Build Sturdy Brick Wall

'''

class Solution:  
  def buildWall(self, height, width, bricks):
    layerVariations = self.buildLayerVariations(width, bricks)
    wallVariations  = self.buildWallVariations(height, layerVariations)
    return wallVariations
    
    
  def buildWallVariations(self, height, layerVariations):
    DP = {}
    MOD = 10 ** 9 + 7
    
    def DFS(currHeight, prevLayer):
      if (currHeight, prevLayer) in DP: return DP[(currHeight, prevLayer)]
      if currHeight == height: return 1
      
      res = 0
      
      for currLayer in layerVariations:
        # We use & bit operator because we're checking for overlaps
        # If there are overlaps, then that means two bricks were
        # laid at the same width position (non-sturdy)
        if prevLayer & currLayer: continue
        res += DFS(currHeight + 1, currLayer) % MOD
        
      DP[currHeight, prevLayer] = res
      return res
    
    return DFS(0, 0)
    
  def buildLayerVariations(self, width, bricks):
    bitmasks = [1 << i for i in range(width)]
    combos = []
    
    def DFS(currPos, prevBits):
      if currPos == width:
        combos.append(prevBits)
        return
      
      for brick in bricks:
        if currPos + brick > width: continue
        # Flip bits except if starting bit - because
        # The first wall is allowed to have matching startPoints
        bit = bitmasks[currPos] if currPos != 0 else 0
        DFS(currPos + brick, prevBits | bit)
    
    DFS(0, 0)
    return combos
    
    
  
def runSolution():
  solution = Solution()
  print(solution.buildWall(height = 2, width = 3, bricks = [1,2]))
  print(solution.buildWall(height = 1, width = 1, bricks = [5]))
  pass
runSolution()