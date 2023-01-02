'''

  1. Two Sum

'''

class Solution:
  '''
    Time Complexity: O(n) - one pass
    Space Complexity: O(n) - hold items in map
  '''
  def twoSum(self, nums, target):
    seenMap = {}
    
    for i, num in enumerate(nums):
      diff = target - num
      
      if diff in seenMap:
        return [seenMap[diff], i]
      
      seenMap[num] = i
    
    return [-1, -1]
  
def runSolution():
  solution = Solution()
  print(solution.twoSum(nums = [2,7,11,15], target = 9))
  print(solution.twoSum(nums = [3,2,4], target = 6))
  print(solution.twoSum(nums = [3,3], target = 6))
  pass
runSolution()
