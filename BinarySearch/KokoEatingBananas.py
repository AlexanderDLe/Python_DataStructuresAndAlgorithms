'''

  875. Koko Eating Bananas

'''

from math import ceil


class SolutionRef:
  def minEatingSpeed(self, piles, h):
    self.piles, self.h = piles, h
    L, R = 1, max(piles)
    
    while L < R:
      speed = L + (R - L)//2
      
      if self.isFeasible(speed): R = speed
      else                     : L = speed + 1
    
    return L
  
  def isFeasible(self, speed):
    hoursRequired = 0
    
    for pile in self.piles:
      hoursRequired += ceil(pile/speed)

    return hoursRequired <= self.h
  
class Solution:
  def minEatingSpeed(self, piles, h):
    self.piles, self.h = piles, h
    L, R = 1, max(piles)
    
    while L < R:
      rate = L + (R - L)//2
      if self.feasible(rate): R = rate
      else                  : L = rate + 1
    
    return L
      
  def feasible(self, rate):
    hoursRequired = 0
    
    for pile in self.piles:
      hoursRequired += ceil(pile / rate)
    
    return hoursRequired <= self.h
  
  
def runSolution():
  solution = Solution()
  print(solution.minEatingSpeed(piles = [3,6,7,11], h = 8))
  print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
  print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
  pass
runSolution()
