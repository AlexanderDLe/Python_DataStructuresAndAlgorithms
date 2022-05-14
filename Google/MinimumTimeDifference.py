'''

  539. Minimum Time Difference

'''

class Solution:
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
    
    
  
def runSolution():
  solution = Solution()
  print(solution.findMinDifference(timePoints = ["23:59","00:00"]))
  print(solution.findMinDifference(timePoints = ["00:00","23:59","00:00"]))
  pass
runSolution()