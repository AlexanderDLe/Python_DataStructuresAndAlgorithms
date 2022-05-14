'''

  210. Course Schedule II

'''

from collections import Counter, defaultdict, deque
from itertools import product


class Solution:
  def findOrder(self, numCourses, prerequisites):
    parents, inDegrees, queue = self.init(numCourses, prerequisites)
    
    result = []
    
    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        result.append(node)
        if node not in parents: continue
        
        for child in parents[node]:
          inDegrees[child] -= 1
          if inDegrees[child] == 0:
            queue.append(child)
    
    return result if len(result) == numCourses else []
  
  
  
  def init(self, numCourses, prerequisites):
    parents, inDegrees = defaultdict(list), Counter()
    sources = set([i for i in range(numCourses)])
    
    for child, parent in prerequisites:
      sources.discard(child)
      parents[parent].append(child)
      inDegrees[child] += 1
      
    return parents, inDegrees, deque(list(sources))


  
def runSolution():
  solution = Solution()
  
  print(solution.findOrder(
    numCourses = 2, prerequisites = [[1,0]]))
  print(solution.findOrder(
    numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
  print(solution.findOrder(
    numCourses = 2, prerequisites = [[1,0],[0,1]]))
  pass
runSolution()