'''

  680. Valid Palindrome 2

'''

def checkValid(s, L, R):
  while L < R:
    if s[L] != s[R]: return False
    L += 1
    R -= 1

  return True

def validPalindrome(s):
  L, R = 0, len(s) - 1

  while L < R:
    if s[L] != s[R]:
      if checkValid(s, L + 1, R) == True: return True
      if checkValid(s, L, R - 1) == True: return True
      return False
      
    L += 1
    R -= 1

  return True


print(validPalindrome('aba'))
print(validPalindrome('abca'))
print(validPalindrome('abc'))