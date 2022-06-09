'''

  1011. Capacity to Ship Packages Within D Days

'''

class SolutionRef:
  def shipWithinDays(self, weights, days):
    self.days, self.weights = days, weights
    L, R = max(weights), sum(weights)
    
    while L < R:
      M = L + (R - L)//2      
      if self.isFeasible(M): R = M
      else                 : L = M + 1
    
    return L
  
  def isFeasible(self, capacity):
    daysRequired = 1
    currWeight   = 0
    
    for weight in self.weights:
      currWeight += weight
      
      if currWeight > capacity:
        daysRequired += 1
        currWeight = weight
    
    return daysRequired <= self.days
  
class Solution:
  def shipWithinDays(self, weights, days):
    self.days, self.weights = days, weights
    L, R = max(weights), sum(weights)
    
    while L < R:
      capacity = L + (R - L)//2
      if self.isFeasible(capacity): R = capacity
      else                        : L = capacity + 1
    
    return L

  
  def isFeasible(self, capacity):
    daysRequired = 1
    currWeight = 0
    
    for weight in self.weights:
      currWeight += weight
      
      if currWeight > capacity:
        currWeight = weight
        daysRequired += 1
    
    return daysRequired <= self.days
  
  
def runSolution():
  solution = Solution()
  print(solution.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
  print(solution.shipWithinDays(weights = [3,2,2,4,1,4], days = 3))
  print(solution.shipWithinDays(weights = [1,2,3,1,1], days = 4))
  pass
runSolution()
