'''

  2009. Minimum Number of Operations to Make Array Continuous
  
'''

class Solution:
  def minOperations(self, nums):
    n = len(nums)
    nums = sorted(set(nums))
    ans = L = 0
    
    for R in range(len(nums)):
      if nums[R] - nums[L] >= n: L += 1
      ans = max(ans, R - L + 1)
      print(L, R, ans)
    
    return n - ans
    
    
def runSolution():
  solution = Solution()
  print(solution.minOperations(nums = [2,3,4,5]))
  print(solution.minOperations(nums = [1,2,3,5,6]))
  print(solution.minOperations(nums = [1,10,100,1000]))
  pass
runSolution()
