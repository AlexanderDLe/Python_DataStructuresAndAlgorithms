'''

  399. Evaluate Division

'''


from collections import defaultdict, deque


class SolutionRef:
  def calcEquation(self, equations, values, queries):
    graph = self.buildGraph(equations, values)
    result = []
    
    for src, dst in queries:
      if src not in graph or dst not in graph:
        result.append(-1.0)
        continue
      
      q = deque([(src, 1.0)])
      visited = set()
      
      while q:
        node, currProduct = q.popleft()
        if node == dst: 
          result.append(currProduct)
          break
        
        visited.add(node)
        for neighbor, value in graph[node]:
          if neighbor not in visited:
            q.append((neighbor, currProduct * value))
    
    return result
    
  
  def buildGraph(self, equations, values):
    graph = defaultdict(list)
    
    for vertices, value in zip(equations, values):
      x, y = vertices
      graph[x].append((y, value))
      graph[y].append((x, 1/value))
    
    return graph
      
class Solution:
  def calcEquation(self, equations, values, queries):
    graph = self.buildGraph(equations, values)
    result = [-1] * len(queries)
    
    for i, (x, y) in enumerate(queries):
      if x not in graph or y not in graph: continue
      
      seen = set([x])
      queue = deque([(x, 1)])
      
      while queue:
        node, val = queue.popleft()
        if node == y: 
          result[i] = val
          break
        
        for next, nextVal in graph[node]:
          if next in seen: continue
          seen.add(next)
          queue.append((next, val * nextVal))
    
    return result
  
  def buildGraph(self, equations, values):
    graph = defaultdict(list)
    for (x, y), val in zip(equations, values):
      graph[x].append((y, val))
      graph[y].append((x, 1/val))
    return graph
      
    
  
def runSolution():
  solution = Solution()
  print(solution.calcEquation(
    equations = [["a","b"],["b","c"]], 
    values = [2.0,3.0], 
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
  
  print(solution.calcEquation(
    equations = [["a","b"],["b","c"],["bc","cd"]], 
    values = [1.5,2.5,5.0], 
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
  
  print(solution.calcEquation(
    equations = [["a","b"]], 
    values = [0.5], 
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))
  pass
runSolution()