'''

  76. Minimum Window Substring
  
'''

from collections import Counter


class SolutionRef:
  def minWindow(self, s, t):
    tFreq = Counter(t)
    count = len(tFreq.keys())
    L, minLen, result = 0, float('inf'), ''
    
    for R, Rchar in enumerate(s):
      tFreq[Rchar] -= 1
      
      if tFreq[Rchar] == 0: count -= 1
      
      while count == 0:
        windowLen = R - L + 1
        if windowLen < minLen:
          result = s[L:R + 1]
          minLen = windowLen
        
        Lchar = s[L]
        tFreq[Lchar] += 1
        L += 1
        
        if tFreq[Lchar] == 1:
          count += 1
    
    return result
  
class Solution:
  def minWindow(self, s, t):
    freqDict = Counter(t)
    satisfied = 0
    uniqueChars = len(list(freqDict.keys()))
    self.result = ''
    
    L = 0
    for R, Rchar in enumerate(s):
      if Rchar in freqDict:
        freqDict[Rchar] -= 1
        if freqDict[Rchar] == 0: satisfied += 1
        
      # Collapse window when match
      while uniqueChars == satisfied and L < R:
        # Set new potential result
        substr = s[L: R + 1]
        if self.result == '' or len(substr) < len(self.result):
          self.result = substr
        
        Lchar = s[L]
        L += 1
        if Lchar in freqDict:
          freqDict[Lchar] += 1
          if freqDict[Lchar] == 1: satisfied -= 1
          
    return self.result
    
  
def runSolution():
  solution = Solution()
  print(solution.minWindow(s = "ADOBECODEBANC", t = "ABC"))
  print(solution.minWindow(s = "a", t = "a"))
  print(solution.minWindow(s = "a", t = "aa"))
  pass
runSolution()
