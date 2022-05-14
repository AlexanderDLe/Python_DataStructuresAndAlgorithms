'''

  253. Meeting Rooms II

  ------------------
    ----     ----
  |
'''

import heapq

class Solution:
  def minMeetingRooms(self, intervals):
    intervals.sort()
    roomsRequired = 0
    minHeap = []
    
    for i in range(len(intervals)):
      curr = intervals[i]
      
      while minHeap and curr[0] >= minHeap[0]:
        heapq.heappop(minHeap)
      
      heapq.heappush(minHeap, curr[1])
      roomsRequired = max(roomsRequired, len(minHeap))
    
    return roomsRequired
  
def runSolution():
  solution = Solution()
  print(solution.minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))
  print(solution.minMeetingRooms(intervals = [[7,10],[2,4]]))
  print(solution.minMeetingRooms(intervals = [[13,15],[1,13]]))
  pass
runSolution()