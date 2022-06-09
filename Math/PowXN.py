'''

  50. Pow(x, n)

'''

class Solution:
  def twoSum(self, x, n):
    if n == 0: return 1
    if n == 1: return x
    if n == -1: return 1/x
    if n % 2 == 0:
      calc = self.twoSum(x, n / 2)
      return calc * calc
    if n % 2 == 1:
      return self.twoSum(x, n - 1) * x
    
    
  
def runSolution():
  solution = Solution()
  print(solution.twoSum(x = 2.00000, n = 10))
  print(solution.twoSum(x = 2.10000, n = 3))
  print(solution.twoSum(x = 2.00000, n = -2))
  pass
runSolution()
