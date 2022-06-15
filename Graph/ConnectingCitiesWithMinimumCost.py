'''

  1135. Connecting Cities With Minimum Cost

'''

from collections import defaultdict, deque
import heapq


class Solution:
  def minimumCost(self, n, connections):
    graph = self.buildGraph(connections)
    minHeap = [(0, 1)]
    seen = set()
    cost = 0
    
    while minHeap:
      distance, node = heapq.heappop(minHeap)
      if node in seen: continue
      
      seen.add(node)
      cost += distance
      if n == len(seen): return cost
      
      for nextDistance, nextNode in graph[node]:
        if nextNode in seen: continue
        heapq.heappush(minHeap, (nextDistance, nextNode))
    
    return -1

  def buildGraph(self, connections):
    connections.sort(key=lambda x: x[2])
    graph = defaultdict(list)
    for u, v, distance in connections:
      graph[u].append((distance, v))
      graph[v].append((distance, u))
    return graph

  
def runSolution():
  solution = Solution()
  
  print(solution.minimumCost(
    n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]))
  print(solution.minimumCost(
    n = 4, connections = [[1,2,3],[3,4,4]]))
  pass
runSolution()