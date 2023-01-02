'''

  1953. Maximum Number of Weeks for Which You Can Work

  5 5 5 5 5
  2 2 1  
'''

from heapq import heappush, heappop

class Node:
  def __init__(self, project, milestones):
    self.project = project
    self.milestones = milestones
  def __lt__(self, other):
    return self.milestones > other.milestones

class SolutionHeapTooSlow:
  def numberOfWeeks(self, milestones):
    heap = []
    
    for i, milestoneCount in enumerate(milestones):
      heappush(heap, Node(i, milestoneCount))
    
    prevProject = None
    weeks = 0
    
    while heap:
      weeks += 1
      
      node: Node = heappop(heap)
      project, milestoneCount = node.project, node.milestones
      milestoneCount -= 1
      
      
      if prevProject: 
        heappush(heap, Node(prevProject[0], prevProject[1]))
        prevProject = None
      
      if milestoneCount > 0: 
        prevProject = (project, milestoneCount)
    
    
    return weeks

class Solution:
  def numberOfWeeks(self, milestones):
    _sum = sum(milestones)
    _max = max(milestones)
    sumWithoutMax = _sum - _max
    
    if sumWithoutMax >= _max - 1:
      return _sum
    else:
      return 2 * (sumWithoutMax) + 1


def runSolution():
  solution = Solution()
  print(solution.numberOfWeeks(milestones = [1,2,3]))
  print(solution.numberOfWeeks(milestones = [5,3,1]))
  pass
runSolution()