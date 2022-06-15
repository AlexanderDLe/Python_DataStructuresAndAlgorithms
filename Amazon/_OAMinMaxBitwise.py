'''

  Question: MAX OR SUBARRAY
  You are given an array A of size N. Now, consider all the subarrays 
  starting at index i - [Ai],[Ai,Ai+1],...,[Ai,...,An]. The score of 
  a subarray is defined as the value obtained after taking the bitwise 
  OR of every element of that subarray. You call a subarray good if 
  the score of that subarray is maximum among all subarrays starting 
  at index i. For every index i, determine the length of the smallest 
  good subarray.

  Given an array A, for every index i, determine the smallest subarray 
  starting at i whose bitwise OR of elements is maximum among all 
  subarrays starting at that index.

  Note: A subarray is a sequence of consecutive elements of an array.
  
  -----------------------------------------------------------------
  
  Example-1

  N = 3
  A = [1, 2, 3]
  Approach

  For i = 1
  For size of subarray = 1, score of this subarray is 1. 
  For size = 2, the score is 1|2=3 
  For size = 3, the score is 1|2|3=3. 
  
  You can see that the maximum score is 3, and the smallest size of 
  the subarray starts at 1, which gives this maximum score 2. 
  So answer for 1st index = 2.
  
  -----------------
  
  For i = 2 
  For size = 1, the score is 2 
  For size = 2, the score is 2|3=3 
  Answer for i=2 is 2.
  
  -----------------
  
  For i = 3 
  For size = 1, the score is 3. 
  So the answer for i = 3 is 1.
  
  Answer: [2, 2, 1]

'''


from collections import defaultdict
from math import inf

class SolutionIDK:
  def minMaxBitwise(self, A):
    n = len(A)
    ans = [-1] * n
    last = [-1] * 31
    
    for i in range(n - 1, -1, -1):
      for j in range(31):
        if A[i] & 1 << j != 0:
          last[j] = i
      
      print(ans, last)
      lastIndex = i
      
      for j in range(31):
        lastIndex = max(lastIndex, last[j])
      
      ans[i] = lastIndex - i + 1
    
    return ans
    
class Solution:
  def minMaxBitwise(self, nums):
    n = len(nums)
    result = [1] * n
    
    for i in range(n):
      prev = nums[i]
      
      for j in range(i + 1, n):
        curr = prev | nums[j]
        if curr > prev: 
          result[i] = j - i + 1
        prev = curr
    
    return result
      
      
        
    
  
def runSolution():
  solution = Solution()
  print(solution.minMaxBitwise([1, 2, 3]))
  print(solution.minMaxBitwise([3, 1, 2]))
  print(solution.minMaxBitwise([2, 3, 2]))
  pass
runSolution()
