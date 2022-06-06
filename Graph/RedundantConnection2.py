'''

  685. Redundant Connection II

'''

from collections import Counter, defaultdict, deque

class Solution:
  def findRedundantDirectedConnection(self, edges):
    pass
  
def runSolution():
  solution = Solution()
  
  print(solution.findRedundantDirectedConnection(
    edges = [[1,2],[1,3],[2,3]]))
  print(solution.findRedundantDirectedConnection(
    edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]))
  pass
runSolution()