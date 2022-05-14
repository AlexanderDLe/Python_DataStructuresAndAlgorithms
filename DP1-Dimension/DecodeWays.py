'''

  91. Decode Ways

        2  2  6
DP:  0  1  
  

'''

class SolutionBruteForce:
  def numDecodings(self, s):
    if s == '': return 0
    
    isValidChar = lambda i: int(s[i:i + 2]) <= 26
    n = len(s)
    count = 0
    
    def recurse(index):
      nonlocal count
      if index == n: count += 1
      if index >= n or s[index] == '0': return
      
      recurse(index + 1)
      
      if index < n - 1 and isValidChar(index):
        recurse(index + 2)
    
    recurse(0)
    return count
  
class Solution1:
  def numDecodings(self, s):
    isValidChar = lambda i: int(s[i:i + 2]) <= 26
    n = len(s)
    DP = { n : 1 }
    
    for i in range(n - 1, -1, -1):
      if s[i] == '0':
        DP[i] = 0
      else:
        DP[i] = DP[i + 1]
        
      if i < n - 1 and s[i] != '0' and isValidChar(i):
        DP[i] += DP[i + 2]
    
    return DP[0]
  
class Solution2:
  def numDecodings(self, s):
    if not s: return 0
    n = len(s)
    DP = [0 for _ in range(n + 1)]
    
    # Base case initialization
    DP[0] = 1
    DP[1] = 0 if s[0] == '0' else 1
    
    for i in range(2, n + 1):
      # One step jump
      if 0 < int(s[i - 1:i]) <= 9:
        DP[i] += DP[i - 1]
        
      # Two step jump
      if 10 <= int(s[i - 2:i]) <= 26:
        DP[i] += DP[i - 2]
    
    return DP[n]
  
class SolutionRef:
  def numDecodings(self, s):
    if not s: return 0
    
    n = len(s)
    DP = [0] * (n + 1)
    DP[0] = 1
    DP[1] = 1 if s[0] != '0' else 0
    
    for i in range(2, n + 1):
      if 1 <= int(s[i - 1: i]) <= 9:
        DP[i] += DP[i - 1]
        
      if 10 <= int(s[i - 2: i]) <= 26:
        DP[i] += DP[i - 2]
    
    print(DP)
    return DP[-1]
      
class Solution:
  def numDecodings(self, s):
    if not s: return 0
    
    n = len(s)
    DP = [0] * (n + 1)
    DP[0] = 1
    DP[1] = 1 if s[0] != '0' else 0
    
    for i in range(1, n):
      num1 = int(s[i: i + 1])
      num2 = int(s[i - 1: i + 1])
      
      if 1 <= num1 <= 9:
        DP[i + 1] += DP[i]
      
      if 10 <= num2 <= 26:
        DP[i + 1] += DP[i - 1]
    
    return DP[-1]
      
  
def runSolution():
  solution = Solution()
  print(solution.numDecodings(s = "12"))
  print(solution.numDecodings(s = "226"))
  print(solution.numDecodings(s = "06"))
  pass
runSolution()