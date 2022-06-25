'''

  1044. Longest Duplicate Substring

'''

class SolutionRef:
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
    
class Solution:
  def longestDupSubstring(self, S):
    L, R = 0, len(S) - 1
    maxRes = ''
    
    while L < R:
      M = 1 + L + (R - L)//2
      
      duplicate, valid = self.isValid(M, S)
      if valid: maxRes = duplicate
      
      if valid: L = M
      else    : R = M - 1
    
    return maxRes
  
  def isValid(self, length, S):
    seen = set()
    
    '''
      banana  <-- len = 6
         ^        6 - 3 = 3, need to add 1 to length
      Need to add 1 to account for last substr
    
    '''
    for i in range(0, len(S) - length + 1):
      substr = S[i:i + length]
      if substr in seen: return (substr, True)
      seen.add(substr)
    
    return '', False
    
    
  
def runSolution():
  solution = Solution()
  print(solution.longestDupSubstring('banana'))
  print(solution.longestDupSubstring('abcd'))
  print(solution.longestDupSubstring('aa'))
  pass
runSolution()