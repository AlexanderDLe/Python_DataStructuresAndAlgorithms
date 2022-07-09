'''

  1129. Shortest Path with Alternating Colors

'''


from collections import defaultdict, deque


class Solution:
  def shortestAlternatingPaths(self, n, redEdges, blueEdges):
    RED, BLUE = 'RED', 'BLUE'
    redGraph, blueGraph = self.buildGraph(redEdges, blueEdges)
    graph = {RED: redGraph, BLUE: blueGraph}
    result = [-1] * n
    
    def BFS(destination):
      distance = 0  
      init = [(0, RED), (0, BLUE)]    
      queue = deque(init)
      visited = set(init)
      
      while queue:
        for _ in range(len(queue)):
          node, color = queue.popleft()
          nextColor = BLUE if color == RED else RED
          
          if node == destination:
            result[destination] = distance
            return
          
          colorGraph = graph[color]
          if node not in colorGraph: continue
          
          for next in colorGraph[node]:
            if (next, nextColor) in visited: continue
            visited.add((next, nextColor))
            queue.append((next, nextColor))
      
        distance += 1
    
    for destination in range(n):
      BFS(destination)
    
    return result
    
    
  
  def buildGraph(self, redEdges, blueEdges):
    redGraph = defaultdict(list)
    blueGraph = defaultdict(list)
    
    for src, dst in redEdges:
      redGraph[src].append(dst)
    for src, dst in blueEdges:
      blueGraph[src].append(dst)
    
    return redGraph, blueGraph
    
    
  
def runSolution():
  solution = Solution()
  print(solution.shortestAlternatingPaths(n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))
  print(solution.shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]))
  pass
runSolution()