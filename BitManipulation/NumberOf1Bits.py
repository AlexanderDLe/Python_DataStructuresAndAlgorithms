'''

  191. Number of 1 Bits

'''


class Solution:
  def countBits(self, n):
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
      n = i
      count = 0
      
      while n:
        n &= (n - 1)
        count += 1
      
      result[i] = count
    
    return result
    
  
def runSolution():
  solution = Solution()
  print(solution.countBits(n = 2))
  print(solution.countBits(n = 5))
  pass
runSolution()
