'''

  Given the stock prices of n months, the net price change for the i-th month 
  is defined as the absolute difference between the average of stock prices for 
  the first i months and for the remaining (n−i) months where 1≤i≤n.

  Note that these averages are rounded down to an integer.

  The average of a set of integers here is defined as the sum of integers divided 
  by the number of integers, rounded down to the nearest integer.
  
  Example:
  the average of [1, 2, 3, 4] is the floor of (1 + 2 + 3 + 4) / 4 = 2.5 and the floor of 2.5 is 2.

  Given an array of stock prices, find the month at which the net price change is minimum.
  If there are several such months, return the earliest month.

  Constraints:

  2 <= n <= 10^5

  1 <= stockPrice[i] <= 10^9

  -------------------------------------------------------------------
  
  [1,2,3,4,5,6]   totalSum = 21

'''

import math

class SolutionRef:
  def averageStockPrices(prices):
    n = len(prices)
    totalSum = sum(prices)
    currSum = 0
    minDiff = math.inf

    for i in range(n):
      currSum += prices[i]
      count = i + 1

      currentAverage = math.floor(currSum / count)
      remainingDivisor = (n - count) or 1
      remainingAverage = math.floor((totalSum - currSum) / (remainingDivisor))
      minDiff = min(minDiff, abs(currentAverage - remainingAverage))
    
    return minDiff

class Solution:
  def averageStockPrices(self, prices):
    n = len(prices)
    if n == 0: return 0
    
    minPriceChange = math.inf
    earliestMonth = 0
    totalSum = sum(prices)
    currSum = 0
    
    for i, price in enumerate(prices):
      currCount = i + 1
      remainingCount = max(1, n - i - 1)
      
      currSum += price
      currAvg = currSum//currCount
      
      remainderSum = totalSum - currSum
      remainderAvg = remainderSum//remainingCount
            
      priceChange = abs(currAvg - remainderAvg)
      if priceChange < minPriceChange:
        minPriceChange = priceChange
        earliestMonth = i
    
    return earliestMonth + 1
  
def runSolution():
  solution = Solution()
  print(solution.averageStockPrices([1,3,2,3]))
  pass
runSolution()
