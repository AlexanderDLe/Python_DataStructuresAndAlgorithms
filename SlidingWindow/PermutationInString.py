'''

  567. Permutation in String

  e i d b a o o o        match = 'ab'
        L R

  freqDict:{
    a: 1
    b: 0
  }
  charCount = 1

'''

from collections import Counter

class SolutionRef:
  def checkInclusion(self, s1, s2):
    n = len(s1)
    freqDict = Counter(s1)
    charCount = len(freqDict.keys())
    
    L = 0
    for R, Rchar in enumerate(s2):
      # print(L, R)
      if Rchar in freqDict:
        freqDict[Rchar] -= 1
        # Mistake: This charCount adjustment needs to be in this condition
        if freqDict[Rchar] == 0: charCount -= 1
        
      if charCount == 0: return True
      
      if R >= n - 1:
        Lchar = s2[L]
        # Mistake: don't forget to increment
        L += 1
        if Lchar in freqDict: 
          freqDict[Lchar] += 1
          if freqDict[Lchar] == 1: charCount += 1
    
    return False
  

class Solution:
  def checkInclusion(self, s1, s2):
    freqDict = Counter(s1)
    uniqueChars = len(freqDict.keys())
    charsSatisfied = L = 0
    
    for R, Rchar in enumerate(s2):
      if Rchar in freqDict: 
        freqDict[Rchar] -= 1
        if freqDict[Rchar] == 0: charsSatisfied += 1
    
      if charsSatisfied == uniqueChars: return True
      
      if R >= len(s1) - 1:
        Lchar = s2[L]
        if Lchar in freqDict: 
          freqDict[Lchar] += 1
          if freqDict[Lchar] == 1: charsSatisfied -= 1
        L += 1
    
    return False
  
def runSolution():
  solution = Solution()
  print(solution.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
  print(solution.checkInclusion(s1 = "ab", s2 = "eidboaoo"))
  print(solution.checkInclusion("abcdxabcde", "abcdeabcdx"))
  pass
runSolution()
