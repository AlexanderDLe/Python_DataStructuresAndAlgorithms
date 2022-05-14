'''

  131. Palindrome Partitioning
  
'''

class SolutionRef:
  def partition(self, s):
    result = []
    
    def isPalindrome(st):
      return st == st[::-1]
    
    def DFS(res, index):
      print(res)
      if index == len(s) + 1:
        result.append(res.copy())
        return

      for i in range(index, len(s) + 1):
        substr = s[index - 1: i]
        
        if isPalindrome(substr):
          res.append(substr)
          DFS(res, i + 1)
          res.pop()
          
    DFS([], 1)
    return result
  
class Solution:
  def partition(self, s):
    n = len(s)
    result = []
    
    def DFS(res, index):
      if index == n:
        result.append(res.copy())
        return
      
      for i in range(index, n):
        substr = s[index:i + 1]
        
        if self.isPalindrome(substr):
          res.append(substr)
          DFS(res, i + 1)
          res.pop()
    
    DFS([], 0)
    return result

  def isPalindrome(self, substr):
    return substr == substr[::-1]
  
  
def runSolution():
  solution = Solution()
  print(solution.partition(s = "aabaa"))
  print(solution.partition(s = "a"))
  pass
runSolution()
