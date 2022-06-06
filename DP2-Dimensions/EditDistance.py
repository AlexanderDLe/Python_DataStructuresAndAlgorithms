'''

  72. Edit Distance        

'''

class SolutionRef:
  def minDistance(self, word1, word2):
    n1, n2 = len(word1), len(word2)
    DP = {}
    
    def DFS(p1, p2):
      if (p1, p2) in DP: return DP[(p1, p2)]
      if p1 == n1 or p2 == n2:
        return n1 - p1 + n2 - p2
        
      res = float('inf')
      
      if word1[p1] == word2[p2]:
        res = DFS(p1 + 1, p2 + 1)
      else:
        insert  = DFS(p1, p2 + 1)
        delete  = DFS(p1 + 1, p2)
        replace = DFS(p1 + 1, p2 + 1)
        res = 1 + min(insert, delete, replace)
      
      DP[(p1, p2)] = res
      return res
    
    return DFS(0, 0)
    
class Solution:
  def minDistance(self, word1, word2):
    n1, n2 = len(word1), len(word2)
    DP = {}
    
    def DFS(p1, p2):
      if (p1,p2) in DP: return DP[p1, p2]
      if p1 == n1 or p2 == n2:
        return (n1 + n2) - (p1 + p2)

      res = float('inf')
      
      if word1[p1] == word2[p2]:
        res = DFS(p1 + 1, p2 + 1)
      else:
        add = DFS(p1, p2 + 1)
        rem = DFS(p1 + 1, p2)
        rep = DFS(p1 + 1, p2 + 1)
        res = 1 + min(add, rem, rep)
      
      
      DP[p1, p2] = res
      return res
    
    return DFS(0, 0)
    
  
def runSolution():
  solution = Solution()
  print(solution.minDistance(word1 = "horse", word2 = "ros"))
  print(solution.minDistance(word1 = "intention", word2 = "execution"))
  pass
runSolution()