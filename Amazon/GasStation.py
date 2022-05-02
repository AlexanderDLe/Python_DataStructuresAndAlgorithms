'''

  132. Gas Station

'''


class Solution:
  def canCompleteCircuit(self, gas, cost):
    n = len(gas)
    startIdx = 0
    
    while startIdx < n:
      currPos = 0
      currGas = gas[startIdx]
      
      while currPos < n:
        currIdx = (startIdx + currPos) % n
        nextIdx = (currIdx + 1) % n
        
        currGas -= cost[currIdx]
        if currGas < 0: break
        currGas += gas[nextIdx]      
        
        currPos += 1
        if currPos == n: return startIdx
      
      startIdx += (currPos + 1)
    
    return -1
  
def runSolution():
  solution = Solution()
  print(solution.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
  print(solution.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
  pass
runSolution()