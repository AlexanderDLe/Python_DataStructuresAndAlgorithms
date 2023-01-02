'''

  415. Add Strings

'''



class SolutionRef:
  def addStrings(self, num1, num2):
    p = len(num1) - 1
    q = len(num2) - 1
    carry = 0
    result = []

    while p >= 0 or q >= 0 or carry > 0:
      pNum = int(num1[p]) if p >= 0 else 0
      qNum = int(num2[q]) if q >= 0 else 0

      sum = pNum + qNum + carry
      carry = sum // 10
      mod   = sum  % 10
      result.insert(0, mod)

      p -= 1
      q -= 1
    
    return ''.join(map(str, result))

class Solution:
  
  '''
  
    Time Complexity
    O(n) Iterate through num1 and num2
    
    Space Complexity
    O(n) store new lists for num1, num2, and result (optionally)
  
  '''
  
  def addStrings(self, num1, num2):
    arr1 = list(map(lambda x: int(x),list(num1)))
    arr2 = list(map(lambda x: int(x),list(num2)))
    result = []
    carry = 0
    
    p1, p2 = len(arr1) - 1, len(arr2) - 1
    
    while p1 >= 0 or p2 >= 0 or carry:
      val1 = arr1[p1] if p1 >= 0 else 0
      val2 = arr2[p2] if p2 >= 0 else 0
      sum = carry + val1 + val2
      
      carry = sum // 10
      sum %= 10
      
      result.insert(0, sum)
      
      if p1 >= 0: p1 -= 1
      if p2 >= 0: p2 -= 1
      
    return ''.join(map(lambda x: str(x), result))
    
  
def runSolution():
  solution = Solution()
  print(solution.addStrings('11', '123'))
  print(solution.addStrings('456', '77'))
  print(solution.addStrings('0', '0'))
  pass
runSolution()
