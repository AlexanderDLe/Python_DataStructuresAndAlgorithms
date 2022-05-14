'''

  703. Kth Largest Element in a Stream

'''

import heapq
from math import sqrt

class Node:
  def __init__(self, distance, point):
    self.distance = distance
    self.point = point
  def __lt__(self, other):
    return self.distance > other.distance

class Solution:
  def kClosest(self, points, k):
    heap = []
    
    for x, y in points:
      distance = sqrt((x*x) + (y*y))
      
      if len(heap) < k:
        heapq.heappush(heap, Node(distance, (x, y)))
      elif distance < heap[0].distance:
        heapq.heappop(heap)
        heapq.heappush(heap, Node(distance, (x, y)))
      
    return list(map(lambda x: x.point, heap))
    


def runSolution():
  solution = Solution()
  print(solution.kClosest(points = [[1,3],[-2,2]], k = 1))
  print(solution.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
  pass
runSolution()