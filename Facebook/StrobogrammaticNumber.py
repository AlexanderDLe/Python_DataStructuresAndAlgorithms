'''

  246. Strobogrammatic Number

  Edge case 1: number is not matchable
  Edge case 2: middle number unaccounted for (L <= R is required to check unmatchables)
  
'''

def isStrobogrammatic(num):
  matches = {'6':'9', '9':'6','1':'1','0':'0','8':'8'}

  L, R = 0, len(num) - 1
  while L <= R:
    char = num[L]
    if char not in matches or num[R] != matches[num[L]]: return False
    L += 1
    R -= 1
  
  return True


print(isStrobogrammatic('69'))
print(isStrobogrammatic('88'))
print(isStrobogrammatic('962'))
print(isStrobogrammatic('2'))