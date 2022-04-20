'''

  215. Kth Largest Element in an Array

'''

import heapq


def findKthLargest(nums, k):
  heap = []

  for num in nums:
    if len(heap) < k:
      heapq.heappush(heap, num)
    else:
      if num > heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, num)
      
  return heap[0]




print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))