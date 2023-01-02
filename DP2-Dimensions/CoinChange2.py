'''

  518. Coin Change 2

  total:  0  1  2  3  4  5  6
      0   1  0  0  0  0  0  0
      1   1  1  1  1  1  1  1
      2   1  1
      3   1
      5   1                

  total:  0  1  2  3  4  5  6
      X   1  0  0  0  0  0  0
      2   1  0  1  0  1  0  1
      3   1  0  1  1  1  1  2
      4   1  0  1  1  2  1  3
      5   1  0                

'''

from itertools import product

class SolutionRef:
  def change(self, amount, coins):
    DP = [[0]*(amount + 1) for _ in range(len(coins) + 1)]
    
    for row in range(len(DP)):
      DP[row][0] = 1
    
    for i in range(1, len(DP)):
      coin = coins[i - 1]
      
      for total in range(1, amount + 1):
        DP[i][total] += DP[i - 1][total]
        if coin <= total: DP[i][total] += DP[i][total - coin]
        
    return DP[-1][-1]
  
class Solution:
  def change(self, amount, coins):
    DP = [[0]*(amount + 1) for _ in range(len(coins) + 1)]
    for row in DP: row[0] = 1
    
    for i in range(1, len(coins) + 1):
      coin = coins[i - 1]
      
      for total in range(1, amount + 1):
        DP[i][total] = DP[i - 1][total]
        if coin <= total: DP[i][total] += DP[i][total - coin]
  
    print(DP)
    return DP[-1][-1]
    
    
  
def runSolution():
  solution = Solution()
  print(solution.change(amount = 5, coins = [1,2,5]))
  # print(solution.change(amount = 3, coins = [2]))
  # print(solution.change(amount = 10, coins = [10]))
  pass
runSolution()