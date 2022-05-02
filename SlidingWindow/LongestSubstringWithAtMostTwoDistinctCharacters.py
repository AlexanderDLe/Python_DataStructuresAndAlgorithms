'''

  159. Longest Substring with At Most Two Distinct Characters

'''

from collections import Counter

class Solution:
  def lengthOfLongestSubstringTwoDistinct(self, s):
    freqMap = Counter()
    L = maxLen = charCount = 0
    
    for R, Rchar in enumerate(s):
      freqMap[Rchar] += 1
      if freqMap[Rchar] == 1:
        charCount += 1
      
      windowLen = R - L + 1
      if charCount <= 2:
        maxLen = max(maxLen, windowLen)
      
      if charCount > 2:
        Lchar = s[L]
        L += 1
        freqMap[Lchar] -= 1
        
        if freqMap[Lchar] == 0:
          charCount -= 1
      
    return maxLen
    
    
  
def runSolution():
  solution = Solution()
  print(solution.lengthOfLongestSubstringTwoDistinct(s = "eceba"))
  print(solution.lengthOfLongestSubstringTwoDistinct(s = "ccaabbb"))
  pass
runSolution()
