'''

  399. Evaluate Division

'''


from collections import defaultdict, deque


class Solution:
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