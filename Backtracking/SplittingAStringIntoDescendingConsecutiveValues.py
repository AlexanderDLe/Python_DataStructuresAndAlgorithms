'''

  1849. Splitting a String Into Descending Consecutive Values

'''

class Solution:
  def splitString(self, s):
    n = len(s)
    
    def backtrack(index, parts, prev):
      if index == n: return parts > 1
      
      for i in range(index, n):
        val = int(s[index:i+1])
        
        if prev == None or prev == val + 1:
          if backtrack(i + 1, parts + 1, val): return True
          
      return False
    
    return backtrack(0, 0, None)
  
  
def runSolution():
  solution = Solution()
  print(solution.splitString(s = "1234"))
  print(solution.splitString(s = "050043"))
  print(solution.splitString(s = "9080701"))
  pass
runSolution()
