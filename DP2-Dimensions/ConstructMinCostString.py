'''

  Google Mock

'''

class Solution:  
  def constructMinCostString(self, n, costs):
    DP = {}
    
    def DFS(index, prevIndex):
      if index in DP: return DP[index]
      if index == n: return 0
      
      res = float('inf')
      
      for i, cost in enumerate(costs[index]):
        if i == prevIndex: continue
        res = min(res, cost + DFS(index + 1, i))
      
      DP[index, prevIndex] = res
      return res
    
    return DFS(0, -1)
    
    
  
def runSolution():
  solution = Solution()
  print(solution.constructMinCostString(2, [[2,3,4,5], [7,3,4,1]]))
  print(solution.constructMinCostString(3, [
    [2,3,4,5], 
    [7,3,4,1],
    [2,4,6,1]
  ]))
  pass
runSolution()