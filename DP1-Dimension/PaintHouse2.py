'''

  265. Paint House II

'''

class Solution:
  def minCostII(self, costs):
    n = len(costs[0])
    DP = costs[0].copy()
    
    for row in range(1, len(costs)):
      copy = DP.copy()
      currCosts = costs[row]
      
      for color in range(n):
        rowMin = float('inf')
        
        for k in range(n):
          if color == k: continue
          rowMin = min(rowMin, copy[k])
        
        DP[color] = currCosts[color] + rowMin
    
    return min(DP)
  

def runSolution():
  solution = Solution()
  print(solution.minCostII(costs = [[1,5,3],[2,9,4]]))
  print(solution.minCostII(costs = [[1,3],[2,4]]))
  pass
runSolution()