'''

  1094. Car Pooling

  [passengerCount, start, end]
  
  [2,1,5],[3,3,7] cap = 5
  
  0    1     2    3    4    5    6    7
  |-----------------------------------|
             2              5
           pickup---------dropoff
                  3                   7
                pickup---------------dropoff
              |
              
  Use heap to keep track of earliest dropoff points (end)
  
'''

from collections import Counter
import heapq

class Solution:
  def carPooling(self, trips, capacity):
    minHeap = []
    currPas = 0
    trips.sort(key=lambda x: x[1])
    
    for passengers, fr, to in trips:
      while minHeap and minHeap[0][0] <= fr:
        currPas -= minHeap[0][1]
        heapq.heappop(minHeap)
      
      currPas += passengers
      if currPas > capacity: return False
      
      heapq.heappush(minHeap, (to, passengers))
    
    return True

  
def runSolution():
  solution = Solution()
  print(solution.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
  print(solution.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))
  pass
runSolution()