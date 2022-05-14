'''

  743. Network Delay Time

'''

from collections import defaultdict, deque
import heapq


class Solution1:
  def networkDelayTime(self, times, n, k):
    graph = self.buildGraph(times)
    seen = set()
    minHeap = [(0, k)]  # (time, node)
    nodesReached = 0
    
    while minHeap:
      time, node = heapq.heappop(minHeap)
      if node in seen: continue
      seen.add(node)
      
      nodesReached += 1
      if nodesReached == n: return time
      
      for nextTime, dest in graph[node]:
        if dest in seen: continue
        heapq.heappush(minHeap, (time + nextTime, dest))
    
    return -1

  def buildGraph(self, times):
    times.sort(key=lambda x: x[2])
    graph = defaultdict(list)
    for src, dest, time in times:
      graph[src].append((time, dest))
    return graph
  
class Solution:
  def networkDelayTime(self, times, n, k):
    graph = self.buildGraph(times)
    seen  = set()
    heap  = [(0, k)]
    nodesReached = 0
    
    while heap:
      time, src = heapq.heappop(heap)
      if src in seen: continue
      seen.add(src)
      
      nodesReached += 1
      if nodesReached == n: return time
      
      for timeCost, dst in graph[src]:
        if dst in seen: continue
        heapq.heappush(heap, (time + timeCost, dst))
    
    return -1
  
  def buildGraph(self, times):
    # times.sort(key=lambda x: x[2])
    graph = defaultdict(list)
    for src, dst, time in times:
      graph[src].append((time, dst))
    return graph

  
def runSolution():
  solution = Solution()
  
  print(solution.networkDelayTime(
    times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]], n = 3, k = 1))
  print(solution.networkDelayTime(
    times = [[1,2,1],[2,3,2],[1,3,4]], n = 3, k = 1))
  print(solution.networkDelayTime(
    times = [[1,2,4]], n = 2, k = 1))
  print(solution.networkDelayTime(
    times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
  print(solution.networkDelayTime(
    times = [[1,2,1]], n = 2, k = 1))
  print(solution.networkDelayTime(
    times = [[1,2,1]], n = 2, k = 2))
  pass
runSolution()