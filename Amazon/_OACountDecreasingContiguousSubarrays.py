'''

  * CONTIGUOUS *

  You are given an array of integers arr. 
  Your task is to count the number of contiguous subarrays, such that 
  elements of the subarray are arranged in strictly decreasing order.
  
  
  Example:
  
  arr = [9, 8, 4, 9, 3]
  
  Subarray [9, 8, 4] meets the criteria (9 > 8 > 4)
  Subarray [8, 4, 9] does not.
  
  --------------------------------------------------------
  
  Example
  arr = [9, 8, 7, 6, 5], the output should be countDecreasingSubarrays(arr) = 15.
  
  All contiguous subarrays satisfy the condition of problem, 
  because all elements of the array are arranged in decreasing order. 
  
  There are 15 possible contiguous subarrays, so the answer is 15.

  --------------------------------------------------------
  
  * CONTIGUOUS SUBARRAYS FORMULA

  [1,2,3,4]
  All Contiguous Subarrays:

  1: [1][2][3][4]
  2: [1,2][2,3][3,4]
  3: [1,2,3][2,3,4]
  4: [1,2,3,4]

  1 + 2 + 3 + 4 = 10

  formula: n(n+1)/2

  * CONTIGUOUS SUBARRAYS FORMULA

  --------------------------------------------------
  
  [9, 8, 7, 8, 4, 5]
                  ^
      
  count  = 1
  result = 2

'''

from collections import defaultdict

class SolutionRef:
  def countDecreasingSubarrays(self, nums):
    n = len(nums)
    if n == 1: return 1
    
    result = 0
    length = 0
    
    for i in range(n - 1):
      curr, next = nums[i], nums[i + 1]
      length += 1
      
      if curr <= next:
        result += self.countSubarrays(length)
        length = 0
    
    if nums[-1] < nums[-2]:
      length += 1
      result += self.countSubarrays(length)
    else:
      result += self.countSubarrays(length)
      result += 1
    
    return result
  
  def countSubarrays(self, n):
    return (n * (n + 1)) / 2
    
class Solution:
  def countDecreasingSubarrays(self, nums):
    n = len(nums)
    if n == 0: return 0
    
    count = 1
    result = 0
    
    for i in range(1, n):
      prev, curr = nums[i - 1], nums[i]
      if curr >= prev:
        result += self.getSubarrayCount(count)
        count = 0
      count += 1
    
    result += self.getSubarrayCount(count)
    return result
  
  def getSubarrayCount(self, n):
    return n*(n+1)/2
    

    
  
def runSolution():
  solution = Solution()
  # print(solution.countDecreasingSubarrays([9, 8, 7, 6, 5]))
  print(solution.countDecreasingSubarrays([9, 8, 7, 8, 4]))
  # print(solution.countDecreasingSubarrays([7, 6, 8, 5]))
  # print(solution.countDecreasingSubarrays([10, 10, 10]))
  pass
runSolution()
