'''

  340. Longest Substring with At most K Distinct Characters

'''

from collections import Counter

class Solution:
  def lengthOfLongestSubstringKDistinct(self, s, k):
    freqMap = Counter()
    L = maxLen = charCount = 0
    
    for R, Rchar in enumerate(s):
      freqMap[Rchar] += 1
      if freqMap[Rchar] == 1:
        charCount += 1
      
      windowLen = R - L + 1
      if charCount <= k:
        maxLen = max(maxLen, windowLen)
      
      if charCount > k:
        Lchar = s[L]
        L += 1
        freqMap[Lchar] -= 1
        
        if freqMap[Lchar] == 0:
          charCount -= 1
    
    return maxLen

    
  
def runSolution():
  solution = Solution()
  print(solution.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
  print(solution.lengthOfLongestSubstringKDistinct(s = "ccaabbb", k = 1))
  print(solution.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
  pass
runSolution()
