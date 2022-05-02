'''

  1010. Pairs of Songs With Total Durations Divisible by 60

'''

from collections import Counter


class Solution:
  def numPairsDivisibleBy60(self, time):
    ans, count = 0, Counter()
    for t in time:
      modded = t % 60
      remaining = (60 - modded) % 60
      
      ans += count[remaining]
      count[t % 60] += 1
    
    return ans
      
    
  
  
def runSolution():
  solution = Solution()
  print(solution.numPairsDivisibleBy60([30,20,150,100,40]))
  print(solution.numPairsDivisibleBy60([60,60,60]))
  pass
runSolution()