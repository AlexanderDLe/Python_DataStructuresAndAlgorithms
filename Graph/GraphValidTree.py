'''

  261. Graph Valid Tree

'''

from collections import Counter, defaultdict, deque

class SolutionRef1:
  def validTreeUnionFind(self, n, edges):
    if len(edges) != n - 1: return False
    
    parent = list(range(n))
    
    def find(x):
      if x != parent[x]:
        parent[x] = find(parent[x])
      return parent[x]
    
    def union(x, y):
      rootX, rootY = find(x), find(y)
      if rootX != rootY:
        parent[rootX] = rootY
    
    for x, y in edges:
      union(x, y)
    
    # There should only be 1 root
    return len({find(i) for i in range(n)}) == 1
  
  def validTreeRef(self, n, edges):
    '''
    
      1. If graph is a tree, there should be n-1 edges at MAX,
         otherwise, there is a cycle.
      2. Start at node 0
      3. BFS throughout the graph
      4. If length of seen nodes if equal to n, then pass.
         Otherwise, we can conclude there was a node that
         was not traversed.
    
    '''
    if len(edges) != n - 1: return False
    
    graph = defaultdict(list)
    
    for x, y in edges:
      graph[x].append(y)
      graph[y].append(x)
    
    queue = deque([0])
    seen = set([0])
    
    while queue:
      node = queue.popleft()
      
      for neighbor in graph[node]:
        if neighbor in seen: continue
        seen.add(neighbor)
        queue.append(neighbor)
    
    return len(seen) == n
    
class SolutionRef2:
  def validTree(self, n, edges):
    if len(edges) != n - 1: return False
    
    graph = defaultdict(list)
    for x, y in edges:
      graph[x].append(y)
      graph[y].append(x)
    
    queue = deque([0])
    seen  = set([0])
    
    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        for next in graph[node]:
          if next in seen: continue
          seen.add(next)
          queue.append(next)
        
    
    return len(seen) == n
  
class Solution:
  def validTree(self, n, edges):
    if len(edges) != n - 1: return False
    seen = set([0])
    queue = deque([0])
    graph = self.buildGraph(edges)
    
    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        
        for next in graph[node]:
          if next in seen: continue
          seen.add(next)
          queue.append(next)
    
    return len(seen) == n
  
  def buildGraph(self, edges):
    graph = defaultdict(list)
    for x, y in edges:
      graph[x].append(y)
      graph[y].append(x)
    return graph
  


  
def runSolution():
  solution = Solution()
  
  print(solution.validTree(
    n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]))
  print(solution.validTree(
    n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]))
  pass
runSolution()