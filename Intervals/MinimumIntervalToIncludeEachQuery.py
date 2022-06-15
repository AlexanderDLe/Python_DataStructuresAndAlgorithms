'''

  1851. Minimum Interval to Include Each Query

'''
import heapq

class Node:
  def __init__(self, start, end):
    self.size  = end - start + 1
    self.start = start
    self.end   = end
  def __lt__(self, other):
    return self.size < other.size

class SolutionBruteForce:
  def minInterval(self, intervals, queries):
    minHeap = []
    
    for start, end in intervals:
      heapq.heappush(minHeap, Node(start, end))
    
    result = []
    for query in queries:
      heapCopy = minHeap.copy()
      res = -1
      
      while heapCopy:
        node = heapq.heappop(heapCopy)
        start, end = node.start, node.end
        
        if start <= query <= end:
          res = end - start + 1
          break
          
      result.append(res)
    
    return result
    
class SolutionRef:
  def minInterval(self, intervals, queries):
    intervals.sort()
    sortedQueries = sorted(enumerate(queries), key=lambda x: x[1])
    
    print('i: ', intervals)
    print('s: ', sortedQueries)
    
    res = [-1] * len(queries)
    activeIntervals = []
    
    for origIndex, point in sortedQueries:
      while activeIntervals and activeIntervals[0][1] < point:
        heapq.heappop(activeIntervals)
       
      while intervals and intervals[0][0] <= point:
        start, end = intervals.pop(0)
        
        if end >= point:
          heapq.heappush(activeIntervals, (end - start + 1, end))
      
      if activeIntervals:
        res[origIndex] = activeIntervals[0][0]
    
    return res

class QueryNode:
  def __init__(self, start, end):
    self.start = start
    self.end = end
  def __lt__(self, other):
    if self.end == other.end: return self.start < other.start
    return self.end < other.end

class Solution:
  def minInterval(self, intervals, queries):
    n = len(queries)
    intervals.sort()
    sortedQueries = sorted(enumerate(queries), key=lambda x: x[1])
    result = [-1] * n
    activeIntervals = []
    
    for index, point in sortedQueries:
      while activeIntervals and activeIntervals[0][1] < point:
        heapq.heappop(activeIntervals)
      
      while intervals and intervals[0][0] <= point:
        start, end = intervals.pop(0)
        
        if end >= point:
          heapq.heappush(activeIntervals, (end - start + 1, end))
          
      if activeIntervals:
        result[index] = activeIntervals[0][0]
      
    return result
    
    
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))
  print(solution.minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]))
  pass
runSolution()