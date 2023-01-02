'''

  310. Minimum Height Trees

'''

from collections import defaultdict, deque


class Solution:
  def findMinHeightTrees(self, n, edges):
    if n == 1: return [0]
    
    inDegrees, graph, sources = self.init(n, edges)
    prevQ = []
    queue = deque(sources)
    seen  = set(queue)
    
    while queue:
      prevQ = list(queue)
      
      for _ in range(len(queue)):
        node = queue.popleft()
        
        for child in graph[node]:
          inDegrees[child] -= 1
          if inDegrees[child] <= 1 and child not in seen:
            seen.add(child)
            queue.append(child)
      
    return prevQ
    
    
  def init(self, n, relations):
    inDegrees = defaultdict(int)
    graph = defaultdict(list)
    sources = set()
    
    for nodeA, nodeB in relations:
      inDegrees[nodeA] += 1
      inDegrees[nodeB] += 1
      graph[nodeA].append(nodeB)
      graph[nodeB].append(nodeA)
      
    for node in range(n):
      if inDegrees[node] == 1: 
        sources.add(node)
        inDegrees[node] -= 1
        
    return inDegrees, graph, sources
      
    
  

def runSolution():
  solution = Solution()
  print(solution.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
  print(solution.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))
  pass
runSolution()