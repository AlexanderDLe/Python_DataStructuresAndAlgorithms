'''

  55. Jump Game

  2 3 1 1 4
          ^
  
  jumpsLeft = 0

'''

class Solution:
  def canJump(self, nums):
    i = 0
    jumpsLeft = 0
    
    while i < len(nums) - 1:
      jumpsLeft = max(jumpsLeft, nums[i])
      if not jumpsLeft: break
      
      i += 1
      jumpsLeft -= 1
    
    return i == len(nums) - 1


def runSolution():
  solution = Solution()
  print(solution.canJump(nums = [2,3,1,1,4]))
  print(solution.canJump(nums = [3,2,1,0,4]))
  print(solution.canJump(nums = [0,1]))
  pass
runSolution()
