'''

  11. Container With Most Water

'''

class Solution:
  def maxArea(self, height):
    mostWater = 0
    n = len(height)
    L, R = 0, n - 1
    
    '''
      1  2  3
         L  R
    '''
    while L < R:
      minHeight = min(height[L], height[R])
      distance  = R - L
      mostWater = max(mostWater, minHeight * distance)
      
      if height[L] < height[R]: L += 1
      else                    : R -= 1
    
    return mostWater
  
def runSolution():
  solution = Solution()
  print(solution.maxArea(height = [1,8,6,2,5,4,8,3,7]))
  pass
runSolution()
