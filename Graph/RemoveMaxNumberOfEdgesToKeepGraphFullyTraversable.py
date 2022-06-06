'''

  1579. Remove Max Number of Edges to Keep Graph Fully Traversable

'''

from collections import Counter, defaultdict, deque

class Solution:
  def maxNumEdgesToRemove(self, n, edges):
    ufA = {i:i for i in range(1, n + 1)}
    ufB = {i:i for i in range(1, n + 1)}
    result = nA = nB = 0
    
    def find(node, uf):
      if node != uf[node]:
        uf[node] = find(uf[node], uf)
      return uf[node]
  
    def union(child, parent, uf):
      cRoot = find(child, uf)
      pRoot = find(parent, uf)
      uf[cRoot] = pRoot
    
    # Shared routes
    for type, x, y in edges:
      if type == 3:
        if find(x, ufA) == find(y, ufA): 
          result += 1
        else: 
          nA += 1
          union(x, y, ufA)
        
        if find(x, ufB) == find(y, ufB): 
          result += 1
        else: 
          nB += 1
          union(x, y, ufB)
        
    
    # Alice's Routes
    for type, x, y in edges:
      if type == 1:
        if find(x, ufA) == find(y, ufA): 
          result += 1
        else: 
          nA += 1
          union(x, y, ufA)
    
    # Bob's Routes
    for type, x, y in edges:
      if type == 2:
        if find(x, ufB) == find(y, ufB): 
          result += 1
        else: 
          nB += 1
          union(x, y, ufB)
    
    if nA == n - 1 and nB == n - 1: return result
    return -1
      
    
  
def runSolution():
  solution = Solution()
  print(solution.maxNumEdgesToRemove(
    n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
  print(solution.maxNumEdgesToRemove(
    n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
  print(solution.maxNumEdgesToRemove(
    n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))
  pass
runSolution()