'''

  217. Contains Duplicate


    1  2  3  4
L   1  1  2  6
R  24 12  4  1
  
'''


class Solution:
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
      
      
  
def runSolution():
  solution = Solution()
  print(solution.productExceptSelf([1,2,3,4]))
  pass
runSolution()
