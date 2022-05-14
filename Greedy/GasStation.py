'''

  134. Gas Station
  
'''

class SolutionBruteForce:
  def canCompleteCircuit(self, gas, cost):
    self.n = len(gas)
    i = 0
    
    while i < len(gas):
      canComplete, endIndex = self.attemptCircuit(gas, cost, i)
      if canComplete: 
        return i
      else: 
        if i == endIndex: i += 1
        else: i = endIndex
    
    return -1
  
  def attemptCircuit(self, gas, cost, start):
    i = 0
    currGas = 0
    while i < self.n:
      index = (start + i) % self.n
      
      currGas += gas[index]
      currGas -= cost[index]
      
      if currGas < 0: return (False, index + 1)
      i += 1
    
    return (True, 0)

class Solution:
  def canCompleteCircuit(self, gas, cost):
    curr = total = diff = start = 0
    
    for i in range(len(gas)):
      diff = gas[i] - cost[i]
      total += diff
      curr  += diff
      
      if curr < 0:
        start = i + 1
        curr = 0
    
    if total >= 0: return start
    
    return -1


def runSolution():
  solution = Solution()
  print(solution.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
  print(solution.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
  pass
runSolution()
