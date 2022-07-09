'''

  Given:

  2D matrix
  Start point
  End point
  Set of intermediate points
  
  Return number of paths from start to end which goes through all intermediate points. 
  You can only move upper right, right, and lower right.

  Clarification: A valid path is one that can go through any point but must go through 
  all intermediate points.
  
'''

from collections import defaultdict
from bisect import insort_left

class Solution:
  def main(self, A, S, X):
    invertedIndex = defaultdict(list)
    self.invertedIndex = invertedIndex
    
    for i, num in enumerate(A):
      invertedIndex[num].append(i)
    
    moves = 0
    currIndex = S
    
    while True:
      currVal = A[currIndex]
      targetVal = currVal + X
      isEven = currVal % 2 == 0

      if not self.exists(targetVal, isEven, currIndex): break
      
      self.removeIndex(A, currIndex, currVal)
      index = self.getIndex(A, targetVal, isEven, currIndex)
      A[currIndex] += X
      currIndex = index
      insort_left(self.invertedIndex[targetVal], index)
      
      moves += 1
    
    return moves

  def removeIndex(self, A, currIndex, currVal):
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