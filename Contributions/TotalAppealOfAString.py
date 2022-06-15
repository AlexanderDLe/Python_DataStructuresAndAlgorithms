'''

  2262. Total Appeal of A String

  Contribution Strategy: The appeal of a string is number of distinct chars
  a string. How does each character contribute to the overall result?
  
  

  a b b c a
  ^     
  abbca, abbc, abb, ab, a   <----- The first a contributes to the overall appeal 5 times in 
                                   5 different substrings.
  appeal = 5 
  result = 5 
  last = {                         Even though it appears twice (abbca) it still counts once.
    a: 0
  }
  
  ------------------------------

  a b b c a                 <----- This b contributes 8 times to the overall appeal.
    ^                              Why? It appears in 8 different substrings.
  ab, abb, abbc, abbca
  b, bb, bbc, bbca                 We can calculate the number of substrings it is in by
                                   (length of left substring) * (length of right substring)
  appeal = 8                       (ab) * (bbca) = 2 * 4 = 8
  result = 13
  last = {
    a: 0
    b: 1
  }

  ------------------------------

  a b b c a                 <----- This b contributes only 3 times compared to the previous b.
      ^                            We use the previous b as the left boundary because we do not
  b, bca, ca                       want to include duplicates.
  
  appeal = 3                       We use the last dict to keep track of the left boundary.
  result = 16
  last = {
    a: 0
    b: 1
  }

  ------------------------------
  
  etc...
  
'''


from collections import defaultdict

class Solution:
  def appealSum(self, s):
    last = defaultdict(lambda: -1)
    n = len(s)
    appeal = 0
    
    for i, char in enumerate(s):
      leftLen = i - last[char]
      rightLen = n - i
      appeal += leftLen * rightLen
      last[char] = i
    
    return appeal
  
def runSolution():
  solution = Solution()
  print(solution.appealSum(s = "abbca"))
  print(solution.appealSum(s = "code"))
  pass
runSolution()
