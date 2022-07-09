'''

  1319. Number of Operations to Make Network Connected

'''


from collections import deque

class UnionFind:
  def __init__(self, n):
    self.parents = {i:i for i in range(n)}
    
  def find(self, x):
    if x != self.parents[x]:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]
  
  def union(self, x, y):
    xRoot, yRoot = self.find(x), self.find(y)
    if xRoot != yRoot: self.parents[xRoot] = yRoot
    
    

class Solution:
  def makeConnected(self, n, connections):
    if n == 0: return 0
    connected = 1
    
    UF = UnionFind(n)
    reconnections = 0
    
    for nodeA, nodeB in connections:
      rootA, rootB = UF.find(nodeA), UF.find(nodeB)
      
      if rootA == rootB: 
        reconnections += 1
      else:
        UF.union(nodeA, nodeB)
        connected += 1
      
    if connected + reconnections < n: return -1
    
    # We take the minimum of n - 1 vs reconnections
    # Because there may be more reconnections than extraneous nodes
    return min(n - connected, reconnections)
    

  
def runSolution():
  solution = Solution()
  print(solution.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))
  print(solution.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))
  print(solution.makeConnected(12,[
    [1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]
  ]))
  pass
runSolution()