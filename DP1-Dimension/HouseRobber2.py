'''

  213. House Robber 2

'''


class Solution:
  def rob(self, nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])
    
    self.nums = nums
    n = len(nums)
    return max(self.process(0, n - 1), self.process(1, n))
  
  def process(self, start, end):
    nums = self.nums

    prev1 = max(nums[start], nums[start + 1])
    prev2 = nums[start]
    
    for i in range(start + 2, end):
      temp  = prev2
      prev2 = prev1
      prev1 = max(prev1, temp + nums[i])
    
    return prev1
  
def runSolution():
  solution = Solution()
  print(solution.rob([1,2,3,1]))
  print(solution.rob([2,3,2]))
  print(solution.rob([1,2,3]))
  print(solution.rob([2,7,9,3,1]))
  pass
runSolution()