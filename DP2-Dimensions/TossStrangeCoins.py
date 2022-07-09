'''

  1230. Toss Strange Coins

'''

class Solution:  
  def probabilityOfHeads(self, prob, target):
    n = len(prob)
    DP = {}
    
    def DFS(index, t):
      if (index, t) in DP: return DP[index, t]
      if index == 0 and t == 0: return 1
      if index == 0: return 0
      
      # Prune
      if index < t: return 0
      
      res = 0
      
      if t: res += DFS(index - 1, t - 1) * prob[index - 1]
      res += DFS(index - 1, t) * (1 - prob[index - 1])
      
      DP[index, t] = res
      return res
      
    
    return DFS(n, target)
    
  
def runSolution():
  solution = Solution()
  print(solution.probabilityOfHeads(prob = [0.4], target = 1))
  print(solution.probabilityOfHeads(prob = [0.5,0.5,0.5,0.5,0.5], target = 0))
  print(solution.probabilityOfHeads(prob = [0.5,0.5,0.5,0.5,0.5], target = 1))
  print(solution.probabilityOfHeads(prob = [0.5,0.5,0.5,0.5,0.5], target = 2))
  pass
runSolution()