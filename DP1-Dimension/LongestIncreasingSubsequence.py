'''

  300. Longest Increasing Subsequence

    0   1   0   3   2   3
    4   3   3   1   2   1

--------------------------------------------

    0   1   0   3   2   3
                        ^

    LIS = [0, 1, 2, 3]
    
--------------------------------------------

    [10,9,2,5,3,7,101,4,18]
              ^

    LIS = [3, 5]

    Use LIS to keep track of longest increasing subsequences.
    
    1. If a new number is greater than the last number, then simply append to LIS.
    
    2. Otherwise, take the smallest valid placement index and replace that value with
       the new value.
       
       Why do we replace? We replace beacuse there may be future subsequences that include
       these new numbers. These smaller values are more useful than lower values because
       they increase the minimum value range.
       
       Replace the greatest value that is >= num.
       
    Return the length of LIS.
    
'''

from bisect import bisect_left


class SolutionRef:
  def lengthOfLIS(self, nums):
    if not nums: return 0
    
    n = len(nums)
    DP = [1] * n
    DP[0] = 1
    result = 1
    
    for i in range(1, n):
      for j in range(i - 1, -1, -1):
        if nums[j] < nums[i]: 
          DP[i] = max(DP[i], DP[j] + 1)
          result = max(result, DP[i])
    
    return result
  
class Solution1:
  def lengthOfLIS(self, nums):
    LIS = []
    
    for num in nums:
      if (not LIS) or (LIS and num > LIS[-1]):
        LIS.append(num)
      else:
        index = bisect_left(LIS, num)
        LIS[index] = num
    
    print(LIS)
    return len(LIS)
    
class Solution:
  def lengthOfLIS(self, nums):
    LIS = []
    
    for num in nums:
      if not LIS or (LIS and num > LIS[-1]):
        LIS.append(num)
      else:
        index = bisect_left(LIS, num)
        LIS[index] = num
    
    return len(LIS)
    

def runSolution():
  solution = Solution()
  print(solution.lengthOfLIS(nums = [10,9,2,5,3,7,101,4,18]))
  print(solution.lengthOfLIS(nums = [0,1,0,3,2,3]))
  print(solution.lengthOfLIS(nums = [7,7,7,7,7,7,7]))
  pass
runSolution()