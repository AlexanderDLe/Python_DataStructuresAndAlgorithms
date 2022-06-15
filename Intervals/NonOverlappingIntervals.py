'''

  435. Non-overlapping Intervals

'''

import heapq


class Node:
  def __init__(self, val):
    self.val = val
  def __lt__(self, other):
    return self.val > other.val

class Solution:
  def eraseOverlapIntervals(self, intervals):
    # Need to sort by interval end because that's the primary comparison
    intervals.sort(key=lambda x: x[1])
    maxHeap = []
    removals = 0
    
    for start, end in intervals:
      if maxHeap and start < maxHeap[0].val:
        removals += 1
      else:
        heapq.heappush(maxHeap, Node(end))
    
    return removals
  
def runSolution():
  solution = Solution()
  print(solution.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],
                                        [58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))
  print(solution.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
  print(solution.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
  print(solution.eraseOverlapIntervals(intervals = [[1,2],[2,3]]))
  pass
runSolution()