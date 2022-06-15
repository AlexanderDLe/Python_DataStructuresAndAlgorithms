'''

  1055. Shortest Way to Form String

'''


from bisect import bisect, bisect_left
from collections import defaultdict, deque


class SolutionMyDP:
  def shortestWay(self, source, target):
    DP = {}
    
    def DFS(index):
      if index in DP: return DP[index]
      if index >= len(target): return 0
    
      res = float('inf')
      add = 0
      
      for char in source:
        if index + add < len(target) and char == target[index + add]:
          res = min(res, 1 + DFS(index + add + 1))
          add += 1
      
      DP[index] = res
      return res
        
    result = DFS(0)
    return result if result != float('inf') else -1
  
class Solution:
  def shortestWay(self, source, target):
    invertedIndex = defaultdict(list)
    for i, char in enumerate(source):
      invertedIndex[char].append(i)
      
    loopCount = 1
    i = -1
    
    for char in target:
      if char not in invertedIndex: return -1
      offsetListForChar = invertedIndex[char]
      
      # bisect_left(A, x) returns the smallest index j s.t. A[j] >= x. 
      # If no such index j exists, it returns len(A).
      j = bisect_left(offsetListForChar, i)
      
      if j == len(offsetListForChar):
        loopCount += 1
        i = offsetListForChar[0] + 1
      else:
        i = offsetListForChar[j] + 1
    
    return loopCount
  

def runSolution():
  solution = Solution()
  print(solution.shortestWay(source = "abc", target = "abcbc"))
  print(solution.shortestWay(source = "abc", target = "acdbc"))
  print(solution.shortestWay(source = "xyz", target = "xzyxz"))
  print(solution.shortestWay(source = "aaaaa", target = "aaaaaaaaaaaaa"))
  pass
runSolution()