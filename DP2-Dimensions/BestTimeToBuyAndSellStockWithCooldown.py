'''

  309. Best Time to Buy and Sell Stock with Cooldown

'''

from itertools import product


class SolutionRef:
  def maxProfit(self, prices):
    DP = {} # (i, buying)
    
    def DFS(index, buying):
      if index >= len(prices): return 0
      if (index, buying) in DP: return DP[(index, buying)]
      
      cooldown = DFS(index + 1, buying)
      if buying:
        buy = DFS(index + 1, False) - prices[index]
        DP[(index, buying)] = max(buy, cooldown)
      else:
        sell = DFS(index + 2, True) + prices[index]
        DP[(index, buying)] = max(sell, cooldown)
      
      return DP[(index, buying)]
      
    return DFS(0, True)
    
class Solution:
  def maxProfit(self, prices):
    DP = {}
    n = len(prices)
    
    def DFS(index, buying):
      if (index, buying) in DP: return DP[(index, buying)]
      if index >= n: return 0
      
      cooldown = DFS(index + 1, buying)
      exchange = 0
      
      if buying: exchange = DFS(index + 1, False) - prices[index]
      else     : exchange = DFS(index + 2, True) + prices[index]
      
      DP[(index, buying)] = max(cooldown, exchange)
      return DP[(index, buying)]
    
    return DFS(0, True)
    
    
  
def runSolution():
  solution = Solution()
  print(solution.maxProfit(prices = [1,2,3,0,2]))
  print(solution.maxProfit(prices = [1]))
  pass
runSolution()