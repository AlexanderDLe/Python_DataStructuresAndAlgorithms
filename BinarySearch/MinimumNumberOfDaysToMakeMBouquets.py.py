'''

  875. Koko Eating Bananas

'''


class SolutionMySolution:
  def minDays(self, bloomDay, m, k):
    if len(bloomDay) < (m * k): return -1
    
    self.bloomDay, self.m, self.k = bloomDay, m, k
    L, R = 1, max(bloomDay) + 1
    
    while L < R:
      days = L + (R - L)//2
      
      if self.isFeasible(days): R = days
      else                    : L = days + 1
    
    return L
  
  def isFeasible(self, days):
    bouquetsCreated = 0
    bloomedFlowers  = 0
    L = R = start = 0
    
    while R < len(self.bloomDay):
      if self.bloomDay[R] <= days:
        bloomedFlowers += 1
      R += 1
      if bloomedFlowers == self.k:
        bouquetsCreated += 1
        bloomedFlowers = 0
        start = L = R
        # Mistake: Don't forget to continue out of loop
        continue
      
      # Mistake: Don't forget that R >= start + self.k
      if R >= start + self.k:
        if self.bloomDay[L] <= days:
          bloomedFlowers -= 1
        L += 1
    
    return bouquetsCreated >= self.m
  
class Solution:
  def minDays(self, bloomDay, m, k):
    if len(bloomDay) < (m * k): return -1
    
    self.bloomDay, self.m, self.k = bloomDay, m, k
    L, R = 1, max(bloomDay)
    
    while L < R:
      days = L + (R - L)//2      
      if self.isFeasible(days): R = days
      else                    : L = days + 1
    
    return L
  
  def isFeasible(self, days):
    bouquets = flowers = 0
    
    for bloom in self.bloomDay:
      if bloom > days:
        flowers = 0
      else:
        flowers += 1
        
        if flowers == self.k:
          bouquets += 1
          flowers = 0
    
    return bouquets >= self.m
  
  
def runSolution():
  solution = Solution()
  # print(solution.minEatingSpeed(bloomDay = [1,10,3,10,2], m = 3, k = 1))
  # print(solution.minEatingSpeed(bloomDay = [1,10,3,10,2], m = 3, k = 2))
  print(solution.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))
  pass
runSolution()
