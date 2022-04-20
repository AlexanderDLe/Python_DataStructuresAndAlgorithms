'''

  528. Random Pick with Weight


   0  1  2   3
  [1, 4, 6, 10]

  L = 0, R = 3

  M = (L + R + 1)//2 = (0 + 3 + 1)//2 = 4/2 = 2

  ---------------------------------------------

   0  1  2   3
  [1, 4, 6, 10]
   L     M   R

  val = 6
  
  ---------------------------------------------

   0  1  2   3
  [1, 4, 6, 10]
   L     M   R

  val = 6


'''

import math
from random import randrange


class Solution:
  def __init__(self, w):
    self.sums = []
    self.total = 0

    for weight in w:
      self.total += weight
      self.sums.append(self.total)

  def pickIndex(self):
    sums, total = self.sums, self.total
    rand = randrange(0, total)
    
    print(sums)
    print(rand)

    L, R = 0, len(sums)
    while L < R:
      M = (L + R)//2
      curr = sums[M]
      print(f'------------------------')
      print(f'L: {L} | M: {M} | R: {R} | curr: {curr}')

      if rand < curr  : R = M
      if rand >= curr : L = M + 1

    return L


solution = Solution([2,1,4,5])
print(solution.pickIndex())