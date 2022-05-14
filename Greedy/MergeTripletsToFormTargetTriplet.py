'''

  1899. Merge Triplets to Form Target Triplet
  
'''

from collections import Counter, defaultdict
import heapq

class Solution:
  def mergeTriplets(self, triplets, target):
    xMax = yMax = zMax = 0
    
    for x, y, z in triplets:
      if x > target[0] or y > target[1] or z > target[2]: continue
      xMax = max(x, xMax)
      yMax = max(y, yMax)
      zMax = max(z, zMax)
      
    return [xMax, yMax, zMax] == target
    

def runSolution():
  solution = Solution()
  print(solution.mergeTriplets(triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]))
  print(solution.mergeTriplets(triplets = [[3,4,5],[4,5,6]], target = [3,2,5]))
  print(solution.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))
  pass
runSolution()
