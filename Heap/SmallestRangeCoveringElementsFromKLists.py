'''

  632. Smallest Range Covering Elements from K Lists
  
'''


from collections import deque
from heapq import heapify, heappop, heappush


class Solution:
  def smallestRange(self, nums):
    res = [float('-inf'), float('inf')]
    minHeap = []
    
    for listIndex, list in enumerate(nums):
      res[0] = min(res[0], list[0])
      res[1] = max(res[1], list[0])
      heappush(minHeap, (list[0], listIndex, 0))
    
    currMax = max([row[0] for row in nums])
    
    while minHeap:
      currMin, listIndex, valIndex = heappop(minHeap)
      
      if currMax - currMin < res[-1] - res[0]:
        res = (currMin, currMax)
      
      if valIndex + 1 == len(nums[listIndex]): break
      
      nextVal = nums[listIndex][valIndex + 1]
      currMax = max(currMax, nextVal)
      heappush(minHeap, (nextVal, listIndex, valIndex + 1))
        
    return res
      
  

  
def runSolution():
  solution = Solution()
  print(solution.smallestRange(nums = [
    [4,10,15,24,26],
    [0, 9,12,20],
    [5,18,22,30]
  ]))
  print(solution.smallestRange(nums = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
  ]))
  pass
runSolution()