'''

  152. Maximum Product Subarray

'''

class SolutionRef:
  def maxProduct(self, nums):
    result = max(nums)
    currMin = currMax = 1
    
    for num in nums:
      tempMax = currMax
      currMax = max(num * currMax, num * currMin, num)
      currMin = min(num * tempMax, num * currMin, num)
      result = max(result, currMax)
      
    return result
  
class Solution:
  def maxProduct(self, nums):
    result = max(nums)
    currMin = currMax = 1
    
    for num in nums:
      tempMax = currMax
      currMax = max(currMax * num, currMin * num, num)
      currMin = min(tempMax * num, currMin * num, num)
      result = max(currMax, result)
    
    return result
  
def runSolution():
  solution = Solution()
  print(solution.maxProduct(nums = [2,3,-2,4]))
  print(solution.maxProduct(nums = [-2,0,-1]))
  print(solution.maxProduct(nums = [-5]))
  pass
runSolution()