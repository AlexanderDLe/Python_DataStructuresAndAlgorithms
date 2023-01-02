'''

  Problem

  Given a plane with empty collection, implement:

  addPoint(point): that adds the point to collection and returns the 
  co-ordinate of the box formed by the points. 

  removePoint(point) which removes the point from collection and returns 
  the updated co-ordinates of the box.

  _____________________________________________________________________________

  Example:

  addPoint([1,2]) -> return  [[1,2],[1,2]]
  addPoint([0,8])  -> return [[0,2] , [1,8]]
  removePoint([0,8]) -> return [[1,2]]

  explanation : 

  addPoint([1,2]) -> return [[1,2],[1,2]] means the only point present in 
  the collection, that itself is the box

  addPoint([0,8]) -> return [[0,2],[1,8]], now collection contains [1,2] & [0,8] 
  so if we make a box along the x and y axis, the other two points will be [0,2] & [1,8]

  removePoint([0,8]) -> return [[1,2]] , once we remove[0,8], only [1,2] remains


  _____________________________________________________________________________

  Constraints

  1. All points are unique
  2. All points are valid x and y coordinates
  3. Max points is 50

  _____________________________________________________________________________


  Strategy

  Maintain 4 heaps, minX, minY, maxX, maxY

  When a point is added, populate the heaps.
  At any given time, we want the largest rectangle - and we can obtain this by getting
  the min/max coords.

  If a coord is invalid, then we pop from heap and select next.
  We use lazy delete to remove from heap.

  _____________________________________________________________________________

'''

from collections import defaultdict
from heapq import heappush, heappop

class MinNode:
  def __init__(self, val, point):
    self.val = val
    self.point = point
  def __lt__(self, other):
    return self.val < other.val

class MaxNode:
  def __init__(self, val, point):
    self.val = val
    self.point = point
  def __lt__(self, other):
    return self.val > other.val

class Solution:
  def __init__(self):
    self.valid = defaultdict(lambda: False)
    self.minX = []
    self.minY = []
    self.maxX = []
    self.maxY = []

  def addPoint(self, point):
    x, y = point
    self.valid[(x, y)] = True

    heappush(self.minX, MinNode(x, (x, y)))
    heappush(self.maxX, MaxNode(x, (x, y)))
    heappush(self.minY, MinNode(y, (x, y)))
    heappush(self.maxY, MaxNode(y, (x, y)))

    self.lazyDelete(self.minX)
    self.lazyDelete(self.maxX)
    self.lazyDelete(self.minY)
    self.lazyDelete(self.minY)

    topRight = (self.maxX[0].val, self.maxY[0].val)
    botLeft  = (self.minX[0].val, self.minY[0].val)

    return (topRight, botLeft)

  def removePoint(self, point):
    x, y = point
    self.valid[(x, y)] = False

  def lazyDelete(self, heap):
    while heap and self.valid[heap[0].point] == False: heappop(heap)

  
def runSolution():
  solution = Solution()
  print(solution.addPoint([1, 2]))
  print(solution.addPoint([0, 8]))
  print(solution.addPoint([3, 4]))
  print(solution.removePoint([0, 8]))
  print(solution.addPoint([1, 3]))
  pass
runSolution()