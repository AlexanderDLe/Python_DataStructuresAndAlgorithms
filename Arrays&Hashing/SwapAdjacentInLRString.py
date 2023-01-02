'''

  777. Swap Adjacent in LR String

'''


from collections import deque


class Solution:
  def canTransform(self, start, end):
    if len(start) != len(end): return False
    
    # check L R orders are the same
    if start.replace('X', '') != end.replace('X', ''): return False
    
    n = len(start)
    
    Lstart = [i for i in range(n) if start[i] == 'L']
    Lend   = [i for i in range(n) if end[i]   == 'L']
    Rstart = [i for i in range(n) if start[i] == 'R']
    Rend   = [i for i in range(n) if end[i]   == 'R']
    
    # Check L positions are correct
    for i, j in zip(Lstart, Lend):
      print('L:', i, j)
      if i < j: return False
      
    # Check R positions are correct
    for i, j in zip(Rstart, Rend):
      print('R:', i, j)
      if i > j: return False
    
    return True
    
  

def runSolution():
  solution = Solution()
  print(solution.canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))
  print(solution.canTransform(start = "X", end = "L"))
  print(solution.canTransform(start = "XXXXXLXXXX", end = "LXXXXXXXXX"))
  pass
runSolution()