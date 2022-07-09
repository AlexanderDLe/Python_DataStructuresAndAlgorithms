'''

  767. Reorganize String
  
'''

from collections import Counter
from heapq import heappop, heappush

class Node:
  def __init__(self, char, freq):
    self.char = char
    self.freq = freq
  def __lt__(self, other):
    return self.freq > other.freq

class Solution:
  def reorganizeString(self, s):
    freqMap = Counter(s)
    maxHeap = []
    result  = ''
    queue = []
    
    for char, freq in list(freqMap.items()):
      heappush(maxHeap, Node(char, freq))
  
    while maxHeap:
      node = heappop(maxHeap)
      char, freq = node.char, node.freq
      
      result += char
      freq -= 1
      
      
      if queue: 
        next = queue.pop(0)
        heappush(maxHeap, Node(next[0], next[1]))
        
      if freq > 0: queue.append((char, freq))
        
    if not queue: return result
    return ''
    
  
def runSolution():
  solution = Solution()
  print(solution.reorganizeString('aab'))
  print(solution.reorganizeString('aaab'))
  pass
runSolution()