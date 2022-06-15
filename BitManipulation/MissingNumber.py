'''

  268. Missing Number

'''


class Solution:
  def missingNumber(self, nums):
    res = len(nums)
    
    for i in range(len(nums)):
      res += (i - nums[i])
  
    return res
    
  
def runSolution():
  solution = Solution()
  print(solution.missingNumber([3,0,1]))
  print(solution.missingNumber([0,1]))
  print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))
  pass
runSolution()
