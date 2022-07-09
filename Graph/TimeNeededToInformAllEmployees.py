'''

  1376. Time Needed to Inform All Employees

'''

from collections import defaultdict


class Solution:
  def numOfMinutes(self, n, headID, manager, informTime):
    graph = self.buildGraph(manager, informTime)
    maxTime = 0
    
    def DFS(node, currTime):
      nonlocal maxTime
      maxTime = max(maxTime, currTime)
      if node not in graph: return
      
      for nextNode, traversalTime in graph[node]:
        DFS(nextNode, currTime + traversalTime)
    
    DFS(headID, informTime[headID])
    return maxTime
  
  def buildGraph(self, manager, informTime):
    graph = defaultdict(list)
    
    for i in range(len(manager)):
      currManager, traversalTime = manager[i], informTime[i]
      graph[currManager].append((i, traversalTime))
    
    return graph

  
def runSolution():
  solution = Solution()
  print(solution.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))
  print(solution.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))
  pass
runSolution()