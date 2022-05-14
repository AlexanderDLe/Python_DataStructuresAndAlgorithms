'''

  703. Kth Largest Element in a Stream

'''

import heapq

class KthLargest:
  def __init__(self, k, nums):
    self.heap, self.k = [], k
    for num in nums:
      self.insertHeap(num)

  def add(self, val):
    self.insertHeap(val)
    return self.heap[0]
  
  def insertHeap(self, num):
    if len(self.heap) < self.k:
      heapq.heappush(self.heap, num)
    elif num > self.heap[0]:
      heapq.heappop(self.heap)
      heapq.heappush(self.heap, num)
    

def runSolution():
  kthLargest = KthLargest(3, [4, 5, 8, 2])
  print(kthLargest.add(3))
  print(kthLargest.add(5))
  print(kthLargest.add(10))
  print(kthLargest.add(9))
  print(kthLargest.add(4))
runSolution()