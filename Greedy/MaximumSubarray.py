'''

  53. Maximum Subarray

'''

class Solution:
  def maxSubArray(self, nums):
    maxSum = curMax = nums[0]
    
    for num in nums[1:]: 
      curMax = max(curMax + num, num)
      maxSum = max(maxSum, curMax)
  
    return maxSum
  
class SolutionDivideAndConquer:
  def maxSubArray(self, nums):
    return self.helper(nums, 0, len(nums) - 1)
  
  def helper(self, nums, L, R):
    if L > R: return float('-inf')
    
    M = (L + R)/2
    
    leftMax = sumNum = 0
    
    for i in range(M - 1, L - 1, -1):
      sumNum += nums[i]
      leftMax = max(leftMax, sumNum)
    
    rightMax = sumNum = 0
    
    for i in range(M + 1, R + 1):
      sumNum += nums[i]
      rightMax = max(rightMax, sumNum)
    
    leftAns = self.helper(nums, L, M - 1)
    rightAns = self.helper(nums, M + 1, R)
    
    return max(leftMax + nums[M] + rightMax, max(leftAns, rightAns))
    
  



def runSolution():
  solution = Solution()
  print(solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
  print(solution.maxSubArray(nums = [1]))
  print(solution.maxSubArray(nums = [5,4,-1,7,8]))
  pass
runSolution()
