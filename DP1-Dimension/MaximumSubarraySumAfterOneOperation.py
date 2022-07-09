'''

  1746. Maximum Subarray Sum After One Operation

'''

from itertools import groupby


class SolutionRef:
  def maxSumAfterOneOperation(self, nums):
    prevSquare, prevNoSquare, res = 0, 0, 0
    
    for num in nums:
      noSquare = max(num, num + prevNoSquare)
      square = max(num*num, (num*num) + prevNoSquare, num + prevSquare)
      prevSquare, prevNoSquare = square, noSquare
      res = max(noSquare, square)
    
    return res
    
class Solution:
  def maxSumAfterOperation(self, nums):
    prevSquare, prevNoSquare = 0, 0
    maxSum = 0
    
    for num in nums:
      noSquare = max(num, prevNoSquare + num)
      square = max(num*num, prevNoSquare + (num*num), prevSquare + num)
      maxSum = max(maxSum, square, noSquare)
      prevNoSquare = noSquare
      prevSquare = square
    
    return maxSum
  

def runSolution():
  solution = Solution()
  print(solution.maxSumAfterOperation(nums = [2,-1,-4,-3]))
  print(solution.maxSumAfterOperation(nums = [1,-1,1,1,-1,-1,1]))
  print(solution.maxSumAfterOperation(nums = [5,4,-1,7,8]))
  print(solution.maxSumAfterOperation(nums = [-2,1,-3,4,-1,2,1,-5,4]))
  pass
runSolution()