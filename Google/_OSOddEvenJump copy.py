'''

  Given an array of integer values:
  You will be given a 0-based start index S

  For each even value Ai, jump to the closest right index j such that Aj = Ai + 1
  For each odd value Ai, jump to the closest left index j such that Aj = Ai + 1
  Increment the value at Ai by a value X after making the jump
  Return the index at which no further jumps are possible

  Eg. A = [2, 1, 3, 7], S = 1, X = 1
  Output : 2

  Explanation:
  start at index 1, A[1]=1(odd value)
  look at closest index to the left which has value A[1] + 1 = 1 + 1 = 2 (i.e index 0)
  Increment A[1] by X = A[1] + 1 = 1 + 1 = 2
  Jump
  
  A = [2, 2, 3, 7]
  pointer at Index 0, A[0] = 2(even value)
  look at closest index to the right which has value A[0] + 1 = 2 + 1 = 3 (i.e index 2)
  Increment A[0] by X = A[0] + 1 = 2 + 1 = 3
  Jump
  
  A = [3, 2, 3, 7]
  pointer ar Index 2, A[2] = 3 (odd value)
  look at closest index to the left which has value A[2] + 1 = 3 + 1 = 4 (no such index exists)

  Return 2 (index at which we can no longer jump)
  
'''

from collections import defaultdict
from bisect import insort_left

class Solution:
  def main(self, A, S, X):
    self.invertedIndex = defaultdict(list)
    
    for i, num in enumerate(A):
      self.invertedIndex[num].append(i)
    
    moves = 0
    currIndex = S
    
    while True:
      currVal = A[currIndex]
      targetVal = currVal + X
      isEven = currVal % 2 == 0

      if not self.exists(targetVal, isEven, currIndex): break
      
      self.removeIndex(currIndex, currVal)
      index = self.getIndex(A, targetVal, isEven, currIndex)
      A[currIndex] += X
      currIndex = index
      insort_left(self.invertedIndex[targetVal], index)
      
      moves += 1
    
    return moves

  def removeIndex(self, currIndex, currVal):
    indices = self.invertedIndex[currVal]
    index = indices.index(currIndex)
    indices.pop(index)

  def getIndex(self, A, targetVal, isEven, currIndex):
    indices = self.invertedIndex[targetVal]
    L, R = 0, len(indices)
    
    while L < R:
      if isEven: M = L + (R - L)//2      
      else     : M = L + (R - L + 1)//2
      index = A[M]
      
      if isEven:
        if index <= currIndex: L = M + 1
        else                 : R = M
      
      else:
        if index >= currIndex: R = M - 1
        else                 : L = M
      
    return L
  
  

  def exists(self, targetVal, isEven, currIndex):
    indices = self.invertedIndex[targetVal]
    isOdd = not isEven
    
    if len(indices) == 0: return False
    if isEven and indices[-1] <= currIndex: return False
    if isOdd  and indices[0]  >= currIndex: return False
      
    return True
  
def runSolution():
  solution = Solution()
  print(solution.main(A = [2, 1, 3, 7], S = 1, X = 1))
  # print(solution.main(A = [2, 4, 4, 3, 5, 5, 5, 5, 5], S = 2, X = 1))
  pass
runSolution()