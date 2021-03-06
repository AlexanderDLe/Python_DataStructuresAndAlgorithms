'''

  410. Split Array Largest Sum

'''

class SolutionRef:
  def splitArray(self, nums, m):
    self.partitions, self.nums = m, nums
    L, R = max(nums), sum(nums)
    
    while L < R:
      maxSum = L + (R - L)//2
      
      if self.isFeasible(maxSum): R = maxSum
      else                         : L = maxSum + 1
    
    return L
  
  def isFeasible(self, threshold):
    currSum = 0
    partitions = 1
    
    for num in self.nums:
      currSum += num
      
      if currSum > threshold:
        partitions += 1
        currSum = num
    
    return partitions <= self.partitions
  
class Solution:
  def splitArray(self, nums, m):
    self.nums, self.m = nums, m
    L, R = max(nums), sum(nums)
    
    while L < R:
      maxSum = L + (R - L)//2
      if self.feasible(maxSum): R = maxSum
      else                    : L = maxSum + 1
    
    return L
    
  
  def feasible(self, maxSum):
    currSum = 0
    partitions = 1
    
    for num in self.nums:
      currSum += num
      
      if currSum > maxSum:
        currSum = num
        partitions += 1
    
    return partitions <= self.m
  
  
def runSolution():
  solution = Solution()
  print(solution.splitArray(nums = [7,2,5,10,8], m = 2))
  print(solution.splitArray(nums = [1,2,3,4,5], m = 2))
  print(solution.splitArray(nums = [1,4,4], m = 3))
  pass
runSolution()
