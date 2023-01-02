'''

  121. Best Time to Buy and Sell Stock

'''

class SolutionRef:
  def maxProfit(self, prices):
    minPrice = prices[0]
    maxProfit = 0
    
    for i in range(1, len(prices)):
      curr = prices[i]
      maxProfit = max(maxProfit, curr - minPrice)
      minPrice = min(minPrice, curr)
      
    return maxProfit

class Solution:
  def maxProfit(self, prices):
    maxProfit = 0
    minCost = prices[0]
    
    for i in range(1, len(prices)):
      price = prices[i]
      maxProfit = max(maxProfit, price - minCost)
      minCost = min(minCost, price)
    
    return maxProfit
  
def runSolution():
  solution = Solution()
  print(solution.maxProfit(prices = [7,1,5,3,6,4]))
  print(solution.maxProfit(prices = [7,6,4,3,1]))
  pass
runSolution()
