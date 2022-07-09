'''

  1088. Confusing Number II

'''

class Solution:
  def confusingNumberII(self, n):
    rotate180 = [(0, 0), (1, 1), (6, 9), (8, 8), (9, 6)]
    self.res = 0
    
    def DFS(num, numRotated, unit):
      if num != numRotated:
        self.res += 1
      
      arr = []
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
  

def runSolution():
  solution = Solution()
  print(solution.confusingNumberII(n = 20))
  print(solution.confusingNumberII(n = 100))
  pass
runSolution()