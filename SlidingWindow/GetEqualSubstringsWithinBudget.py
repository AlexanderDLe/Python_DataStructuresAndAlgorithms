'''

  1208. Get Equal Substrings Within Budget

'''

from collections import Counter

class Solution:
  def equalSubstring(self, s, t, maxCost):
    L = R = cost = maxLen = 0
    
    while R < len(s):
      cost += self.getCost(s[R], t[R])
      R += 1
      
      if cost <= maxCost:
        maxLen = max(maxLen, R - L)
        
      if cost > maxCost:
        cost -= self.getCost(s[L], t[L])
        L += 1
    
    return maxLen
  
  def getCost(self, charA, charB):
    return abs(ord(charA) - ord(charB))
  
def runSolution():
  solution = Solution()
  print(solution.equalSubstring(s = "abcd", t = "bcdf", maxCost = 3))
  print(solution.equalSubstring(s = "abcd", t = "cdef", maxCost = 3))
  print(solution.equalSubstring(s = "abcd", t = "acde", maxCost = 0))
  pass
runSolution()
