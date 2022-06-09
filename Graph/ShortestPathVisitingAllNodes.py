'''

  847. Shortest Path Visiting All Nodes
  https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/178744/Python-BFS-solution-with-optimization.-Beats-100

'''

from collections import defaultdict, deque


class Solution:
  def shortestPathLength(self, graph):
    n = len(graph)
    masks = [1 << i for i in range(n)]
    allVisited = (1 << n) - 1
    queue = deque([(i, masks[i]) for i in range(n)])
    visitedStates = [{masks[i]} for i in range(n)]
    steps = 0
    print(masks, allVisited)
    print(visitedStates)

    while queue:
      for _ in range(len(queue)):
        currentNode, visited = queue.popleft()
        if visited == allVisited: return steps

        for nb in graph[currentNode]:
          newVisited = visited | masks[nb]
          
          if newVisited not in visitedStates[nb]:
            visitedStates[nb].add(newVisited)
            queue.append((nb, newVisited))

      steps += 1
    
    return -1
      
    
  
def runSolution():
  solution = Solution()
  print(solution.shortestPathLength(
    graph = [[1,2,3],[0],[0],[0]]))
  
  # print(solution.shortestPathLength(
  #   graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]))
  
  pass
runSolution()