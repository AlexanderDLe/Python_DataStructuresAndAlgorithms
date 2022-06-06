'''

  2158. Amount of New Area Painted Each Day

  [1,4] [4,7] [5,8]
  
  0-0-0-1-1-1-2
  
  X-X-X-X-X-X-X
  ^
  
  
  [0, 0, 0]
'''

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
    n = len(paint)
    records, maxPos = [], 0
    
    for i, (start, end) in enumerate(paint):
      maxPos = max(maxPos, end)
      records.append((start, i, 'START'))
      records.append((end, i, 'END'))
    records.sort()
    
    result = n * [0]
    minHeap, endSet = [], set()
    i = 0
    
    for pos in range(maxPos + 1):
      while i < len(records) and records[i][0] == pos:
        pos, index, type = records[i]
        
        if type == 'START': heapq.heappush(minHeap, index)
        if type == 'END'  : endSet.add(index)
        i += 1
        
      while minHeap and minHeap[0] in endSet: heapq.heappop(minHeap)
      if minHeap: result[minHeap[0]] += 1
    
    return result
  

def runSolution():
  solution = Solution()
  print(solution.amountPainted(paint = [[1,4],[4,7],[5,8]]))
  pass
runSolution()