'''

  1466. Reorder Routes to Make All Paths Lead to the City Zero

'''


from collections import defaultdict, deque


class Solution:
  def minReorder(self, n, connections):
    graph = self.buildGraph(connections)
    seen = set([0])
    queue = deque([0])
    result = 0
    
    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        
        for next, type in graph[node]:
          if next in seen: continue
          if type == 'outgoing': result += 1
          seen.add(next)
          queue.append(next)
    
    return result
    
  def buildGraph(self, connections):
    graph = defaultdict(list)
    for src, dst in connections:
      graph[src].append((dst, 'outgoing'))
      graph[dst].append((src, 'incoming'))
    return graph
    
  
def runSolution():
  solution = Solution()
  print(solution.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
  print(solution.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))
  print(solution.minReorder(n = 3, connections = [[1,0],[2,0]]))
  pass
runSolution()