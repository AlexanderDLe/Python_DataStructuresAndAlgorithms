'''

  238. Product of Array Except Self


    1  2  3  4
L   1  1  2  6
R  24 12  4  1
  
'''


class SolutionRef:
  def productExceptSelf(self, nums):
    n = len(nums)
    L, R = [1] * n, [1] * n
    
    for i in range(1, n):
      L[i] = L[i - 1] * nums[i - 1]
    
    for i in range(n - 2, -1, -1):
      R[i] = R[i + 1] * nums[i + 1]
    
    result = []
    for i in range(n):
      result.append(L[i] * R[i])
    return result


class Solution:
  
  '''

    Time Complexity
    O(n) Iterate through nums
    
    Space Complexity
    O(1) Result array doesn't count
  
  '''
  
  def productExceptSelf(self, nums):
    n = len(nums)
    
    result = [1] * n
    
    for i in range(1, n):
      result[i] = result[i - 1] * nums[i - 1]
      
    currProduct = 1
    for i in range(n-2, -1, -1):
      currProduct *= nums[i + 1]
      result[i] *= currProduct
    
    return result
      
  
def runSolution():
  solution = Solution()
  print(solution.productExceptSelf(nums = [1,2,3,4]))
  print(solution.productExceptSelf(nums = [-1,1,0,-3,3]))
  pass
runSolution()
