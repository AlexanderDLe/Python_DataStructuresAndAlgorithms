'''

  96. Unique Binary Search Trees

'''

class Solution:  
  def numTrees(self, n):
    DP = {0: 1, 1:1, 2:2}
    
    def DFS(num):
      if num in DP: return DP[num]
      res = 0
      
      for i in range(num):
        res += DFS(i) * DFS(num - i - 1)
      
      DP[num] = res
      return res
    
    return DFS(n)
    
  
def runSolution():
  solution = Solution()
  print(solution.numTrees(n = 3))
  print(solution.numTrees(n = 1))
  pass
runSolution()