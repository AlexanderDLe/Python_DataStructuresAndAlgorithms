'''

  256. Paint House

'''

from itertools import groupby


class Solution:
  def minCost(self, costs):
    redCost, blueCost, greenCost = costs[0]
    
    for i in range(1, len(costs)):
      redTemp, blueTemp, greenTemp = redCost, blueCost, greenCost      
      red, blue, green = costs[i]
      
      redCost = red + min(blueTemp, greenTemp)
      blueCost = blue + min(redTemp, greenTemp)
      greenCost = green + min(redTemp, blueTemp)
    
    return min(redCost, blueCost, greenCost)
  

def runSolution():
  solution = Solution()
  print(solution.minCost(costs = [[17,2,17],[16,16,5],[14,3,19]]))
  print(solution.minCost(costs = [[7,6,2]]))
  pass
runSolution()