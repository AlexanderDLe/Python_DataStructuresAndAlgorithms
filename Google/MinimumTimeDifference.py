'''

  539. Minimum Time Difference

'''

class SolutionRef:
  def findMinDifference(self, timePoints):
    if len(timePoints) < 2: return 0
    
    def convertToMins(time):
      hr, min = time.split(':')
      return int(hr) * 60 + int(min)
    
    timePoints.sort()
    minutes = list(map(convertToMins, timePoints))
    minutes.insert(0, minutes[-1] - (24 * 60))
    
    minDiff = float('inf')
    for i in range(1, len(minutes)):
      prev, curr = minutes[i - 1], minutes[i]
      minDiff = min(minDiff, abs(curr - prev))
      
    return minDiff
    

class Solution:
  def findMinDifference(self, timePoints):
    marks = [False] * (24 * 60)
    
    for time in timePoints:
      h, m = time.split(':')
      h, m = int(h), int(m)
      if marks[h * 60 + m]: return 0
      marks[h * 60 + m] = True
      
    prev = 0
    minVal = float('inf')
    first, last = float('inf'), float('-inf')
    
    for i in range(24 * 60):
      if not marks[i]: continue
      
      if first != float('inf'):
        minVal = min(minVal, i - prev)
      
      first = min(first, i)
      last  = max(last, i)
      prev  = i
    
    minVal = min(minVal, (24*60 - last + first))
    print(first, last)
    return minVal
        

      
      
    
    
  
def runSolution():
  solution = Solution()
  print(solution.findMinDifference(timePoints = ["23:59","00:00"]))
  print(solution.findMinDifference(timePoints = ["00:00","23:59","00:00"]))
  print(solution.findMinDifference(timePoints = ['10:00', '15:32', '11:41']))
  pass
runSolution()