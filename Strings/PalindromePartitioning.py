'''

  131. Palindrome Partitioning

  aabaa
  ^
  
  a|abaa
'''

from functools import cmp_to_key


class Solution:
  def partition(self, s):
    self.s = s
    n = len(s)
    
    def backtrack(index, res):
      if index == n:
        result.append(res.copy())
        return

      for i in range(index, n):
        if self.isPalindrome(index, i):
          res.append(s[index:i + 1])
          backtrack(i + 1, res)
          res.pop()
    
    result = []
    backtrack(0, [])
    return result

  def isPalindrome(self, L, R):
    while L < R:
      if self.s[L] != self.s[R]: return False
      L += 1
      R -= 1
      
    return True
      
    
    
  
def runSolution():
  solution = Solution()
  print(solution.partition(s = "aab"))
  print(solution.partition(s = "a"))
  pass
runSolution()
