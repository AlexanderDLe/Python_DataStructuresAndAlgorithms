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

from collections import Counter, defaultdict

class SolutionRef:
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
  
class Solution1:
  def lengthOfLongestSubstring(self, s):
    longestLen = 0
    freqMap = defaultdict(int)
    L = 0
    
    for R, Rchar in enumerate(s):
      freqMap[Rchar] += 1
      
      while freqMap[Rchar] > 1:
        Lchar = s[L]
        freqMap[Lchar] -= 1
        L += 1
        
      windowLen = R - L + 1
      if longestLen < windowLen:
        longestLen = windowLen
    
    return longestLen
  
class Solution:
  
  '''
  
    Time Complexity:
    - O(n) Pass through string input at least once.
    
    Space Complexity: 
    - Average: O(m) where m is the number of unique characters
    - O(1) because there are at most 26 unique letters
  
  '''
  
  def lengthOfLongestSubstring(self, s):
    longestLength = 0
    freqMap = defaultdict(int)
    L = 0
    
    for R, Rchar in enumerate(s):
      freqMap[Rchar] += 1
      
      # Collapse window while repeat detected
      while freqMap[Rchar] > 1:
        Lchar = s[L]
        freqMap[Lchar] -= 1
        L += 1
        
      # Set longestLength
      windowLength = R - L + 1
      longestLength = max(longestLength, windowLength)
          
        
    return longestLength
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.lengthOfLongestSubstring(s = "abcabcbb"))
  print(solution.lengthOfLongestSubstring(s = "bbbbb"))
  print(solution.lengthOfLongestSubstring(s = "pwwkew"))
  pass
runSolution()
