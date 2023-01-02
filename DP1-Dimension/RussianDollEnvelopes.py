'''

  354. Russian Doll Envelopes
  
  1. Sort by width then height
  
  [2,3],[5,4],[6,4],[6,5],[6,7]
  start
  
'''

from bisect import bisect_left


class Solution:
  def maxEnvelopes(self, envelopes):
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    print(envelopes)
    LIS = []
    size = 0
    
    for _, height in envelopes:
      # If LIS is empty or height is greater than largest height
      # Then add to LIS
      if not LIS or height > LIS[-1]:
        LIS.append(height)
        size += 1
      # If height is smaller than largest height, then place that height
      # in the correct position in ascending order.
      else:
        index = bisect_left(LIS, height)
        LIS[index] = height
        
      print(LIS)
    return size

def runSolution():  
  solution = Solution()
  print(solution.maxEnvelopes(envelopes = [[5,4],[6,4],[6,7],[6,6],[2,3],[7,1],[8,5], [9,6]]))
  # print(solution.gameOfLife(envelopes = [[1,1],[1,1],[1,1]]))
runSolution()