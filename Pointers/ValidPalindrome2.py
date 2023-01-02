'''

  680. Valid Palindrome 2

'''

class Solution:
  
  '''
  
    Time Complexity:
    - O(n) Iterate through input string twice
    
    Space Complexity:
    - O(1) No data structure used
  
  '''
  
  def validPalindrome(self, s):
    L, R = 0, len(s) - 1
    
    while L < R:
      if s[L] == s[R]:
        L += 1
        R -= 1
        
      else:
        removeLeft  = self.isPalindrome(L + 1, R, s)
        removeRight = self.isPalindrome(L, R - 1, s)
        return removeLeft or removeRight
    
    return True
  
  
  def isPalindrome(self, L, R, s):
    while L < R:
      if s[L] != s[R]: return False
      L += 1
      R -= 1
      
    return True
  
def runSolution():
  solution = Solution()
  print(solution.validPalindrome(s = "aba"))
  print(solution.validPalindrome(s = "abca"))
  print(solution.validPalindrome(s = "abc"))
  pass
runSolution()
