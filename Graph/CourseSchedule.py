'''

  207. Course Schedule

'''

from collections import Counter, defaultdict, deque
from itertools import product


class Solution:
  def canFinish(self, numCourses, prerequisites):
    parents, inDegrees, queue = self.init(numCourses, prerequisites)
    
    count = 0
    
    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        count += 1
        if node not in parents: continue
        
        for child in parents[node]:
          inDegrees[child] -= 1
          if inDegrees[child] == 0:
            queue.append(child)
    
    return count == numCourses
  
  
  
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
  
  print(solution.canFinish(
    numCourses = 2, prerequisites = [[1,0]]))
  print(solution.canFinish(
    numCourses = 2, prerequisites = [[1,0],[0,1]]))
  pass
runSolution()