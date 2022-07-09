'''

  547. Number of Provinces

'''


from collections import deque


class Solution:
  def findCircleNum(self, isConnected):
    seen = set()
    provinces = 0
    
    def DFS(node):
      if node in seen: return
      seen.add(node)

      for next, valid in enumerate(isConnected[node]):
        if next in seen: continue
        if valid: DFS(next)
    
    for node in range(len(isConnected)):
      if node not in seen:
        DFS(node)
        provinces += 1
      
    return provinces

  
def runSolution():
  solution = Solution()
  print(solution.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
  print(solution.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))
  pass
runSolution()