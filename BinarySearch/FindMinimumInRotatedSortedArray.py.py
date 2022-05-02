'''

  33. Search in Rotated Sorted Array

  [1,2,3,4,5]
  
  
  [2,3,4,5,1]
'''

class Solution:
  def findMin(self, nums):
    L, R, n = 0, len(nums) - 1, len(nums)
    
    while L <= R:
      M = L + (R - L)//2
      
      curr = nums[M]
      prev = nums[M - 1] if M > 0 else float('inf')
      next = nums[M + 1] if M < n - 1 else float('inf')
      rightIsSorted = nums[R] > nums[M]
      
      if curr < prev and curr < next: return curr
      if rightIsSorted: R = M - 1
      else            : L = M + 1
        
    return -1
  
  
def runSolution():
  solution = Solution()
  print(solution.findMin(nums = [3,4,5,1,2]))
  print(solution.findMin(nums = [4,5,6,7,0,1,2]))
  print(solution.findMin(nums = [11,13,15,17]))
  pass
runSolution()
