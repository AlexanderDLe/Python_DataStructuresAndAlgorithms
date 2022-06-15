'''

  Given a Binary String.
  
  Replace all "01" to "10" until it's no more possible. 
  
  In 1 second you replace all "01" to "10" in next second keep repeating this procedure.
  Return the total seconds to complete this. 
  
  eg: 0101->1010->1100 ans:2

  -----------------------------------------------------------
  
  Example:
  
  String s = "011"
  For operation 1 -> 101
  For operation 2 -> 110

  Output : 2

  -----------------------------------------------------------
  
  Example :
  
  String s = "001011"
  For operation 1: 010101
  For operation 2: 101010
  For operation 3: 110100
  For operation 4: 111000
  Output : 4

  -----------------------------------------------------------

  Example:
  String s = "011010101001010"
  For operation 1: 101101010010100
  For operation 2: 110110100101000
  For operation 3: 111011001010000
  For operation 4: 111101010100000
  For operation 5: 111110101000000
  For operation 6: 111111010000000
  For operation 7: 111111100000000
  Output : 7
  
  -----------------------------------------------------------
  
  
  If you go through binary strings 1 by 1 you'll notice a pattern. 
  
  It is almost always the index of the left most zero minus the index 
  of the right most one.
  
  001
  s e     s = start, e = end
          e - s
  010     2 - 0
  100     2
  
   1   5 
  10000100 5 - 1 = 4
   s   e
  ------------------------
  
  EXCEPT in one case: 0101.
  
  As long as there is two instances of '01' in the string you will have 
  to subtract 1 from the solution using the index math. 
  
  Cases such as 0101 011011 or even 01110111. 
  In my code, I call this idiosyncrasy. 
  
  ------------------------
  
  0  3    s - e
  0101    3 - 0
  s  e    3
  
  ------------------------
  011011
  
  101101
  110110
  111010
  111100
  4
  
  ------------------------
  00011001
  
  00101010
  01010100
  10101000
  11010000
  11100000
  6
  
  ------------------------
  01010101
  
  10101010
  11010100
  11101000
  11110000
  
  
'''

from collections import defaultdict

class Solution:
  def func(self, s):
    n = len(s)
    index1 = 0
    index0 = n
    idiosyncrasy = 0
    
    for i in range(n):
      if   s[i] == '0':
        index0 = min(index0, i)
      elif s[i] == '1':
        index1 = max(index1, i)
        
      if i < n - 1 and s[i] == '0' and s[i + 1] == '1':
        idiosyncrasy += 1
    
    result = index1 - index0
    # print(index1, index0, idiosyncrasy)
    if index0 > index1: return 0
    
    return result - (idiosyncrasy - 1) if idiosyncrasy > 1 else result

def runSolution():
  solution = Solution()
  print(solution.func('0001'))
  print(solution.func('011010'))
  print(solution.func('011011'))
  print(solution.func('00011001'))
  print(solution.func('0101'))
  print(solution.func('01010101'))
  pass
runSolution()