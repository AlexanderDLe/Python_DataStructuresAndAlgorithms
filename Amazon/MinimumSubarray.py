'''
  1438. Longest Contiguous Subarray with Absolute Diff Less Than Or Equal to Limit


  Sliding Window Technique

  Window Criteria
  When absolute difference between min and max in window is > limit, then contract window

  We'll also need two monotonic queues to hold the current max and min for each window.

'''

import heapq


def longestSubarray(nums, limit):
  maxQ = []
  minQ = []

  getQLast  = lambda Q: nums[Q[-1]]
  getQFirst = lambda Q: nums[Q[0]]
  getDiff   = lambda  : getQFirst(maxQ) - getQFirst(minQ)

  L = 0
  R = 0
  maxLen = 0

  while R < len(nums):
    Rval = nums[R]
    while minQ and Rval < getQLast(minQ): minQ.pop()
    while maxQ and Rval > getQLast(maxQ): maxQ.pop()
    minQ.append(R)
    maxQ.append(R)
    R += 1

    windowLen = R - L
    if getDiff() <= limit: maxLen = max(maxLen, windowLen)

    while getDiff() > limit:
      print(getDiff())
      if minQ[0] == L: minQ.pop(0)
      if maxQ[0] == L: maxQ.pop(0)
      L += 1

  return maxLen    


print(longestSubarray([8,2,4,7], limit = 4))
