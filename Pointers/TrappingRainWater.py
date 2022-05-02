'''

  42. Trapping Rain Water

'''

class Solution:
  def trap(self, height):
    n = len(height)
    totalWater = 0
    maxL, maxR = 0, 0
    L, R = 0, n - 1
    
    while L < R:
      maxL = max(maxL, height[L])
      maxR = max(maxR, height[R])
      minHeight = min(maxL, maxR)
      
      if height[L] < height[R]: 
        floor = L + 1
        L += 1
      else                    : 
        floor = R - 1
        R -= 1
      
      totalWater += max(0, minHeight - height[floor])
    
    return totalWater
  
def runSolution():
  solution = Solution()
  print(solution.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
  print(solution.trap(height = [4,2,0,3,2,5]))
  pass
runSolution()
