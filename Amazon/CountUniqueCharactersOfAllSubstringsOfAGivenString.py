'''

  828. Count Unique Characters of All Substrings of a Given String

  ------------------------------------------------------------------------
  
  Input: s = "ABC"
  Output: 10
  
  Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".

  Evey substring is composed with only unique letters.
  Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

  ------------------------------------------------------------------------

  Input: s = "ABA"
  Output: 8

  Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

  ------------------------------------------------------------------------

  ABCFBDAB

  Determine the contribution of each unique char:

  Ex.:


  ABCFBDAB
      ^

  --CFBDA-
      ^
  This this position, it is unique for this substring. Therefore, anything
  beyond these chars will not count.

  --CFBDA-
  
  For every substring that includes B on the left, it has a multiplicative product
  with every substring that includes B on the right.

  Therefore the answer will be added by:
  (num. of substrings on left) * (num. of substrings on right)

  ----------------------

  01234567
  --CFBDA-
      ^
  leftSubstrings = i - (index - 1) = 4 - (4 - 1) = 3


'''

from collections import defaultdict


class SolutionRef:
  def countChars(str):
    n = len(str)
    dict = {}

    for i, char in enumerate(str):
      if char not in dict: dict[char] = []
      dict[char].append(i)

    result = 0
    for key in dict:
      indexes = dict[key]

      for i, index in enumerate(indexes):
        if i == 0: leftSubstrings = index + 1
        else     : leftSubstrings = index - indexes[i - 1]

        if i == len(indexes) - 1: rightSubstrings = n - index
        else                    : rightSubstrings = indexes[i + 1] - index

        result += leftSubstrings * rightSubstrings

      
    return result
  
class Solution:
  def countChars(self, str):
    n = len(str)
    indiceMap = defaultdict(list)
    
    for i, char in enumerate(str):
      indiceMap[char].append(i)
      
    result = 0
    
    for indices in list(indiceMap.values()):
      for i, index in enumerate(indices):
        leftBoundary  = indices[i - 1] if i > 0 else -1
        rightBoundary = indices[i + 1] if i < len(indices) - 1 else n
        
        leftLen  = index - leftBoundary
        rightLen = rightBoundary - index
        
        result += leftLen * rightLen
        
    
    return result
    
    
  
def runSolution():
  solution = Solution()
  print(solution.countChars('ABC'))
  print(solution.countChars('LEETCODE'))
  pass
runSolution()
