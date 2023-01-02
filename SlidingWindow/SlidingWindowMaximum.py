'''

  239. Sliding Window Maximum
  
'''

from collections import deque

class SolutionRef:
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
    
    
class Solution:
  
  '''
  
    Time Complexity
    O(n) to iterate through all nums
    
    Space Complexity
    O(k) to hold at most k items in queue
  
  '''
  
  def maxSlidingWindow(self, nums, k):
    result = []
    maxQ = deque()
    L = 0
    
    for R, Rval in enumerate(nums):
      while maxQ and Rval > nums[maxQ[-1]]: maxQ.pop()
      maxQ.append(R)
      
      if maxQ[0] < L: maxQ.popleft()
      
      # Move left boundary forward if window size == k
      if R - L + 1 == k: 
        result.append(nums[maxQ[0]])
        L += 1
    
    return result
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
  print(solution.maxSlidingWindow(nums = [1], k = 1))
  pass
runSolution()
