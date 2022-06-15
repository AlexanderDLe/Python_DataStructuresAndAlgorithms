'''

  509. Fibonacci Number


    1  2  3  1
              
m:  1  2  4  4
             ^ Take either the previous largest value or rob prev-prev
'''


class Solution:
  def rob(self, nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
      temp  = prev2
      prev2 = prev1
      prev1 = max(prev1, temp + nums[i])
    
    return prev1
  
def runSolution():
  solution = Solution()
  print(solution.rob([1,2,3,1]))
  print(solution.rob([2,7,9,3,1]))
  pass
runSolution()