'''

  785. Is Graph Bipartite?

'''


from collections import defaultdict, deque


class Solution:
  def isBipartite(self, graph):
    blues = set()
    reds  = set()
    visited = set()
    
    for i in range(len(graph)):
      if i in visited: continue
      
      queue = deque([(i, 'blue')])  # (node, color)
      visited.add(i)
      
      while queue:
        node, color = queue.popleft()
        
        if color == 'red':
          if node in blues: return False
          if node in reds : continue
        
        if color == 'blue':
          if node in reds : return False
          if node in blues: continue
          
        if color == 'blue': blues.add(node)
        if color == 'red' : reds.add(node)
        visited.add(node)
        
        for next in graph[node]:
          nextColor = 'red' if color == 'blue' else 'blue'
          queue.append((next, nextColor))
    
    return True
    
      
    
  
def runSolution():
  solution = Solution()
  print(solution.isBipartite(
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]))
  
  print(solution.isBipartite(
    graph = [[1,3],[0,2],[1,3],[0,2]]))
  
  
  '''
  
    0   1
    |
    4---2
    |
    3
    
  
  '''
  print(solution.isBipartite(
    graph = [[4],[],[4],[4],[0,2,3]]))
  
  pass
runSolution()