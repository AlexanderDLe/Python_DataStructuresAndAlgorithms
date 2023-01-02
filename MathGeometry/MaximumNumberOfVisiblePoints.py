'''

  1610. Maximum Number of Visible Points

'''


from collections import defaultdict, deque
import math


class Solution:
  def visiblePoints(self, points, angle, location):
    arr, extra = [], 0
    originX, originY = location
    
    for x, y in points:
      if x == originX and y == originY:
        extra += 1
        continue
    
      arr.append(math.atan2(y - originY, x - originX))
      print(arr)
    
    arr.sort()
    arr = arr + [x + 2.0 * math.pi for x in arr]
    angle = math.pi * angle / 180
    
    L = ans = 0
    
    for R in range(len(arr)):
      while arr[R] - arr[L] > angle:
        L += 1
      ans = max(ans, R - L + 1)
    
    return ans + extra
      
    
  
def runSolution():
  solution = Solution()
  print(solution.visiblePoints(
    points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]))
  
  print(solution.visiblePoints(
    points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]))
  
  print(solution.visiblePoints(
    points = [[1,0],[2,1]], angle = 13, location = [1,1]))
  pass
runSolution()