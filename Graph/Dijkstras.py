'''

  841. Keys and Rooms

'''


from heapq import heapify, heappop, heappush


class Solution:
  def Dijkstras(self, start, edges):
    n = len(edges)
    minDistances = [float('inf')] * n
    minDistances[start] = 0
    
    minHeap = [(0, start)]
    visited = set()
    
    while minHeap:
      currentMinDistance, vertex = heappop(minHeap)
      if currentMinDistance == float('inf'): break
      if vertex in visited: continue
      visited.add(vertex)
      
      for nextVertex, distanceToNext in edges[vertex]:
        prevDistance = minDistances[nextVertex]
        totalDistance = currentMinDistance + distanceToNext
        minDistance = min(prevDistance, totalDistance)
        minDistances[nextVertex] = minDistance
        
        heappush(minHeap, (minDistance, nextVertex))
      
    return list(map(lambda x: x if x != float('inf') else -1, minDistances))

    
    
  
def runSolution():
  solution = Solution()
  print(solution.Dijkstras(
    start = 0, 
    edges = [
      [[1, 7]],
      [[2, 6], [3, 20], [4, 3]],
      [[3, 14]],
      [[4, 2]],
      [],
      [],
  ]))
  pass
runSolution()