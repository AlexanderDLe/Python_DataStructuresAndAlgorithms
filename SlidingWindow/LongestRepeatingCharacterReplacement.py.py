'''

  424. Longest Repeating Character Replacement

  B A A A     k = 0
 L  R

  mostCommonChar = 
  mostCommonCont = 
  {
    A: 1
    B: 1
  }
  
  maxLen = 
  windowLen = 
  replacementsNeeded = 

'''

from collections import Counter

class SolutionRef:
  def characterReplacement(self, s, k):
    freqMap = Counter()
    L = maxLen = mostFreq = 0
    
    for R, Rchar in enumerate(s):
      freqMap[Rchar] += 1
      
      mostFreq = max(mostFreq, freqMap[Rchar])
      replacementsNeeded = R - L + 1 - mostFreq

      if replacementsNeeded <= k:
        maxLen = max(maxLen, R - L + 1)
      
      if replacementsNeeded > k:
        freqMap[s[L]] -= 1
        L += 1
    
    return maxLen

'''

  A A B A B B A  K = 2
 LR
 
  maxLen = 0
  maxFreq = 1
  
  freqMap = {
    A: 1
    B:
  }

'''
class Solution:
  def characterReplacement(self, s, k):
    freqMap = Counter()
    L = maxLen = maxFreq = 0
    
    for R, Rchar in enumerate(s):
      freqMap[Rchar] += 1
      
      maxFreq = max(maxFreq, freqMap[Rchar])
      windowLen = R - L + 1
      replacementsNeeded = windowLen - maxFreq
      
      if replacementsNeeded <= k:
        maxLen = max(maxLen, windowLen)
      
      if replacementsNeeded > k:
        Lchar = s[L]
        freqMap[Lchar] -= 1
        L += 1
    
    return maxLen
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.characterReplacement(s = "ABAB", k = 2))
  print(solution.characterReplacement(s = "AABABBA", k = 1))
  print(solution.characterReplacement(s = "BAAA", k = 0))
  pass
runSolution()
