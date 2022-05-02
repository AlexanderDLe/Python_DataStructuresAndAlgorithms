'''

  360. Sort Transformed Array

'''

class Solution:
  def sortTransformedArray(self, nums, a, b, c):
    nums = [x*x*a + x*b + c for x in nums]
    
    result = [0] * len(nums)
    L = 0
    R = len(nums) - 1
    
    
    index, sign = (L, 1) if a < 0 else (R, -1)
    print(nums)
    while L <= R:
      leftIsLarger = nums[L] * -sign > nums[R] * -sign
      
      if leftIsLarger:
        result[index] = nums[L]
        L += 1
      else:
        result[index] = nums[R]
        R -= 1
      index += sign
      print(result)
      
    return result
      
      
    
  
  
  
def runSolution():
  solution = Solution()
  print(solution.sortTransformedArray(nums = [-4,-2,2,4], a = 1, b = 3, c = 5))
  print(solution.sortTransformedArray(nums = [-4,-2,2,4], a = -1, b = 3, c = 5))
  pass
runSolution()