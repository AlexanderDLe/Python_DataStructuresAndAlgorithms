'''

  5. Longest Palindromic Substring

'''

class Solution:
  def longestPalindrome(self, s):
    self.s, self.n = s, len(s)
    result = ''
    
    for i in range(self.n):
      palindrome1 = self.getPalindrome(s, i, i)
      palindrome2 = self.getPalindrome(s, i, i + 1)
      longer = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
      
      if len(longer) > len(result): result = longer
    
    return result
  
  def getPalindrome(self, s, L, R):
    valid = False
    
    while L >= 0 and R < self.n and s[L] == s[R]:
      valid = True
      L -= 1
      R += 1
    
    if not valid: return ''
    else: return s[L + 1 : R]
    
  
def runSolution():
  solution = Solution()
  print(solution.longestPalindrome("babad"))
  print(solution.longestPalindrome("cbbd"))
  pass
runSolution()