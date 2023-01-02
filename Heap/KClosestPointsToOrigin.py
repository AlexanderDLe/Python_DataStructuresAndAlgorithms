'''

  973. K Closest Points to Origin

'''

import heapq
from heapq import heappush, heappop
import math


class SolutionRef:
  class HeapNode:
    def __init__(self, distance, coord):
      self.distance = distance
      self.coord = coord
      
    def __lt__(self, other):
      return self.distance > other.distance
    
  def kClosest(self, points, k):
    heap = []

    for point in points:
      x, y = point
      distance = math.sqrt((x*x) + (y*y))
      print(distance, point)
      if len(heap) < k:
        heapq.heappush(heap, self.HeapNode(distance, point))
      else:
        if distance >= heap[0].distance: continue
        heapq.heappop(heap)
        heapq.heappush(heap, self.HeapNode(distance, point))
      
    result = []
    while len(heap) > 0:
      node = heapq.heappop(heap)
      result.append(node.coord)

    return result

class Solution:
  
  '''

    Time Complexity:
    O(n * logk) 
    - n for iterating through all points
    - logk to maintain heap of size k
    
    Space Complexity:
    O(k)
    - k is the size of the heap
  
  '''
  
  class HeapNode:
    def __init__(self, distance, point):
      self.distance = distance
      self.point = point
      
    def __lt__(self, other):
      return self.distance > other.distance
    
    
  def kClosest(self, points, k):
    maxHeap = []
    
    for point in points:
      distance = self.calculateDistance(point)
      
      if len(maxHeap) < k:
        heappush(maxHeap, self.HeapNode(distance, point))
      elif distance < maxHeap[0].distance:
        heappop(maxHeap)
        heappush(maxHeap, self.HeapNode(distance, point))
        
    return list(map(lambda x: x.point, maxHeap))
  
  def calculateDistance(self, point):
    x, y = point
    return math.sqrt((x*x) + (y*y))
    
    
  
def runSolution():
  solution = Solution()
  print(solution.kClosest([[1,3],[-2,2]], 1))
  print(solution.kClosest([[3,3],[5,-1],[-2,4]], k = 2))
  pass
runSolution()
