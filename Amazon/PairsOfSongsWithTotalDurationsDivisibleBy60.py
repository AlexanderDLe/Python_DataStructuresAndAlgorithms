'''

  1010. Pairs of Songs With Total Durations Divisible by 60

'''

from collections import Counter


class SolutionRef:
  def numPairsDivisibleBy60(self, time):
    ans, count = 0, Counter()
    for t in time:
      modded = t % 60
      remaining = (60 - modded) % 60
      
      ans += count[remaining]
      count[t % 60] += 1
    
    return ans
      
    
class Solution:
  def numPairsDivisibleBy60(self, time):
    result, counter = 0, Counter()
    
    for t in time:
      moddedTime = t % 60
      remainder  = (60 - moddedTime) % 60
      
      result += counter[remainder]
      counter[moddedTime] += 1
  
    return result
      
      
    
  
  
def runSolution():
  solution = Solution()
  print(solution.numPairsDivisibleBy60([30,20,150,100,40]))
  print(solution.numPairsDivisibleBy60([60,60,60]))
  pass
runSolution()