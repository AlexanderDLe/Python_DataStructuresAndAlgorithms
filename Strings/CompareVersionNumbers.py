'''

  1554. Strings Differ by One Character
  
'''

class Solution:
  def compareVersion(self, version1, version2):
    version1 = list(map(lambda x: int(x), version1.split('.')))
    version2 = list(map(lambda x: int(x), version2.split('.')))
    
    n1, n2 = len(version1), len(version2)
    n = n1 if n1 > n2 else n2
    
    for i in range(n):
      v1 = version1[i] if i < n1 else 0
      v2 = version2[i] if i < n2 else 0
      
      if   v1 < v2: return -1
      elif v1 > v2: return 1
    
    return 0
  
def runSolution():
  solution = Solution()
  print(solution.compareVersion(version1 = "1.01", version2 = "1.001"))
  print(solution.compareVersion(version1 = "1.0", version2 = "1.0.0"))
  print(solution.compareVersion(version1 = "0.1", version2 = "1.1"))
  print(solution.compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))
  pass
runSolution()
