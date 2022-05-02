'''

  704. Binary Search

'''

class SolutionAllCheck:
  def search(self, nums, target):
    L, R = 0, len(nums) - 1
    
    while L <= R:
      M = (L + R + 1)//2
      
      if nums[M] == target: return M
      if nums[M] > target : R = M - 1
      else                : L = M + 1
    
    return -1

class Solution:
  def search(self, nums, target):
    L, R = 0, len(nums)
    
    while L < R:
      M = L + (R - L)//2
      print(L, M, R)
      
      if nums[M] == target: return M
      if nums[M] >  target: R = M
      else                : L = M + 1
    
    return L if nums[L] == target else -1
  
  
def runSolution():
  solution = Solution()
  print(solution.search(nums = [-1,0,3,5,9,12], target = 9))
  print(solution.search(nums = [-1,0,3,5,9,12], target = 2))
  print(solution.search(nums = [5], target = 5))
  pass
runSolution()
