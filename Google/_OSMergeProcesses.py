'''

  Given two processes P1 and P2 with their memory consumption graphs wrt time. (timestamp, memory)
  Output Ps = P1 + P2

  -----------------------------------------------------
  
  Example
  P1 = [(0,0), (5,2), (10,0)]
  P2 = [(0,0), (3,1), (7,3), (12,0)]

  Ps = [(0,0), (3,1), (5,3), (7,5), (10,3), (12,0)]
  
  -----------------------------------------------------
          v
  P1 = [(0,0), (5,2), (10,0)]
          v
  P2 = [(0,0), (3,1), (7,3), (12,0)]
  
  If same, then add and append to output.
  
  Output = []
  -----------------------------------------------------
  
        prev1    v
  P1 = [(0,0), (5,2), (10,0)]
        prev2    v
  P2 = [(0,0), (3,1), (7,3), (12,0)]
  
  If different times, then check if there is an overlapping
  process then add earlier time to output.
  
  In this case, the previous P1 process if (0,0), so there is
  not memory allocated for P1 at the time (3,1) takes place.
  
  Output = [(0,0), (3,1)]
  
  -----------------------------------------------------
  
        prev1    v
  P1 = [(0,0), (5,2), (10,0)]
               prev2    v
  P2 = [(0,0), (3,1), (7,3), (12,0)]
  
  If different times, then check if there is an overlapping
  process then add earlier time to output.
  
  Here, (5,2) is earlier than (7,3), so it is next. The previous
  P2 process is (3,1) and is still ongoing. Therefore it overlaps by 1.
  
  Output = [(0,0), (3,1)]
  
'''

class Solution:
  def main(self, P1, P2):
    n1, n2 = len(P1), len(P2)
    prevMem1 = prevMem2 = 0
    p1 = p2 = 0
    result = []
    
    while p1 < n1 or p2 < n2:
      if p2 == n2:
        result.append(P1[p1])
        p1 += 1
        continue
    
      if p1 == n1:
        result.append(P2[p2])
        p2 += 1
        continue
      
      time1, mem1 = P1[p1]
      time2, mem2 = P2[p2]
      
      if time1 == time2:
        result.append((time1, mem1 + mem2))
        p1 += 1
        p2 += 1
        prevMem1 = mem1
        prevMem2 = mem2
      
      elif time1 < time2:
        result.append((time1, mem1 + prevMem2))
        p1 += 1
        prevMem1 = mem1
      
      elif time1 > time2:
        result.append((time2, mem2 + prevMem1))
        p2 += 1
        prevMem2 = mem2
    
    return result
      

def runSolution():
  solution = Solution()
  print(solution.main(
    P1 = [(0,0), (5,2), (10,0)],
    P2 = [(0,0), (3,1), (7,3), (12,0)]
  ))
  pass
runSolution()