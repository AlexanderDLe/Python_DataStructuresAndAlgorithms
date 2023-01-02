'''

  56. Merge Intervals

'''

class SolutionRef:
  def merge(self, intervals):
    intervals.sort()
    result = []
    
    prev = intervals[0]
    for i in range(1, len(intervals)):
      curr = intervals[i]
      
      if curr[0] > prev[1]:
        result.append(prev)
        prev = curr
      else:
        prev[1] = max(prev[1], curr[1])
    
    result.append(prev)
    return result

class Solution:
  
  '''
  
    Time Complexity
    O(n) Iterate through intervals
    
    Space Complexity
    O(n) Result array
  
  '''
  
  def merge(self, intervals):
    intervals.sort()
    result = []
    prev = intervals[0]
    
    for i in range(1, len(intervals)):
      curr = intervals[i]
      
      if curr[0] <= prev[1]:
        prev[1] = max(prev[1], curr[1])
      else:
        result.append(prev)
        prev = curr
    
    result.append(prev)
    
    return result
    
  
def runSolution():
  solution = Solution()
  print(solution.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
  print(solution.merge(intervals = [[1,4],[4,5]]))
  pass
runSolution()