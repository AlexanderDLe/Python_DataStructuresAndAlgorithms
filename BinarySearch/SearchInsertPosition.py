'''

  35. Search Insert Position

'''

from math import floor


class SolutionRef:
  def searchInsert(self, nums, target):
    L, R = 0, len(nums)
    
    while L < R:
      M = L + (R - L)//2
      
      if nums[M] >= target: R = M
      else                : L = M + 1
    
    return L


class Solution:
  def searchInsert(self, nums, target):
    L, R = 0, len(nums)
    
    while L < R:
      M = L + (R - L)//2
      
      if nums[M] >= target: R = M
      else                : L = M + 1
    
    return L


def runSolution():
  solution = Solution()
  print(solution.searchInsert(nums = [1,3,5,6], target = 5))
  print(solution.searchInsert(nums = [1,3,5,6], target = 2))
  print(solution.searchInsert(nums = [1,3,5,6], target = 7))
  pass
runSolution()
