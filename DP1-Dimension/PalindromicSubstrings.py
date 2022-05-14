'''

  647. Palindromic Substrings

'''

class Solution:
  def countSubstrings(self, s):
    self.s, self.n = s, len(s)
    count = 0
    
    for i in range(self.n):
      count += self.countPalindromes(s, i, i)
      count += self.countPalindromes(s, i, i + 1)
    
    return count
  
  def countPalindromes(self, s, L, R):
    currCount = False
    
    while L >= 0 and R < self.n and s[L] == s[R]:
      currCount += 1
      L -= 1
      R += 1
    
    return currCount
    
  
def runSolution():
  solution = Solution()
  print(solution.countSubstrings(s = "abc"))
  print(solution.countSubstrings(s = "aaa"))
  pass
runSolution()