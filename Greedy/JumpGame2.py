'''

  45. Jump Game II

  2  3  0  1  4
              ^
  
  nextJump  = 0
  jumpsLeft = 0
  jumpCount = 2
  
'''

class Solution:
  def jump(self, nums):
    jumpCount = jumpsLeft = nextJump = i = 0
    n = len(nums);
    
    for i in range(n - 1):
      nextJump = max(nextJump, nums[i])
      
      if not jumpsLeft:
        jumpCount += 1
        jumpsLeft = nextJump
      
      jumpsLeft -= 1
      nextJump  -= 1
    
    return jumpCount


def runSolution():
  solution = Solution()
  print(solution.jump(nums = [2,3,1,1,4]))
  print(solution.jump(nums = [2,3,0,1,4]))
  pass
runSolution()
