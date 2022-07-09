'''

  413. Arithmetic Slices

'''

class Solution:  
  def numberOfArithmeticSlices(self, nums):
    n = len(nums)
    prev = 0
    ans = 0
    
    for i in range(2, n):
      diff1 = nums[i - 1] - nums[i - 2]
      diff2 = nums[i] - nums[i - 1]
      
      if diff1 == diff2: prev += 1
      else             : prev = 0
      
      ans += prev
    
    return ans
    
  
def runSolution():
  solution = Solution()
  print(solution.numberOfArithmeticSlices(nums = [1,2,3,4]))
  print(solution.numberOfArithmeticSlices(nums = [1]))
  pass
runSolution()