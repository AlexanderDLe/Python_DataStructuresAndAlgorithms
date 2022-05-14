'''

  703. Kth Largest Element in a Stream

'''

import heapq

class Node:
  def __init__(self, val):
    self.val = val
  def __lt__(self, other):
    return self.val > other.val

class Solution:
  def lastStoneWeight(self, stones):
    heap = []
    for stone in stones:
      heapq.heappush(heap, Node(stone))
    
    while len(heap) >= 2:
      x, y = heapq.heappop(heap).val, heapq.heappop(heap).val
      
      if x != y:
        heapq.heappush(heap, Node(x - y))
      
    return heap[0].val if heap else 0
    


def runSolution():
  solution = Solution()
  print(solution.lastStoneWeight([2,7,4,1,8,1]))
  print(solution.lastStoneWeight([1]))
  pass
runSolution()