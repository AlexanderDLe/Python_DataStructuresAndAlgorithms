'''

  1584. Min Cost to Connect All Points

'''

from collections import defaultdict
import heapq


class Solution:
  def minCostConnectPoints(self, points):
    n = len(points)
    
    seen = set()
    minHeap = [(0, 0)]
    cost = 0
    
    while len(seen) < n:
      distance, index = heapq.heappop(minHeap)
      if index in seen: continue
      seen.add(index)
      cost += distance
      
      for i in range(n):
        if i in seen: continue
        nextDistance = self.getDistance(points[index], points[i])
        heapq.heappush(minHeap, (nextDistance, i))
    
    return cost
    

  def getDistance(self, x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

  
def runSolution():
  solution = Solution()
  
  print(solution.minCostConnectPoints(
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))
  print(solution.minCostConnectPoints(
    points = [[3,12],[-2,5],[-4,1]]))
  pass
runSolution()