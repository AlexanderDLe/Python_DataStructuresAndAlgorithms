'''

  1648. Sell Diminishing-Valued Colored Balls

  5 >  4 >  3 >  2 >  1 >  0
  5    9   12   14   15
  
  
  
  3 > 2 > 1 > 0
  3   5   6   

'''

import heapq
import re

class SolutionBS:
  def maxProfit(self, inventory, orders):
    def getNumItems(M):
      sum = 0
      for item in inventory:
        sum += max(0, item - M)      
      return sum
    
    
    L, R = 0, max(inventory)
    
    while L < R:
      M = (L + R + 1)//2
      
      if getNumItems(M) >= orders: L = M
      else: R = M - 1
    
    
    ans = 0
    for item in inventory:
      if item <= L: continue
      ans += (item + L + 1)*(item - L)//2
      
    return (ans - (getNumItems(L) - orders) * (L + 1))
  
class Solution:
  def maxProfit(self, inventory, orders):
    inventory.sort(reverse=True)
    inventory.append(0)
    profit = 0
    width = 1
    
    for i in range(len(inventory)-1):
      if inventory[i] > inventory[i+1]:
        if width * (inventory[i] - inventory[i+1]) < orders:
          profit += width * self.sumRange(inventory[i+1]+1, inventory[i])
          orders -= width * (inventory[i] - inventory[i+1])
          
        else:
          whole, remaining = divmod(orders, width)
          profit += width * self.sumRange(inventory[i]-whole+1, inventory[i])
          profit += remaining * (inventory[i]-whole)
          break
      
      width += 1
      # print(width)
    return profit % (10**9 + 7)
        
  def sumRange(self, lo, hi):
    # inclusive lo and hi
    print('-----')
    print(hi, lo)
    print(((hi * (hi+1))), ((lo * (lo-1))))
    print(((hi * (hi+1)) // 2), ((lo * (lo-1)) // 2))
    print((hi * (hi+1)) // 2 - (lo * (lo-1)) // 2)
    return (hi * (hi+1)) // 2 - (lo * (lo-1)) // 2
    
    
    

  
def runSolution():
  solution = Solution()
  print(solution.maxProfit(inventory = [6,5,5,1], orders = 12))
  # print(solution.maxProfit(inventory = [3,5], orders = 6))
  pass
runSolution()
