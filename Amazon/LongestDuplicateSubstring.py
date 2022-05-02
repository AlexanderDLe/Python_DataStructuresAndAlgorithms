'''

  1044. Longest Duplicate Substring

'''

class Solution:
  M = 2**63 - 1
  
  def longestDupSubstring(self, S):
    self.S = S
    unicodes = [ord(c) - ord('a') for c in S]
    
    L, R = 0, len(S) - 1
    result = ''
    
    while L < R:
      M = (L + R + 1)//2
      isValid, validStr = self.validDuplicate(M)
      print(M, isValid, validStr)

      if isValid: 
        L = M
        result = validStr
      else: 
        R = M - 1
    
    return result
    
  
  def validDuplicate(self, M):
    seen = set()
    
    # banana 
    for i in range(0, len(self.S) - M + 1):
      substr = self.S[i:i + M]
      if substr in seen: return (True, substr)
      seen.add(substr)
      print(M, substr)
    
    return (False, '')
    
  
def runSolution():
  solution = Solution()
  print(solution.longestDupSubstring('banana'))
  print(solution.longestDupSubstring('abcd'))
  pass
runSolution()