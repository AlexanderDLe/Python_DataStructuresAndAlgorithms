'''

  322. Coin Change

'''

class Solution:
  def coinChange(self, coins, amount):
    DP = [float('inf')] * (amount + 1)
    DP[0] = 0
    
    for coin in coins:
      for total in range(1, len(DP)):
        if coin <= total and DP[total - coin] != float('inf'):
          DP[total] = min(DP[total], DP[total - coin] + 1)
    
    return DP[-1] if DP[-1] != float('inf') else -1
  
def runSolution():
  solution = Solution()
  print(solution.coinChange(coins = [1,2,5], amount = 11))
  print(solution.coinChange(coins = [2], amount = 3))
  print(solution.coinChange(coins = [1], amount = 0))
  pass
runSolution()