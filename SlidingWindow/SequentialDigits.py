'''

  1291. Sequential Digits

'''

class Solution:
  def sequentialDigits(self, low, high):
    result = []
    val = '123456789'
    
    def process(digits):
      for i in range(0, 10 - digits):
        num = int(val[i:i+digits])
        if num < low: continue
        if num > high: return
        result.append(num)
    
    LDigits = len(list(str(low)))
    HDigits = len(list(str(high)))
    for digits in range(LDigits, HDigits + 1):
      process(digits)
    
    return result
  
  
def runSolution():
  solution = Solution()
  print(solution.sequentialDigits(low = 100, high = 300))
  print(solution.sequentialDigits(low = 1000, high = 13000))
  pass
runSolution()
