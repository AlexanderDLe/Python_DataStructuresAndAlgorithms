'''

  2055. Plates Between Candles

'''


from collections import defaultdict


class SolutionSlow:
  def platesBetweenCandles(self, s, queries):
    self.buildPrefix(s)
    
    result = []
    for start, end in queries:
      result.append(self.scanForPlates(s, start, end))
      
    return result
  
  def scanForPlates(self, s, start, end):
    while start < end and s[start] != '|': start += 1
    while start < end and s[end]   != '|': end   -= 1
    
    if start >= end: return 0
    return self.prefixes[end] - self.prefixes[start]
  
  def buildPrefix(self, s):
    self.prefixes = {}
    plateCount = 0
    
    for i, char in enumerate(s):
      if char == '*': 
        plateCount += 1
      else: 
        self.prefixes[i] = plateCount
      

class Solution:
  def platesBetweenCandles(self, s, queries):
    n = len(s)
    left  = self.buildNearestLeftCandle(s, n)
    right = self.buildNearestRightCandle(s, n)
    plates = self.buildPlatesPerIndex(s, n)
    result = []
    
    for start, end in queries:
      startCandle = right[start]
      endCandle = left[end]
      
      if startCandle >= endCandle: 
        result.append(0)
      else:
        result.append(plates[endCandle] - plates[startCandle])
        
    return result
    
  def buildPlatesPerIndex(self, s, n):
    plates = [0] * n
    count = 0
    
    for i in range(n):
      if s[i] == '*':
        count += 1
        plates[i] = count
      else:
        plates[i] = plates[i - 1]
    
    return plates
    
  def buildNearestLeftCandle(self, s, n):
    left  = [-1] * n
    count = -1
    
    for i in range(n):
      if s[i] == '|':
        count = i
        left[i] = count
      else:
        left[i] = count
        
    return left
      
  def buildNearestRightCandle(self, s, n):
    right = [n + 1] * n 
    count = n + 1

    for i in range(n - 1, -1, -1):
      if s[i] == '|':
        count = i
        right[i] = count
      else:
        right[i] = count
    
    return right
  
def runSolution():
  solution = Solution()
  print(solution.platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]]))
  print(solution.platesBetweenCandles(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]))
  pass
runSolution()