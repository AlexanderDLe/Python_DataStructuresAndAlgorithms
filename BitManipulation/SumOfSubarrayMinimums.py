'''

  136. Single Number

'''


class Solution:
  def singleNumber(self, nums):
    res = 0
    for num in nums: res ^= num
    return res
  
def runSolution():
  solution = Solution()
  print(solution.singleNumber(nums = [2,2,1]))
  print(solution.singleNumber(nums = [4,1,2,1,2]))
  print(solution.singleNumber(nums = [1]))
  pass
runSolution()
