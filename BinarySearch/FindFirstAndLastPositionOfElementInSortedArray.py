'''

  34. Find First and Last Position of Element in Sorted Array

'''

class Solution:
  def searchRange(self, nums, target):
    first = self.binarySearch(nums, target, 'first')
    last  = self.binarySearch(nums, target, 'last')
    return [first, last]
  
  def binarySearch(self, nums, target, search):
    L, R = 0, len(nums) - 1
    
    while L <= R:
      M = L + (R - L)//2
      val = nums[M]
      
      if val != target:
        if val < target: L = M + 1
        else           : R = M - 1
        
      if val == target:
        if search == 'first':
          if   M == 0            : return M
          elif nums[M - 1] != val: return M
          else: R = M - 1
        
        if search == 'last':
          if   M == len(nums) - 1: return M
          elif nums[M + 1] != val: return M
          else: L = M + 1
    
    return -1
      
  
def runSolution():
  solution = Solution()
  print(solution.searchRange(nums = [5,7,7,8,8,10], target = 8))
  # print(solution.searchRange(nums = [5,7,7,8,8,10], target = 6))
  # print(solution.searchRange(nums = [], target = 0))
  pass
runSolution()
