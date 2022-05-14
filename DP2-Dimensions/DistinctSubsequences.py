'''

  115. Distinct Subsequences              

'''

from itertools import product

class Solution:
  def numDistinct(self, s, t):
    nS, nT = len(s), len(t)
    DP = {}
    
    def DFS(pS, pT):
      if (pS,pT) in DP: return DP[(pS, pT)]
      if pT == nT: return 1
      if pS == nS: return 0
      
      res = 0

      if s[pS] == t[pT]:
        res += DFS(pS + 1, pT + 1)
        res += DFS(pS + 1, pT)
      else:
        res += DFS(pS + 1, pT)
      
      DP[(pS, pT)] = res
      return res
      
    return DFS(0, 0)
    
  
def runSolution():
  solution = Solution()
  print(solution.change(s = "rabbbit", t = "rabbit"))
  print(solution.change(s = "babgbag", t = "bag"))
  pass
runSolution()