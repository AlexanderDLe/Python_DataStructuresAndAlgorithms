'''

  1. Two Sum

'''


class Solution:
  def twoSum(self, nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
      diff = target - num
      if diff in seen: return [seen[diff], i]
      seen[num] = i
    
    return []

  
def runSolution():
  solution = Solution()
  print(solution.twoSum([2,7,11,15], target = 9))
  pass
runSolution()
