'''

  1584. Min Cost to Connect All Points

'''

import heapq


class SolutionRef:
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


class Solution:
  def minCostConnectPoints(self, points):
    heap = [(0, 0)] # (distance, index)
    seen = set()
    total = 0
    
    while heap:
      distance, index = heapq.heappop(heap)
      if index in seen: continue
      seen.add(index)
      total += distance
      
      if len(seen) == len(points): break
      
      for nextIndex in range(len(points)):
        if nextIndex in seen: continue
        nextDistance = self.getDistance(points[index], points[nextIndex])
        heapq.heappush(heap, (nextDistance, nextIndex))
    
    return total

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