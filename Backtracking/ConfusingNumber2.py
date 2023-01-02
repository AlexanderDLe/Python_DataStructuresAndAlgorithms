'''

  1088. Confusing Number II

'''

class SolutionRef:
  def confusingNumberII(self, n):
    rotate180 = [(0, 0), (1, 1), (6, 9), (8, 8), (9, 6)]
    self.res = 0
    
    def DFS(num, numRotated, unit):
      arr = []
      if num != numRotated:
        self.res += 1
      
      for digit, digitRotated in rotate180:
        if digit == 0 and num == 0: continue # Skip Infinite Zero
        if num * 10 + digit > n: break       # Over N already
        
        nextNum = (num * 10) + digit
        nextNumRotated = (digitRotated * unit) + numRotated
        arr.append((nextNum, nextNumRotated))
        DFS(nextNum, nextNumRotated, unit * 10)
    
      if arr: print(arr)
      
    DFS(0, 0, 1)
    return self.res

class Solution:
  def confusingNumberII(self, n):
    rotate180 = [(0, 0), (1,1), (6,9), (8, 8), (9, 6)]
    
    def DFS(num, numRotated, unit):
      if num != numRotated: self.res += 1
      
      for digit, rotatedDigit in rotate180:
        if num == 0 and digit == 0: continue
        if (num * 10) + digit > n: break
        
        nextNum = (num * 10) + digit
        nextRotated = (rotatedDigit * unit) + numRotated
        DFS(nextNum, nextRotated, unit * 10)
    
    self.res = 0
    DFS(0, 0, 1)    
    return self.res
  

def runSolution():
  solution = SolutionRef()
  # print(solution.confusingNumberII(n = 20))
  print(solution.confusingNumberII(n = 100))
  pass
runSolution()