'''

  125. Valid Palindrome

'''

class Solution:
  def isPalindrome(self, s):
    L, R = 0, len(s) - 1
    
    while L < R:
      if not s[L].isalnum(): 
        L += 1
      elif not s[R].isalnum(): 
        R -= 1
      else: 
        if s[L].lower() != s[R].lower(): return False
        L += 1
        R -= 1
    
    return True
  
def runSolution():
  solution = Solution()
  print(solution.isPalindrome(s = "A man, a plan, a canal: Panama"))
  print(solution.isPalindrome(s = "race a car"))
  pass
runSolution()
