'''

  Given a Binary String.
  Replace all "01" to "10" until it's no more possible. 
  In 1 second you replace all "01" to "10" in next second keep 
  repeating this procedure. Return the total seconds to complete this. 
  
  eg: 0101->1010->1100 ans:2

  Explanation:

  Example :
  String s = "011"
  For operation 1 -> 101
  For operation 2->110

  Output : 2

  Example :
  String s = "001011";
  For operation 1: 010101
  For operation 2: 101010
  For operation 3: 110100
  For operation 4: 111000
  Output : 4

  Example:
  String s = "011010101001010"
  Output : 7
  
  -------------------------------------------------
  
  0101010
       ^
  -------------------------------------------------
  
  0101010
       ^    Travel from left to first 1
  -------------------------------------------------
  
  0101010
      ^
           
  ones  = 1
  count = 0
'''

import heapq


class SolutionBruteForce:
  def func(self, s):
    count = 0
    
    while '01' in s:
      s = s.replace('01', '10')
      count += 1
    
    return count
  
class Solution:
  def func(self, s):
    count = ones = 0
    n = len(s)
    i = n - 1
    
    while i >= 0 and s[i] == '0':
      i -= 1
    
    while i >= 0:
      if s[i] == '1':
        ones += 1
        
      if s[i] == '0':
        count = max(count, ones - 1)
        count += 1
        ones = 0
      
      i -= 1
      
    return count
      
  
def runSolution():
  solution = Solution()
  print(solution.func('011010101001010'))
  print(solution.func('011'))
  print(solution.func('010101'))
  pass
runSolution()