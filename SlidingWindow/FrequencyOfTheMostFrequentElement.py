'''

  1838. Frequency of the Most Frequent Element
  
'''

class SolutionRef:
  def maxFrequency(self, nums, k):
    nums.sort()
    L = R = currSum = result = 0
    incsRequired = lambda currSum: nums[R] * (R - L + 1) - currSum
    
    while R < len(nums):
      currSum += nums[R]
      
      while incsRequired(currSum) > k:
        currSum -= nums[L]
        L += 1
      
      result = max(result, R - L + 1)
      R += 1
    
    return result
    
class Solution:
  def maxFrequency(self, nums, k):
    nums.sort()
    L = R = currSum = ans = 0
    incsRequired = lambda currSum: nums[R] * (R - L  + 1) - currSum
    
    while R < len(nums):
      currSum += nums[R]
      
      while incsRequired(currSum) > k:
        currSum -= nums[L]
        L += 1
      
      ans = max(ans, R - L + 1)
      R += 1
    
    return ans
  
def runSolution():
  solution = Solution()
  print(solution.maxFrequency(nums = [1,2,4], k = 5))
  print(solution.maxFrequency(nums = [1,4,8,13], k = 5))
  print(solution.maxFrequency(nums = [3,9,6], k = 2))
  pass
runSolution()
