'''

  2039. The Time When the Network Becomes Idle

'''

from collections import defaultdict, deque
import heapq


class Solution:
  def networkBecomesIdle(self, edges, patience):
    adjList = self.buildGraph(edges)
    
    # BFS to get shortest route from node to master
    shortest = {}
    queue = deque([(0, 0)])
    seen = set()
    
    while queue:
      currPos, currDist = queue.popleft()
      if currPos in seen: continue
      
      seen.add(currPos)
      shortest[currPos] = currDist
      
      for nei in adjList[currPos]:
        queue.append((nei, currDist + 1))
    
    result = 0
    
    for i in range(1, len(patience)):
      resendInterval = patience[i]
      
      # The server will stop sending requests after it's been sent to the master node and back
      timeToCompleteCycle = shortest[i] * 2
      
      # Last second the server can re-request a message
      lastResendSecond = timeToCompleteCycle - 1
      
      # Calculate the last time a packet is actually resent
      totalRequestsSent = lastResendSecond // resendInterval
      lastResentTime = totalRequestsSent * resendInterval
      
      # The last packet still has to go through the entire cycle
      lastPacketTime = lastResentTime + timeToCompleteCycle
      
      result = max(result, lastPacketTime)
    
    return result + 1
      
    
  def buildGraph(self, edges):
    graph = defaultdict(list)
    for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)
    return graph

  
def runSolution():
  solution = Solution()
  print(solution.networkBecomesIdle(edges = [[0,1],[1,2]], patience = [0,2,1]))
  print(solution.networkBecomesIdle(edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]))
  pass
runSolution()