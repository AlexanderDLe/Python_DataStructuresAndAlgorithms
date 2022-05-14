'''

  76. Minimum Window Substring
  
'''

from collections import Counter


class Solution:
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
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.minWindow(s = "ADOBECODEBANC", t = "ABC"))
  print(solution.minWindow(s = "a", t = "a"))
  print(solution.minWindow(s = "a", t = "aa"))
  pass
runSolution()
