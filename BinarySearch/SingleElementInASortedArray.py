'''

  540. Single Element in a Sorted Array

  Duplicates appear only twice.
  
  Since duplicates only appear twice, we can figure out if a duplicate is
  on the left or right side by determining if the left side has an even
  number of digits or not.
  
  [1,1,2,2,3,3,4,5,5,6,6,6]
           ^   
  At this first 3, we see it is a duplicate. Since it is the first duplicate,
  then there must be 4 numbers before it.

  if   val == next and M % 2 == 1: R = M - 1
  elif val == next and M % 2 == 0: L = M + 1
  elif val == prev and M % 2 == 0: R = M - 1
  elif val == prev and M % 2 == 1: L = M + 1
'''

class Solution:
  def singleNonDuplicate(self, nums):
    n = len(nums)
    L, R = 0, n - 1
    
    while L <= R:
      M = L + (R - L)//2
      val = nums[M]
      prev = nums[M - 1] if M > 0 else -1
      next = nums[M + 1] if M < n - 1 else -1
      
      if val != prev and val != next: return val
      
      if   val == next and M % 2 == 1: R = M - 1
      elif val == next and M % 2 == 0: L = M + 1
      elif val == prev and M % 2 == 0: R = M - 1
      elif val == prev and M % 2 == 1: L = M + 1
    
    return -1
        
      
      
  
def runSolution():
  solution = Solution()
  print(solution.singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))
  print(solution.singleNonDuplicate(nums = [3,3,7,7,10,11,11]))
  pass
runSolution()
