'''

  57. Insert Interval

'''

class Solution:
  def insert(self, intervals, newInterval):
    result = []
    n = len(intervals)
    i = 0
    
    while i < n and newInterval[0] > intervals[i][1]:
      result.append(intervals[i])
      i += 1
      
    # Merge
    prev = newInterval
    while i < n and intervals[i][0] <= prev[1]:
      prev[0] = min(prev[0], intervals[i][0])
      prev[1] = max(prev[1], intervals[i][1])
      i += 1
    result.append(prev)
    
    while i < n:
      result.append(intervals[i])
      i += 1
    
    return result
  
def runSolution():
  solution = Solution()
  print(solution.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
  print(solution.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
  pass
runSolution()