'''

  2158. Amount of New Area Painted Each Day

  [1,4] [4,7] [5,8]
  
  0-0-0-1-1-1-2
  
  X-X-X-X-X-X-X
  ^
  
  
  [0, 0, 0]
'''

from collections import deque
from heapq import heappush, heappop
import heapq


class SolutionRef:
  def amountPainted(self, paint):
    # Construct the sweep line
    records = []
    maxPos = 0
    
    for i, [start, end] in enumerate(paint):
      records.append((start, i, 'start')) # use 1 and -1 to record the type
      records.append((end, i, 'end'))
      maxPos = max(maxPos, end)
    records.sort()
    
    # Sweep across all positions
    ans = [0] * len(paint)
    indexes = []
    endedSet = set()
    i = 0
    
    print(records)
    for pos in range(maxPos + 1):
      while i < len(records) and records[i][0] == pos:
        pos, index, type = records[i]
        if type == 'start': heapq.heappush(indexes, index)
        else              : endedSet.add(index)
        i += 1
      
      while indexes and indexes[0] in endedSet:
        heapq.heappop(indexes)
        
      if indexes: ans[indexes[0]] += 1
    
    return ans
  
class Solution:
  def amountPainted(self, paint):
    START, END = 'START', 'END'
    endPos = 0
    records = []
    
    for i, (start, end) in enumerate(paint):
      records.append((start, i, START))
      records.append((end, i, END))
      endPos = max(endPos, end)
      
    records.sort()
    result = [0] * len(paint)
    minHeap = []
    ended = set()
    i = 0
    
    for pos in range(endPos + 1):
      while i < len(records) and pos == records[i][0]:
        _, index, type = records[i]
        
        if type == START: heappush(minHeap, index)
        if type == END  : ended.add(index)
        i += 1
      
      while minHeap and minHeap[0] in ended: heappop(minHeap)
      if minHeap: result[minHeap[0]] += 1
      
    return result

def runSolution():
  solution = Solution()
  # print(solution.amountPainted(paint = [[1,4],[4,7],[5,8]]))
  print(solution.amountPainted(paint = [[0,10]]))
  pass
runSolution()