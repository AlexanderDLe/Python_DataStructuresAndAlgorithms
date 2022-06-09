'''

  1143. Longest Common Subsequence
  
    a  c  e
  a 1  
  b    1  1
  c    2 
  d       2
  e       1

'''

from itertools import product


class SolutionBottomUp:
  def longestCommonSubsequence(self, text1, text2):
    DP = [[0]*(len(text2) + 1) for _ in range(len(text1) + 1)]
    
    for i in range(len(text1) - 1, -1, -1):
      for j in range(len(text2) - 1, -1, -1):
        if text1[i] == text2[j]:
          DP[i][j] = 1 + DP[i + 1][j + 1]
        else:
          DP[i][j] = max(DP[i][j + 1], DP[i + 1][j])
    
    return DP[0][0]


class Solution:
  def longestCommonSubsequence(self, text1, text2):
    DP = {}
    n1, n2 = len(text1), len(text2)
    
    def DFS(p, q):
      if (p,q) in DP: return DP[p,q]
      if p >= n1 or q >= n2: return 0
    
      res = 0
      if text1[p] == text2[q]:
        res = 1 + DFS(p + 1, q + 1)
      else:
        res = max(DFS(p + 1,q), DFS(p, q + 1))
      
      DP[p,q] = res
      return res
    
    
    return DFS(0, 0)
  
  
  
def runSolution():
  solution = Solution()
  print(solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
  print(solution.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
  print(solution.longestCommonSubsequence(text1 = "abc", text2 = "def"))
  pass
runSolution()