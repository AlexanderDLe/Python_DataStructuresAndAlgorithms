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

from collections import Counter, defaultdict

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

  k = 1
  
  AABABBA
  L  R

  maxLen = 4
  
'''

class Solution:
  
  '''
  
    Time Complexity
    O(n) to iterate through all elements
    
    Space Complexity
    O(1)
  
  '''
  
  def characterReplacement(self, s, k):
    freqMap = defaultdict(int)
    maxLen = maxFreq = L = 0
    
    for R, Rchar in enumerate(s):
      freqMap[Rchar] += 1
      
      maxFreq = max(maxFreq, freqMap[Rchar])
      replacementsRequired = R - L + 1 - maxFreq
      
      if replacementsRequired > k:
        freqMap[s[L]] -= 1
        L += 1
        
      maxLen = max(maxLen, R - L + 1)
    
    return maxLen
    
  def characterReplacementPractice(self, s, k):
    freqMap = defaultdict(int)
    maxLen = maxFreq = L = 0
    
    for R, Rchar in enumerate(s):
      freqMap[Rchar] += 1
      
      # Set the most common char
      maxFreq = max(maxFreq, freqMap[Rchar])
        
      # Determine replacements needed
      windowSize = R - L + 1
      replacementsRequired = windowSize - maxFreq
      
      # Move L forward if window requires more than k replacements
      # Mistake: don't forget to update the map
      if replacementsRequired > k: 
        Lchar = s[L]
        freqMap[Lchar] -= 1
        L += 1
      
      # Update maxLen
      maxLen = max(maxLen, R - L + 1)
    
    return maxLen
    
  
def runSolution():
  solution = Solution()
  print(solution.characterReplacement(s = "ABAB", k = 2))
  print(solution.characterReplacement(s = "AABABBA", k = 1))
  print(solution.characterReplacement(s = "BAAA", k = 0))
  pass
runSolution()
