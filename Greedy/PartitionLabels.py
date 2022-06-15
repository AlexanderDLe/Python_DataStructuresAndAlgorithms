'''

  763. Partition Labels
  
'''

from collections import Counter, defaultdict
import heapq

class Solution:
  def partitionLabels(self, s):
    if not s: return 0

    indexes = {char:i for i, char in enumerate(s)}
    prevIndex = 0
    endIndex  = 0
    result = []
    
    for i, char in enumerate(s):
      endIndex = max(endIndex, indexes[char])
      if i == endIndex: 
        result.append(i - prevIndex + 1)
        prevIndex = i + 1
    
    return result
    

def runSolution():
  solution = Solution()
  print(solution.partitionLabels(s = "ababcbacadefegdehijhklij"))
  print(solution.partitionLabels(s = "eccbbbbdec"))
  pass
runSolution()
