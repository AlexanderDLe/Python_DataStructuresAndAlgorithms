'''

  1891. Cutting Ribbons

  -------------------------------------------------

  k = 22

  [9,7,5]
  L = 0
  R = 21
  
  len = (L + R + 1)/2
  len = 22/2 = 11

  -------------------------------------------------

  [9,7,5]
  L = 0
  R = 11
  
  len = 12/2 = 6

  -------------------------------------------------

  [9,7,5]
  L = 0
  R = 6
  
  len = 7/2 = 3

  -------------------------------------------------

  [9,7,5]
  L = 0
  R = 6
  
  len = 5/2 = 3

'''


def maxLength(ribbons, k):
  def isValid(len):
    nonlocal k, ribbons
    res = 0

    for ribbon in ribbons:
      res += ribbon//len
    
    if res >= k: return True
    else       : return False

  L = 1
  R = sum(ribbons)
  if k > R: return 0

  while L < R:
    len = (L + R + 1)//2

    if isValid(len): L = len
    else           : R = len - 1

  return L

print(maxLength(ribbons = [9,7,5], k = 3))
print(maxLength(ribbons = [7,5,9], k = 4))
print(maxLength(ribbons = [5,7,9], k = 22))