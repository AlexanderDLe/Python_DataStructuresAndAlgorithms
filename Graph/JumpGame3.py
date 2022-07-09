'''

  AlgoExpert A Star

'''

from collections import deque
from heapq import heappop, heappush


class Solution:
  def canReach(self, arr, start):
    n = len(arr)
    queue = deque([start])
    visited = set([start])
    
    while queue:
      index = queue.popleft()
      val = arr[index]
      
      if val == 0: return True
      
      forw = index + val
      back = index - val
      
      if forw < n and forw not in visited:
        queue.append(forw)
        visited.add(forw)
      
      if back > -1 and back not in visited:
        queue.append(back)
        visited.add(forw)
    
    return False
    
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.canReach(arr = [4,2,3,0,3,1,2], start = 5))
  print(solution.canReach(arr = [4,2,3,0,3,1,2], start = 0))
  print(solution.canReach(arr = [3,0,2,1,2], start = 2))
  pass
runSolution()