'''

  2268. Minimum Number of Keypresses
  
  26 letters can be mapped onto 9 digits with at most 3 chars per digit
  
  Strategy:
  
  Use as few chars per digit as possible.
  1. Use up all digits to map the most frequent 9 chars to 1 presses first.
  2. Use up all digits to map the next frequent 9 chars to 2 presses
  3. Use the rest of the digits to map the rest of the chars
  
  As mentioned, it will be more optimal to map most frequest chars first -
  We are seeking the minimal presses, so by mapping most frequent to 1-presses
  we can minimize the press count.
  
  ----------------------------------------------------------------
  
  string = 'aaabbbdddcdeffkkklmmnnoopqrrrr'
  
  freqMap = {
    r = 4,
    a = 3
    b = 3
    d = 3
    k = 3
    f = 2
    m = 2
    n = 2
    o = 2
    c = 1
    d = 1
    e = 1
    l = 1
    p = 1
    q = 1
  }
  
  Turned into an array sorting in DESC:
  [4,3,3,3,3,2,2,2,2,1,1,1,1,1,1]
  
  - The first 9 will be 1-presses, the next 9 will be 2-presses, etc.
  
  
  
'''

from collections import Counter
from itertools import product


class SolutionRef:
  def minimumKeypresses(self, s):
    freqMap = Counter(s)
    vals = list(freqMap.values())
    vals.sort(reverse=True)
    
    result = 0
    presses = 1
    count = 0
    
    for val in vals:
      count += 1
      
      if count > 9:
        count = 1
        presses += 1
        
      result += val * presses
    
    return result
  
  
class Solution:
  def minimumKeypresses(self, s):
    freqMap = Counter(s)
    vals = list(freqMap.values())
    vals.sort(reverse=True)
    
    result = 0
    presses = 1
    
    for i, freq in enumerate(vals):
      if i > 0 and i % 9 == 0:
        presses += 1
      result += presses* freq
      
    return result
      
      
  
def runSolution():  
  solution = Solution()
  print(solution.minimumKeypresses(s = "apple"))
  print(solution.minimumKeypresses(s = "abcdefghijkl"))
runSolution()