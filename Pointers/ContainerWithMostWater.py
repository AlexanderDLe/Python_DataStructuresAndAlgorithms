'''

  11. Container With Most Water

'''

class SolutionRef:
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
  
class Solution:
  
  '''
  
    Time Complexity
    O(n) to iterate through heights
    
    Space Complexity
    O(1)
  
  '''
  
  def maxArea(self, height):
    mostWater = 0
    L, R = 0, len(height) - 1
    
    while L < R:
      minHeight = min(height[L], height[R])
      distance = R - L
      currentWater = minHeight * distance
      mostWater = max(mostWater, currentWater)
      
      if height[L] < height[R]: L += 1
      else                    : R -= 1
    
    return mostWater
  
  
def runSolution():
  solution = Solution()
  print(solution.maxArea(height = [1,8,6,2,5,4,8,3,7]))
  pass
runSolution()
