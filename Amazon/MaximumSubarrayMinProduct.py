'''

  1856. Maximum Subarray Min-Product
  
      1  2  3  2
      ^
      P = 0
      N = 3
        
PLE  -1  0  1  0
NLE   4  4  3  4
sum   1  3  6  8

'''

class Solution:
  def maxSumMinProduct(self, nums):
    n = len(nums)
    NLE, PLE, prefixSums = self.init(nums, n)
    result = 0
    
    for i in range(n):
      rightBound = NLE[i]
      leftBound  = PLE[i]
      sub = prefixSums[leftBound] if leftBound >= 0 else 0
      totalSum = prefixSums[rightBound - 1] - sub
      result = max(result, totalSum * nums[i])
    
    return result % (10 ** 9 + 7)
  
  def init(self, nums, n):
    NLE = [n] * n
    PLE = [-1] * n
    prefixSums = [0] * n
    
    stack = []
    for i in range(n - 1, -1, -1):
      while stack and nums[i] <= nums[stack[-1]]: stack.pop()
      if stack: NLE[i] = stack[-1]
      stack.append(i)
    
    stack = []
    for i in range(n):
      while stack and nums[i] <= nums[stack[-1]]: stack.pop()
      if stack: PLE[i] = stack[-1]
      stack.append(i)
    
    currSum = 0
    for i, num in enumerate(nums):
      currSum += num
      prefixSums[i] = currSum
    
    print(NLE)
    print(PLE)
    print(prefixSums)
    return NLE, PLE, prefixSums
    
    
'''

      1  2  3  2
      ^
      P = 0
      N = 3
      
PLE  -1  0  1  0
NLE   4  4  3  4
sum   1  3  6  8

'''
  
def runSolution():
  solution = Solution()
  print(solution.maxSumMinProduct(nums = [1,2,3,2]))
  print(solution.maxSumMinProduct(nums = [2,3,3,1,2]))
  print(solution.maxSumMinProduct(nums = [3,1,5,6,4,2]))
  pass
runSolution()