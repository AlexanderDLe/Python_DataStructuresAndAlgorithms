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
  P2 = [(3,1), (7,3), (12,0)]
  
  If same, then add and append to output.
  
  Output = [(0,0), (3,0)]
  
'''

class Solution:
  def main(self, P1, P2):
    n1, n2 = len(P1), len(P2)
    prevMem1 = prevMem2 = 0
    p = q = 0
    result = []
    
    while p < n1 or q < n2:
      if q == n2:
        result.append(P1[p])
        p += 1
        continue
    
      if p == n1:
        result.append(P2[q])
        q += 1
        continue
      
      time1, mem1 = P1[p]
      time2, mem2 = P2[q]
      
      if time1 == time2:
        result.append((time1, mem1 + mem2))
        p += 1
        q += 1
        prevMem1 = mem1
        prevMem2 = mem2
      
      elif time1 < time2:
        result.append((time1, mem1 + prevMem2))
        p += 1
        prevMem1 = mem1
      
      elif time1 > time2:
        result.append((time2, mem2 + prevMem1))
        q += 1
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