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
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 + n2 != n3: return False
    
    DP = {}
    
    def DFS(p1, p2):
      if p1 + p2 == n3: return True
      if (p1, p2) in DP: return DP[(p1, p2)]
      
      p3 = p1 + p2
      if p1 < n1 and s1[p1] == s3[p3] and DFS(p1 + 1, p2):
        return True
    
      if p2 < n2 and s2[p2] == s3[p3] and DFS(p1, p2 + 1):
        return True
    
      DP[(p1, p2)] = False
      return False
  
    return DFS(0, 0)
  
def runSolution():
  solution = Solution()
  print(solution.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
  print(solution.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
  print(solution.isInterleave(s1 = "", s2 = "", s3 = ""))
  print(solution.isInterleave(s1 = "", s2 = "", s3 = "a"))
  pass
runSolution()