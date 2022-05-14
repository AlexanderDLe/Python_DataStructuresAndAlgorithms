'''

  239. Sliding Window Maximum
  
'''

from collections import deque



class Solution:
  def maxSlidingWindow(self, nums, k):
    getQLast = lambda Q: nums[Q[-1]]
    monoQ = deque()
    result = []
    
    for R, Rnum in enumerate(nums):
      while monoQ and Rnum >= getQLast(monoQ): monoQ.pop()
      monoQ.append(R)
      
      if monoQ[0] == R - k: monoQ.popleft()
      
      if R >= k - 1: result.append(nums[monoQ[0]])
    
    return result
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
  print(solution.maxSlidingWindow(nums = [1], k = 1))
  pass
runSolution()
