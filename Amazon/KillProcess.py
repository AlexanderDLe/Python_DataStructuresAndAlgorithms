'''

  582. Kill Process

'''

from collections import defaultdict, deque


class Solution:
  def killProcess(self, pid, ppid, kill):
    if kill == 0: return pid
    
    parentToChildren = self.buildParentToChildren(pid, ppid)
    result = []
    queue  = deque([kill])
    
    while queue:
      for _ in range(len(queue)):
        id = queue.popleft()
        result.append(id)
        
        children = parentToChildren[id]
        queue.extend(children)
    
    return result

  def buildParentToChildren(self, pid, ppid):
    parentToChildren = defaultdict(list)
    
    for child, parent in zip(pid, ppid):
      parentToChildren[parent].append(child)
    
    return parentToChildren  
  
  
def runSolution():  
  solution = Solution()
  print(solution.killProcess(pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5))
  print(solution.killProcess(pid = [1], ppid = [0], kill = 1))
runSolution()