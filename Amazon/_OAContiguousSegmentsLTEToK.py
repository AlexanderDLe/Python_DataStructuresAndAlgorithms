'''

  Amazon warehouse has a group of n items of various weights lined up in a row. 
  
  A segment of contiguously placed items can be shipped ogether if only if the difference
  betweeen the weihts of the heaviest and lightest item differs by at most k to avoid load 
  imbalance.

  Given the weights of the n items and an integer k, find the number of segments of items 
  that can be shipped together.

  Note: A segment (l,r) is a subarray starting at index l and ending at index r where l less 
  than equal(<=) r.

  -----------------------------------------------------------------------------------------

  Example:
  weights = [1, 3, 6], k=3

  weight difference between max and min for each (l,r) index pair are:

  (0,0) -> max(weights[0]) - min(weights[0]) = max(1)-min(1) = 1-1 =0
  (0,1) -> max(weights[0], weights[1]) - min(weights[0],weights[1])= max(1,3)-min(1,3)=3-1=2
  (0,2) -> max(weights[0], weights[1], weights[2]) - min(weights[0],weights[1],weights[2])= max(1,3,6)-min(1,3,6)=6-1=5
  (1,1) -> max(weights[1]) - min(weights[1]) = max(3)-min(3) = 3-3 =0
  (1,2) -> max(weights[1], weights[2]) - min(weights[1],weights[2]) = max(3,6)-min(3,6) = 6-3 =3
  (2,2) -> max(weights[2]) - min(weights[2]) = max(6)-min(6) = 6-6 =0

  as only 5 out 6 pair, is less than equal equal to k (3) , so the number of segments that can shipped together is 5.

  -----------------------------------------------------------------------------------------

  Sliding Window + 2 Monotonic Deques
  
  k = 3
  
  [1, 3, 6]
  LR          Subarrays [1]
  
  min = [1]
  max = [1]
  ans = 1

  -----------------------------------------------------------------------------------------
  
  k = 3
  
  [1, 3, 6]
  L   R          Subarrays [1,3], [3]
  
  min = [1, 3]
  max = [3]
  ans = 1 + 2

  -----------------------------------------------------------------------------------------  
  
  k = 3
  
  [1, 3, 6]
   L     R      Difference is greater than 3 (k), therefore we increment L.
  
  min = [1, 3, 6]
  max = [6]
  ans = 1 + 2

  -----------------------------------------------------------------------------------------
  
  k = 3
  
  [1, 3, 6]
      L  R      Difference is <= 3 (k), therefore we add subarrays [3,6], and [6]
  
  min = [3, 6]
  max = [6]
  ans = 1 + 2 + 2

  -----------------------------------------------------------------------------------------
  
  ans = 5
  
  -----------------------------------------------------------------------------------------
  Bonus
  
  [1, 3, 6, 10]
            LR
      
  min = [10]
  max = [10]
  ans = 1 + 2 + 2
  
'''


from collections import defaultdict, deque


class Solution:
  def appealSum(self, nums, k):
    getFirstVal = lambda Q: nums[Q[0]]
    getLastVal  = lambda Q: nums[Q[-1]]
    getDiff = lambda: getFirstVal(maxQ) - getFirstVal(minQ)
    
    maxQ, minQ = deque(), deque()
    L = R = ans = 0
    
    while R < len(nums):
      curr = nums[R]
      while maxQ and curr > getLastVal(maxQ): maxQ.pop()
      while minQ and curr < getLastVal(minQ): minQ.pop()
      maxQ.append(R)
      minQ.append(R)
      
      # Collapse window before adding to answer
      while getDiff() > k:
        if L >= maxQ[0]: maxQ.popleft()
        if L >= minQ[0]: minQ.popleft()
        L += 1
        
      if getDiff() <= k:
        ans += R - L + 1
      
      R += 1
    
    return ans
        
      

    
  
def runSolution():
  solution = Solution()
  print(solution.appealSum([1, 3, 6], 3))
  print(solution.appealSum([1, 3, 6, 10], 3))
  pass
runSolution()
