'''

  278. First Bad Version

'''

class Solution:
  def search(self, n = 5, bad = 4):
    L, R = 1, n
    
    while L < R:
      M = L + (R - L)//2
      
      if self.isBadVersion(M, n): R = M
      else                      : L = M + 1
      
    return L
  
  def isBadVersion(self, version, n):
    if version >= n: return True
  
  
def runSolution():
  solution = Solution()
  print(solution.search(n = 5, bad = 4))
  print(solution.search(n = 1, bad = 1))
  pass
runSolution()
