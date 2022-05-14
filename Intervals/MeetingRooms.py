'''

  252. Meeting Rooms

'''

import heapq

class Solution:
  def canAttendMeetings(self, intervals):
    intervals.sort()
    
    for i in range(1, len(intervals)):
      prev = intervals[i - 1]
      curr = intervals[i]
      if curr[0] < prev[1]: return False
    
    return True
  
def runSolution():
  solution = Solution()
  print(solution.canAttendMeetings(intervals = [[0,30],[5,10],[15,20]]))
  print(solution.canAttendMeetings(intervals = [[7,10],[2,4]]))
  pass
runSolution()