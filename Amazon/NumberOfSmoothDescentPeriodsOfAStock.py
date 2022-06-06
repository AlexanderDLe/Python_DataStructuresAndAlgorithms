'''

  2110. Number of Smooth Descent Periods of a Stock

'''

class Solution:
  def getDescentPeriods(self, prices):
    result = prevPrice = prevCount = 0
    
    for price in prices:
      if prevPrice - price == 1:
        prevCount += 1
        result += prevCount
      else:
        prevCount = 1
        result += 1
        
      prevPrice = price
    
    return result

  
def runSolution():
  solution = Solution()
  print(solution.getDescentPeriods(prices = [3,2,1,4]))
  print(solution.getDescentPeriods(prices = [8,6,7,7]))
  pass
runSolution()