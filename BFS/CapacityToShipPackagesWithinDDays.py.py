'''

  2162. Minimum Cost to Set Cooking Time

'''

class Solution:
  def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
    def countCost(minutes, seconds):
      print(minutes, seconds)
      time = f'{minutes // 10}{minutes % 10}{seconds // 10}{seconds % 10}'
      time = time.lstrip('0')
      print(time)
      totalCost = 0
      currDigit = str(startAt)
      
      for digit in time:
        if currDigit != digit:
          totalCost += moveCost
          currDigit = digit
          
        totalCost += pushCost
      
      return totalCost
    
    result = float('inf')
    for m in range(100): # Check which [mm:ss] configuration works out
      for s in range(100):
        if m * 60 + s == targetSeconds:
          result = min(result, countCost(m, s))
          
    return result
  
  
def runSolution():
  solution = Solution()
  print(solution.minCostSetTime(startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600))
  print(solution.minCostSetTime(startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76))
  pass
runSolution()
