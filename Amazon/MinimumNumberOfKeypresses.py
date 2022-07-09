'''

  2268. Minimum Number of Keypresses
  
'''

from collections import Counter
from itertools import product


class Solution:
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
  
def runSolution():  
  solution = Solution()
  print(solution.minimumKeypresses(s = "apple"))
  print(solution.minimumKeypresses(s = "abcdefghijkl"))
runSolution()