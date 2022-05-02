'''

  33. Search in Rotated Sorted Array

'''

class Solution:
  def search(self, nums, target):
    L, R = 0, len(nums) - 1
    
    while L <= R:
      M = L + (R - L)//2
      rightIsSorted = nums[R] > nums[M]
      
      if nums[M] == target: return M
      
      if rightIsSorted:
        if nums[M] <= target <= nums[R]: L = M + 1
        else                           : R = M - 1
      else:
        if nums[L] <= target <= nums[M]: R = M - 1
        else                           : L = M + 1
        
    return -1
  
  
def runSolution():
  solution = Solution()
  print(solution.search(nums = [4,5,6,7,0,1,2], target = 0))
  print(solution.search(nums = [4,5,6,7,0,1,2], target = 3))
  print(solution.search(nums = [1], target = 0))
  pass
runSolution()
