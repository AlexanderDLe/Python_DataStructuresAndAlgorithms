'''

  490. The Maze

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
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], 
    start = [0,4], 
    destination = [4,4]))
  
  print(solution.calcEquation(
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], 
    start = [0,4], 
    destination = [3,2]))
  pass
runSolution()