'''

  621. Task Scheduler

'''

from collections import Counter
import heapq

class Node:
  def __init__(self, freq):
    self.freq = freq
  def __repr__(self):
    return f'({self.freq})'
  def __lt__(self, other):
    return self.freq > other.freq

class Solution:
  def leastInterval(self, tasks, n):
    freqDict = Counter(tasks)
    
    heap = []
    for key in freqDict:
      heapq.heappush(heap, Node(freqDict[key]))
    
    queue = []
    cycles = 0
    while heap or queue:
      if heap:
        freq = heapq.heappop(heap).freq
        freq -= 1
        if freq > 0: queue.append((cycles + n, freq))
        
      if queue and queue[0][0] <= cycles:
        heapq.heappush(heap, Node(queue.pop(0)[1]))
      
      cycles += 1
    
    return cycles
    

  
def runSolution():
  solution = Solution()
  print(solution.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
  print(solution.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
  pass
runSolution()