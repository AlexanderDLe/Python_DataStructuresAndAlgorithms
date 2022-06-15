'''

  787. Cheapest Flights Within K Stops

'''

from collections import defaultdict
import heapq


class SolutionRef:
  def findCheapestPrice(self, n, flights, src, dst, k):
    prices = [float('inf')] * n
    prices[src] = 0
    
    for i in range(k + 1):
      tempPrices = prices.copy()
      
      for s, d, p in flights:  # source, destination, price
        if prices[s] == float('inf'): 
          continue
        if prices[s] + p < tempPrices[d]:
          tempPrices[d] = prices[s] + p
      
      prices = tempPrices
    
    return -1 if prices[dst] == float('inf') else prices[dst]




class Solution:
  def findCheapestPrice(self, n, flights, src, dst, k):
    prices = [float('inf')] * n
    prices[src] = 0
    
    for _ in range(k + 1):
      temp = prices.copy()
      
      for fr, to, cost in flights:
        if flights[fr] == float('inf'): continue
        temp[to] = min(temp[to], prices[fr] + cost)
      
      prices = temp
      
    return prices[dst] if prices[dst] != float('inf') else -1

  
  
def runSolution():
  solution = Solution()
  
  print(solution.findCheapestPrice(
    n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
  print(solution.findCheapestPrice(
    n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
  pass
runSolution()