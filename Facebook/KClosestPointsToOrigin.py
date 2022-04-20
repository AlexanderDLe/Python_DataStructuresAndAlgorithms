'''

  973. K Closest Points to Origin

'''

import heapq
import math


class HeapNode:
  def __init__(self, distance, coord) -> None:
    self.distance = distance
    self.coord = coord
  def __lt__(self, other):
    return self.distance > other.distance

def kClosest(points, k):
  heap = []

  for point in points:
    x, y = point
    distance = math.sqrt((x*x) + (y*y))
    print(distance, point)
    if len(heap) < k:
      heapq.heappush(heap, HeapNode(distance, point))
    else:
      if distance >= heap[0].distance: continue
      heapq.heappop(heap)
      heapq.heappush(heap, HeapNode(distance, point))
    
  result = []
  while len(heap) > 0:
    node = heapq.heappop(heap)
    result.append(node.coord)

  return result


print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], k = 2))