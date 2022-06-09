'''

  Was asked during screening.
  
  It's like desgin an algorithm to output matches schedule between teams from different schools.
  Need to make sure each team has a one game to paly and with a team from a different school.

  For eg:

  School A has team [A1,A2]
  School B has team [B1,B2, B3]
  School C has team [C1]
  
  Input: [[A1,A2], [B1,B2, B3], [C1]]
  Output one valid match schedule for one round is acceptable:
  [[A1,B1],[A2,B2],[B3,C1]]

  What's the best algorithm for this? Any equivalent Leetcode problems?
'''

import heapq


class MaxNode:
  def __init__(self, teams):
    self.teams = teams
  def __repr__(self):
    return f'n:{len(self.teams)}'
  def __lt__(self, other):
    return len(self.teams) > len(other.teams)

class Solution:
  def func(self, teams):
    maxHeap = []
    for team in teams:
      heapq.heappush(maxHeap, MaxNode(team))
      
    result = []
    
    while maxHeap:
      res = []
      firstTeam = heapq.heappop(maxHeap).teams
      res.append(firstTeam.pop())
      
      if not maxHeap: return []
      secondTeam = heapq.heappop(maxHeap).teams
      res.append(secondTeam.pop())
      
      if firstTeam: heapq.heappush(maxHeap, MaxNode(firstTeam))
      if secondTeam: heapq.heappush(maxHeap, MaxNode(secondTeam))
      
      result.append(res)
    
    return result
  
def runSolution():
  solution = Solution()
  print(solution.func(teams = [['A1','A2'], ['B1','B2','B3'], ['C1']]))
  pass
runSolution()