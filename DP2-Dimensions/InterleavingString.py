'''

  97. Interleaving String               

'''

from itertools import product

class SolutionRef:
  def isInterleave(self, s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    DP = {}
    
    def DFS(p1, p2):
      if p1 == n1 and p2 == n2 and p1 + p2 == len(s3): return True
      if p1 + p2 >= n3: return False
      
      if (p1, p2) in DP: return DP[(p1, p2)]
      
      if p1 < n1 and s1[p1] == s3[p1 + p2] and DFS(p1 + 1, p2):
        return True

      if p2 < n2 and s2[p2] == s3[p1 + p2] and DFS(p1, p2 + 1):
        return True
    
      DP[(p1, p2)] = False
      return False
    
    return DFS(0, 0)

class Solution:
  def isInterleave(self, s1, s2, s3):
    DP = {}
    
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 + n2 != n3: return False
    
    def DFS(i1, i2, i3):
      if (i1, i2) in DP: return DP[(i1, i2)]
      if i1 + i2 == n3: return True
      
      if i1 < n1 and s1[i1] == s3[i3] and DFS(i1 + 1, i2, i3 + 1): return True
      if i2 < n2 and s2[i2] == s3[i3] and DFS(i1, i2 + 1, i3 + 1): return True
      
      DP[(i1, i2)] = False
      return False
    
    return DFS(0, 0, 0)
  
def runSolution():
  solution = Solution()
  print(solution.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
  print(solution.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
  print(solution.isInterleave(s1 = "", s2 = "", s3 = ""))
  print(solution.isInterleave(s1 = "", s2 = "", s3 = "a"))
  pass
runSolution()