'''

  3. Longest Substring Without Repeating Characters


  abcabcbb
   L  R
 
  {
    a: 1
    b: 1
    c: 1
  }
'''

from collections import Counter

class Solution:
  def lengthOfLongestSubstring(self, s):
    longestLen = 0
    freqMap = Counter()
    L, R = 0, 0
    
    while R < len(s):
      Rchar = s[R]
      freqMap[Rchar] += 1
      R += 1
      
      if freqMap[Rchar] == 1: 
        longestLen = max(longestLen, R - L)
      else:
        while freqMap[Rchar] != 1:
          Lchar = s[L]
          freqMap[Lchar] -= 1
          L += 1
    
    return longestLen
  
def runSolution():
  solution = Solution()
  print(solution.lengthOfLongestSubstring(s = "abcabcbb"))
  print(solution.lengthOfLongestSubstring(s = "bbbbb"))
  print(solution.lengthOfLongestSubstring(s = "pwwkew"))
  pass
runSolution()
