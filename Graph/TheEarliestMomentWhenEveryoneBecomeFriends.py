'''

  1101. The Earliest Moment When Everyone Become Friends

'''


class Solution:
  def earliestAcq(self, logs, n):
    parents = {i:i for i in range(n)}
    count = n
    
    def find(x):
      if x != parents[x]:
        parents[x] = find(parents[x])
      return parents[x]
    
    def union(x, y):
      xRoot, yRoot = find(x), find(y)
      parents[xRoot] = yRoot
      
    logs.sort()
    
    for time, x, y in logs:
      if find(x) != find(y):
        count -= 1
        union(x, y)
      
      if count == 1: return time
    
    return -1
    
  
def runSolution():
  solution = Solution()
  print(solution.earliestAcq(
    logs = [
      [20190101,0,1],
      [20190104,3,4],
      [20190107,2,3],
      [20190211,1,5],
      [20190224,2,4],
      [20190301,0,3],
      [20190312,1,2],
      [20190322,4,5]], 
    n = 6))
  
  print(solution.earliestAcq(
    logs = [
      [0,2,0],
      [1,0,1],
      [3,0,3],
      [4,1,2],
      [7,3,1]], 
    n = 4))
  
  pass
runSolution()