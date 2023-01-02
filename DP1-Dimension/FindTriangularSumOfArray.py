'''

  2221. Find Triangular Sum of an Array

'''

class Solution:
  def triangularSum(self, nums):
    n = len(nums)
    arr = [0] * n
    
    for row in range(n - 1):
      for col in range(n - row - 1):
        arr[col] = (nums[col] + nums[col + 1]) % 10
      print(arr)
      nums = arr
      arr = [0] * n
    
    return nums[0]
  
def runSolution():
  solution = Solution()
  print(solution.triangularSum(nums = [1,2,3,4,5]))
  print(solution.triangularSum(nums = [5]))
  pass
runSolution()