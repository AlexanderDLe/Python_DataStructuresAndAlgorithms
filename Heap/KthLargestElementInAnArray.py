'''

  215. Kth Largest Element in an Array

'''

from collections import Counter
import heapq


class Solution:
  def findKthLargest(self, nums, k):
    heap = []
    
    for num in nums:
      if len(heap) < k:
        heapq.heappush(heap, num)
      elif num > heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, num)
    
    return heap[0]
    

  
def runSolution():
  solution = Solution()
  print(solution.leastInterval(nums = [3,2,1,5,6,4], k = 2))
  print(solution.leastInterval(nums = [3,2,3,1,2,4,5,5,6], k = 4))
  pass
runSolution()