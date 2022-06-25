'''
  1438. Longest Contiguous Subarray with Absolute Diff Less Than Or Equal to Limit

  Given an array of integers nums and an integer limit, return the size of the longest 
  non-empty subarray such that the absolute difference between any two elements of this 
  subarray is less than or equal to limit.

  Input: nums = [8,2,4,7], limit = 4
  Output: 2 
  Explanation: All subarrays are: 

  [8]       with maximum absolute diff |8-8| = 0 <= 4.
  [8,2]     with maximum absolute diff |8-2| = 6 > 4. 
  [8,2,4]   with maximum absolute diff |8-2| = 6 > 4.
  [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
  [2]       with maximum absolute diff |2-2| = 0 <= 4.
  [2,4]     with maximum absolute diff |2-4| = 2 <= 4.
  [2,4,7]   with maximum absolute diff |2-7| = 5 > 4.
  [4]       with maximum absolute diff |4-4| = 0 <= 4.
  [4,7]     with maximum absolute diff |4-7| = 3 <= 4.
  [7]       with maximum absolute diff |7-7| = 0 <= 4. 

  Therefore, the size of the longest subarray is 2.

  -----------------------------------------------------------------------

  Sliding Window Technique

  8   2   4   7
  ||

  Use two monotonic Queues
'''

from collections import deque


class SolutionRef:
  def longestSubarray(self, nums, limit):
    maxQ = []
    minQ = []

    getQFront = lambda Q: nums[Q[0]]
    getQLast  = lambda Q: nums[Q[-1]]
    getQDiffs = lambda  : abs(getQFront(maxQ) - getQFront(minQ))

    maxLen = 0
    L = 0
    R = 0

    while R < len(nums):
      Rval = nums[R]

      while maxQ and Rval > getQLast(maxQ): maxQ.pop()
      while minQ and Rval < getQLast(minQ): minQ.pop()

      maxQ.append(R)
      minQ.append(R)
      R += 1

      if getQDiffs() <= limit: maxLen = max(maxLen, R - L)

      while getQDiffs() > limit:
        if L == maxQ[0]: maxQ.pop(0)
        if L == minQ[0]: minQ.pop(0)
        L += 1

    return maxLen
  
class Solution:
  def longestSubarray(self, nums, limit):
    getQDiff  = lambda: abs(getQFront(maxQ) - getQFront(minQ))
    getQLast  = lambda Q: nums[Q[-1]]
    getQFront = lambda Q: nums[Q[0]]
    
    maxQ = deque()
    minQ = deque()
    result = 0
    L = R = 0
    
    while R < len(nums):
      Rnum = nums[R]
      
      while maxQ and Rnum > getQLast(maxQ): maxQ.pop()
      while minQ and Rnum < getQLast(minQ): minQ.pop()
      maxQ.append(R)
      minQ.append(R)
      R += 1
      
      while getQDiff() > limit:
        if maxQ[0] == L: maxQ.popleft()
        if minQ[0] == L: minQ.popleft()
        L += 1
      
      result = max(result, R - L)
    
    return result
  
def runSolution():
  solution = Solution()
  print(solution.longestSubarray([8,2,4,7], 4))
  print(solution.longestSubarray([10,1,2,4,7,2], 5))
  pass
runSolution()