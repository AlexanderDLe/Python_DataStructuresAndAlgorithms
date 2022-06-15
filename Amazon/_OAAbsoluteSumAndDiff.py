'''

  You are given the following integer N, array A of length N, integer x.
  Given a single non-negative integer x, determine the count of pairs (i,j) where 
  
  1. 1 <= i < j <= N 
  2. | Ai + Aj | + | Ai - Aj | >=x.
  
  Here |x| denotes the absolute value of x. For example |-3| = 3.

  -------------------------------------------------------------------
  
  Example 1

  N = 3, A = [7, 8, 9], x=17

  i=1 and j=2: | Ai + Aj | + | Ai - Aj | = 16
  i=1 and j=3: | Ai + Aj | + | Ai - Aj | = 18
  i=2 and j=3: | Ai + Aj | + | Ai - Aj | = 18
  
  Therefore, 2 such pairs exist.
  
  -------------------------------------------------------------------
  
  Example 2
  
  N = 2, A = [4, 5], x=12
  
  i=1 and j=2: | Ai + Aj | + | Ai - Aj | = 10

  Therefore, no such pair which gives a value greater than or equal to 'x'.
  Therefore, No such pairs exist.

  -------------------------------------------------------------------
  
  the above problem can be solved in O(n) time complexity

  large : larger number 
  small : smaller number
  
  (large + small) + (large-small) >= x      <-- The small number cancels out
  (large) + (large) >= x
  (large) * 2 >= x

  Therefore x is independent of the smaller number
  Thus large can be paired with any number to get x
  
  --------------
  
  Say x = 21. In order for a pair to be >= 21, the value of large must be 11. Why? 
  
  If large == 11, then (11 * 2) = 22, which is >= x
  If large == 10, then (10 * 2) = 20, which is <  x
  
  Therefore, the minimum large value should be at least half of x.
    
  The minimum value of large should be (x+1)/2 // Lmin = (x+1)/2  
  
  Now just traverse the array and calculate numbers greater than or equal to Lmin

  i) all numbers >= Lmin can be paired with numbers <Lmin // (count of num >= Lmin) * (count of num <Lmin)
  ii) all numbers >= Lmin can be paired within themselves // (count of num >= Lmin)C2

  return (i)+(ii)
  
  ---------------------------------------------------------------
  
  Example
  
  [7, 8, 9] x = 17
  
  Lmin = (17 + 1)//2 = 18//2 = 9
  Therefore all pairs that include 9 will be valid.
  
  In [7, 8, 9], there is one 1 Lmin out of 3 total numbers.
  
  
'''


from collections import defaultdict


class Solution:
  def sumOfSumDiff(self, nums, x):
    n = len(nums)
    minVal = (x + 1) // 2
    minCount = 0
    
    for num in nums:
      if num >= minVal: minCount += 1
    
    pairsWithSmalls = minCount * (n - minCount)
    pairsWithLmins  = self.getPairsAmongCount(minCount)

    return pairsWithSmalls + pairsWithLmins
  
  
    
  def getPairsAmongCount(self, count):
    if count <= 1: return 0
    possibilities = self.fact(count)
    possibilitiesWithoutOne = self.fact(count - 1)
    return (possibilities * possibilitiesWithoutOne)/2
  
  def fact(self, n):
    if n == 0: return 1
    return n * self.fact(n - 1)
    
  
def runSolution():
  solution = Solution()
  print(solution.sumOfSumDiff(nums = [16, 18, 15, 29], x=20))
  # print(solution.sumOfSumDiff(nums = [7, 8, 9], x=17))
  # print(solution.sumOfSumDiff(nums = [4, 5], x=12))
  pass
runSolution()
