'''

  1579. Remove Max Number of Edges to Keep Graph Fully Traversable

'''

from collections import Counter, defaultdict, deque

class Solution:
  def maxNumEdgesToRemove(self, n, edges):
    parents = {i:i for i in range(1, n + 1)}
    result = nA = nB = 0
    
    def find(node):
      if node != parents[node]:
        parents[node] = find(parents[node])
      return parents[node]
  
    def union(child, parent):
      cRoot = find(child)
      pRoot = find(parent)
      parents[cRoot] = pRoot
    
    # Shared routes
    for type, x, y in edges:
      if type == 3:
        if find(x) == find(y): 
          result += 1
        else: 
          nA += 1
          nB += 1
          union(x, y)
    
    # Alice's Routes
    parentsCopy = parents.copy()
    for type, x, y in edges:
      if type == 1:
        if find(x) == find(y): 
          result += 1
        else: 
          nA += 1
          union(x, y)
    
    # Bob's Routes
    parents = parentsCopy
    for type, x, y in edges:
      if type == 2:
        if find(x) == find(y): 
          result += 1
        else: 
          nB += 1
          union(x, y)
    
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