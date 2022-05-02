'''

  1481. Least Number of Unique Integers after K Removals

'''

from collections import Counter
import heapq


class HeapNode:
  def __init__(self, value, freq):
    self.value = value
    self.freq = freq
  def __repr__(self):
    return f'({self.value}, {self.freq})'
  def __lt__(self, other):
    return self.freq < other.freq

class Solution:
  def findLeastNumOfUniqueInts(self, arr, k):
    counter = Counter()
    for num in arr: counter[num] += 1
    
    minHeap = []
    for value, freq in counter.items():
      heapq.heappush(minHeap, HeapNode(value, freq))
    
    while minHeap and k > 0:
      node = heapq.heappop(minHeap)
      value, freq = node.value, node.freq
      
      newFreq = freq - k
      k -= freq
      
      if newFreq > 0:
        heapq.heappush(minHeap, HeapNode(value, newFreq))        
        
    return len(minHeap)
        
      
  
def runSolution():
  solution = Solution()
  print(solution.findLeastNumOfUniqueInts(arr = [5,5,4], k = 1))
  print(solution.findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))
  pass
runSolution()