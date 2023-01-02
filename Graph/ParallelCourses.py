'''

  1136. Parallel Courses

'''

from collections import defaultdict, deque


class Solution:
  def minimumSemesters(self, n, relations):
    parents, inDegrees, sources = self.init(n, relations)
    result = 0
    
    queue = deque(list(sources))
    
    while queue:
      result += 1
      
      for _ in range(len(queue)):
        node = queue.popleft()
        n -= 1
        
        if node not in parents: continue
        for child in parents[node]:
          inDegrees[child] -= 1
          if inDegrees[child] == 0: queue.append(child)
    
    return result if n == 0 else -1
    
  
  def init(self, n, relations):
    parents = defaultdict(list)
    inDegrees = defaultdict(int)
    sources = set([i for i in range(1, n + 1)])
    
    for prev, next in relations:
      inDegrees[next] += 1
      sources.discard(next)
      parents[prev].append(next)
    
    return (parents, inDegrees, sources)
    
  

def runSolution():
  solution = Solution()
  print(solution.minimumSemesters(n = 3, relations = [[1,3],[2,3]]))
  print(solution.minimumSemesters(n = 3, relations = [[1,2],[2,3],[3,1]]))
  pass
runSolution()