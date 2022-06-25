'''

  696. Count Binary Substrings

'''

from itertools import product


class Solution:
  def countBinarySubstrings(self, s):
    ans = 0
    prev = curr = 0
    
    for i in range(len(s)):
      if i == 0:
        curr += 1
        continue
      
      pVal, cVal = s[i - 1], s[i]
      
      if pVal == cVal:
        curr += 1
        continue
      
      if pVal != cVal:
        ans += min(prev, curr)
        prev = curr
        curr = 1
    
    ans += min(prev, curr)    
    return ans

def runSolution():
  solution = Solution()
  print(solution.countBinarySubstrings(s = "00110011"))
  print(solution.countBinarySubstrings(s = "10101"))
  
runSolution()