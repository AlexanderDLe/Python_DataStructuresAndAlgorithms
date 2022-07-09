'''

  714. Best Time to Buy and Sell Stock with Transaction Fee

'''

from itertools import groupby


class SolutionTopDown:
  def maxProfit(self, prices, fee):
    n = len(prices)
    DP = {}
    
    def DFS(index, buying):
      if (index, buying) in DP: return DP[(index, buying)]
      if index == n: return 0
      selling = not buying      
      res = 0
      
      # Do nothing at this day
      res = max(res, DFS(index + 1, buying))
      
      # Buy stock on this day
      if buying: res = max(res, DFS(index + 1, False) - prices[index])
      
      # Sell stock on this day
      if selling: res = max(res, DFS(index + 1, True) + prices[index] - fee)
      
      DP[(index, buying)] = res
      return res
    
    return DFS(0, True)
    
  
class Solution:
  def maxProfit(self, prices, fee):
    n = len(prices)
    DP = [[0]*2 for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
      nextDay = DP[i + 1]
      currDay = DP[i]
      
      # Set max buy
      currDay[0] = max(nextDay[0], nextDay[1] + prices[i])
      
      # Set max sell
      currDay[1] = max(nextDay[1], nextDay[0] - prices[i] - fee)
      
      print(prices[i])
      print(DP)
      
    return DP[0][1]
    
  

def runSolution():
  solution = Solution()
  print(solution.maxProfit(prices = [1,3,2,8,4,9], fee = 2))
  # print(solution.maxProfit(prices = [1,3,7,5,10,3], fee = 3))
  pass
runSolution()