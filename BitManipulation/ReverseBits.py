'''

  190. Reverse Bits

'''


class Solution:
  def countBits(self, n):
    ans = 0
    
    while n:
      ans = (ans << 1) + (n & 1)
      n = n >> 1
    
    return ans
    
  
def runSolution():
  solution = Solution()
  print(solution.countBits(n = 2))
  print(solution.countBits(n = 5))
  pass
runSolution()
