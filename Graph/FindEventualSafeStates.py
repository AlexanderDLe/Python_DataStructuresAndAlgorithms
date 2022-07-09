'''

  802. Find Eventual Safe States

'''


from collections import defaultdict, deque


class SolutionRef:
  def eventualSafeNodes(self, graph):
    UNVISITED, VISTING, SAFE = 0, 1, 2
    state = defaultdict(lambda: UNVISITED)
    
    def DFS(node):
      state[node] = VISTING
      
      for next in graph[node]:
        if state[next] == VISTING: return True
        if state[next] == UNVISITED and DFS(next): return True
        
      state[node] = SAFE
      return False
    
    result = []
    for node in range(len(graph)):
      if state[node] == UNVISITED: DFS(node)
      if state[node] == SAFE: result.append(node)
    
    return result
    
class Solution:
  def eventualSafeNodes(self, graph):
    UNVISITED, VISITING, SAFE = 0, 1, 2
    state = defaultdict(lambda: UNVISITED)
    
    def DFS(node):
      state[node] = VISITING
      
      for next in graph[node]:
        if state[next] == VISITING: return True
        if state[next] == UNVISITED and DFS(next): return True
      
      state[node] = SAFE
      return False
    
    result = []
    for node in range(len(graph)):
      if state[node] == UNVISITED: DFS(node)
      if state[node] == SAFE     : result.append(node)
    
    return result
    
  
def runSolution():
  solution = Solution()
  print(solution.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))
  print(solution.eventualSafeNodes(graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]))
  print(solution.eventualSafeNodes(graph = [[],[0,2,3,4],[3],[4],[]]))
  pass
runSolution()