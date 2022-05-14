'''

  323. Number of Connected Components in an Undirected Graph

'''

from collections import defaultdict

class Solution:
  def countComponents(self, n, edges):
    self.relations = defaultdict(list)
    
    for nodeA, nodeB in edges:
      self.relations[nodeA].append(nodeB)
      self.relations[nodeB].append(nodeA)
    
    count = 0
    self.seen = set()

    for node in range(n):
      if node in self.seen: continue
      count += 1
      self.DFS(node)
      
    return count
  
  def DFS(self, node):
    if node in self.seen: return
    self.seen.add(node)
    
    for next in self.relations[node]:
      self.DFS(next)
    
    
    
    
  
  


  
def runSolution():
  solution = Solution()
  
  print(solution.countComponents(
    n = 5, edges = [[0,1],[1,2],[3,4]]))
  print(solution.countComponents(
    n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]))
  pass
runSolution()