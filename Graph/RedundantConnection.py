'''

  684. Redundant Connection

'''

from collections import Counter, defaultdict, deque
from itertools import product


class SolutionRef:
  def findRedundantConnection1(self, edges):
    parents = [i for i in range(len(edges) + 1)]
    
    def find(node):
      if node != parents[node]: 
        parents[node] = find(parents[node])
      return parents[node]

    def union(nodeA, nodeB):
      parents[find(nodeA)] = parents[nodeB]
      
    for a, b in edges:
      if find(a) == find(b): return [a, b]
      else: union(a, b)
  
  def findRedundantConnection2(self, edges):
    parents = {v:-1 for v in range(1, len(edges) + 1)}
    
    def find(node):
      if parents[node] != -1:
        parents[node] = find(parents[node])
        return parents[node]
      
      else:
        return node
    
    def union(nodeA, nodeB):
      parentA = find(nodeA)
      parentB = find(nodeB)
      
      if parentA == parentB:
        return True
      
      else:
        parents[parentA] = parentB
        return False
    
    
    for nodeA, nodeB in edges:
      if union(nodeA, nodeB): return [nodeA, nodeB]
      
class Solution1:
  def findRedundantConnection(self, edges):
    parents = {i:i for i in range(1, len(edges) + 1)}
    
    def getRoot(node):
      if node != parents[node]:
        parents[node] = getRoot(parents[node])
      return parents[node]
  
    def union(nodeA, nodeB):
      rootA = getRoot(nodeA)
      rootB = getRoot(nodeB)
      parents[rootA] = rootB
        
    for nodeA, nodeB in edges:
      if getRoot(nodeA) == getRoot(nodeB): return [nodeA, nodeB]
      else: union(nodeA, nodeB)

class Solution:
  def findRedundantConnection(self, edges):
    graph = {i:i for i in range(1, len(edges) + 1)}
    
    def find(node):
      if node != graph[node]:
        graph[node] = find(graph[node])
      return graph[node]
  
    def union(nodeA, nodeB):
      graph[find(nodeA)] = find(nodeB)
    
    for nodeA, nodeB in edges:
      if find(nodeA) == find(nodeB): return [nodeA, nodeB]
      else: union(nodeA, nodeB)
    
    return []
    
    
    
  


  
def runSolution():
  solution = Solution()
  
  print(solution.findRedundantConnection(
    edges = [[1,2],[1,3],[2,3]]))
  print(solution.findRedundantConnection(
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))
  pass
runSolution()