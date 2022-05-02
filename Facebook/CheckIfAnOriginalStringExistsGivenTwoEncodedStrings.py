'''

  2060. Check if an Original String Exists Given Two Encoded Strings
  
'''

from functools import cache


def possiblyEquals(s1, s2):
  def allPossibleWildcardLengths(nums, carryover = 0, options = set()):
    if len(nums) == 0: return

    for x in range(1, len(nums) + 1):
        prefix = int(''.join(nums[:x]))

        if x == len(nums): 
          options.add(carryover + prefix)
        else: 
          allPossibleWildcardLengths(nums[x:], carryover + prefix, options)

    return options
  
  def parse(string):
    res = []
    numbers = []

    for c in string:
      if c.isdigit(): numbers.append(c)
      else:
        if numbers:
          res.append(allPossibleWildcardLengths(numbers, 0, set()))
          numbers = []
        res.append(c)

    if numbers:
      res.append(allPossibleWildcardLengths(numbers, 0, set()))

    return res
  
  repr1, repr2 = parse(s1), parse(s2)
  len1, len2 = len(repr1), len(repr2)

  print(repr1)
  print(repr2)

  @cache
  def DFS(i, j, diff):
    # if both strings have been exhausted, we're done
    # if only one string is at max-length, then we're probably iterating through
    # the diffs, so we can wait
    if i == len1 and j == len2: return diff == 0

    # if only one string has been exhausted, we're not able to match the two
    if i > len1  or  j > len2 : return False

    s1 = repr1[i] if i < len1 else ''
    s2 = repr2[j] if j < len2 else ''

    s1_isWild = type(s1) != str
    s2_isWild = type(s2) != str

    # if one is wildcard and other is a string,
    # go through all the possibilities for wildcards and recurse
    if s1_isWild and not s2_isWild:
      for digit in s1:
        if DFS(i + 1, j, diff + digit): return True
      return False
    
    if s2_isWild and not s1_isWild:
      for digit in s2:
        if DFS(i, j + 1, diff - digit): return True
      return False

    # If both are wildcards
    # You need to go through all combinations
    if s1_isWild and s2_isWild:
      for digit1 in s1:
        for digit2 in s2:
          if DFS(i + 1, j + 1, diff + digit1 - digit2): return True
      return False

    # If both are strings
    if not s1_isWild and not s2_isWild:
      if diff == 0:
        if s1 != s2: return False
        else       : return DFS(i + 1, j + 1, diff)
      
      else:
        if diff > 0: return DFS(i, j + 1, diff - 1)
        else       : return DFS(i + 1, j, diff + 1)


  return DFS(0, 0, 0)


# print(possiblyEquals(s1 = "internationalization", s2 = "i18n"))
print(possiblyEquals(s1 = "l123eyabc", s2 = "44y3"))
# print(possiblyEquals(s1 = "a5b", s2 = "c5b"))