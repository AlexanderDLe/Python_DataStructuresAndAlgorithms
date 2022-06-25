'''

  1834. Single-Threaded CPU

'''

from heapq import heappush, heappop

class Solution:
  def getOrder(self, tasks):    
    # Mistake: We need to maintain the order of tasks - therefore we 
    # cannot sort and must use a heap to maintain order instead.
    timeHeap = []
    for index, (startTime, duration) in enumerate(tasks):
      heappush(timeHeap, (startTime, duration, index))
      
      
    currTime = timeHeap[0][0]
    durationHeap = []
    result = []
    
    
    while timeHeap or durationHeap:
      while timeHeap and currTime >= timeHeap[0][0]:
        _, duration, index = heappop(timeHeap)
        heappush(durationHeap, (duration, index))
      
      # Mistake: What happens if currTime is less than min of timeHeap?
      # We have to catch up currTime
      if len(durationHeap) == 0:
        startTime, duration, index = heappop(timeHeap)
        currTime = startTime
        heappush(durationHeap, (duration, index))
      
      duration, index = heappop(durationHeap)
      currTime += duration
      result.append(index)
  
  
    return result
  

def runSolution():
  solution = Solution()
  print(solution.getOrder([[1,2],[2,4],[3,2],[4,1]]))
  print(solution.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))
  print(solution.getOrder([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]))
  print(solution.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
  pass
runSolution()
