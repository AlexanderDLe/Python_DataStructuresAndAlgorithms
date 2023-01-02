'''

  12. Integer to Roman

  I, II, III, IV, V, VI, VII, VIII, IX, X


  ---------------------------------------------------------------------------------
  
  1994    IV
     ^    4
     
  1994    XC + IV
    ^     90 + 4
     
  1994    CM + XC + IV
   ^     900 + 90 + 4
   
  1994    M    + CM + XC + IV
  ^       1000 + 900 + 90 + 4
  
          MCMXCIV

'''


class Solution:
  def intToRoman(self, num):
    arr = list(map(int, list(str(num))))
    result = []
    zeroes = 1
    
    for i in range(len(arr) - 1, -1, -1):
      digit = arr[i]
      val = digit * zeroes
      one, five, ten = self.determineCharacters(val)
      
      if   digit <= 3: result.insert(0, one * digit)
      elif digit == 4: result.insert(0, one + five)
      elif digit == 5: result.insert(0, five)
      elif digit == 6: result.insert(0, five + one)
      elif digit == 7: result.insert(0, five + one + one)
      elif digit == 8: result.insert(0, five + one + one + one)
      elif digit == 9: result.insert(0, one + ten)
      
      zeroes *= 10
    
    return ''.join(result)
  
  def determineCharacters(self, val):
    if   val <= 9  : one, five, ten = 'I', 'V', 'X'
    elif val <= 99 : one, five, ten = 'X', 'L', 'C'
    elif val <= 999: one, five, ten = 'C', 'D', 'M'
    else           : one, five, ten = 'M', None, None

    return (one, five, ten)

class Solution2:
  def intToRoman(self, num):
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    return M[int(num/1000)] + C[int((num%1000)/100)] + X[int((num%100)/10)] + I[int(num%10)];
  

  
def runSolution():
  solution = Solution2()
  print(solution.intToRoman(3))
  print(solution.intToRoman(58))
  print(solution.intToRoman(1994))
  print(solution.intToRoman(3999))
  pass
runSolution()
