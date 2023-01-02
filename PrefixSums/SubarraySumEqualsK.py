'''

  560. Subarray Sum Equals K

  k = 2

  5  5  1  1
0 5 10 11 12

  set = [0, 5, 10, 11, 12]

  -----------------------------------

  k = 0

  1  -1  0
0 1   0  0
     | |      <-- One subarray
     |   |    <-- Two subarrays
        | |   <-- Three subarrays

  Since subarrays can overlap, you need to use a dict to keep track
  of occurences a particular sum

  ---------------------------------------------------------------------
  ---------------------------------------------------------------------
  ---------------------------------------------------------------------
  ---------------------------------------------------------------------
  
  [1, 2, 3] k = 3
  
  Iterate over the input array, keep a running sum for prefix sums.
  For every iteration, determine if a it is possible to find value sum - k
  in the dict.
  
  If a value exists in freqmap that is sum - k, that means a subarray of value k exists.
  
  [1, 2, 3] k = 3
   ^
  
  currentSum = 1
  
  freqMap = {
    0: 1      <--- base case
    1: 1
  }
  
  1 - 3 = -2. -2 does not exist in the freqMap.
  
  ---------------------------------------------------------------------
    
  [1, 2, 3] k = 3
      ^
  
  currentSum = 3
  
  freqMap = {
    0: 1
    1: 1
  }
  
  3 - 3 = 0. 0 DOES exist in the freqMap. Increment result by that amount.
  
  freqMap = {
    0: 1
    1: 1
    3: 1
  }
  
  ---------------------------------------------------------------------
    
  [1, 2, 3] k = 3
         ^
  
  currentSum = 6
  
  freqMap = {
    0: 1
    1: 1
    3: 1
  }
  
  6 - 3 = 3. 3 DOES exist in the freqMap. Increment result by that amount.
  
  freqMap = {
    0: 1
    1: 1
    3: 1
    6: 1
  }
  
  ---------------------------------------------------------------------

'''

from collections import defaultdict


class Solution:
  
  '''
  
    Time Complexity
    O(n) - Iterate through all numbers
    
    Space Complexity
    O(n) - Store the running sums in a freqMap
  
  '''
  
  def subarraySum(self, nums, k):
    freqMap = defaultdict(int)
    freqMap[0] = 1
    currentSum = 0
    result = 0
    
    for num in nums:
      currentSum += num
      diff = currentSum - k
      result += freqMap[diff]
      freqMap[currentSum] += 1
      
    return result
      



def runSolution():
  solution = Solution()
  print(solution.subarraySum([1,1,1], 2))
  print(solution.subarraySum([1,2,3], 3))
  print(solution.subarraySum([1,-1,0], 0))
  pass
runSolution()
