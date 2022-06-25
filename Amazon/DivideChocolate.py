'''
  1231. Divide Chocolate

  https://leetcode.com/problems/divide-chocolate/solution/

  You have one chocolate bar that consists of some chunks. 
  Each chunk has its own sweetness given by the array sweetness.

  You want to share the chocolate with your k friends so you start 
  cutting the chocolate bar into k + 1 pieces using k cuts, each piece 
  consists of some consecutive chunks.

  Being generous, you will eat the piece with the minimum total 
  sweetness and give the other pieces to your friends.

  Find the maximum total sweetness of the piece you can get by cutting 
  the chocolate bar optimally.

  ----------------------------------------------------------

  Ex1:

  Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
  Output: 6
  Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

  ----------------------------------------------------------

  We want to use binary search to find the optimal cuts.
  The binary search range is the range of sweetness we should search.

  In this case, the minimum value of the binary search will be the smallest
  sweetness unit. It ensures that the smallest chunk is valid.

  For the maximum, we need to keep in mind that we want the SMALLEST piece after splitting.
  
  Therefore, it will be the sum of the sweetness divided by the chunks. sum/(k+1)
  It is the largest piece we can get for ourselves. Why? There is no way to possibly
  split the chunks into k + 1 yet have a piece greater than the sum/k+1 AND be the minimal piece.

  For instance, if you divide 2 by 2, the smallest possible piece will be 1, there's no way it can be 1.5

  sum(sweetness) = 45
  chunks = k + 1 = 6

  min = 1
  max = 45 / 6 = 7

  Now that we have our workable binary search range, we must determine how we binary search
  through the possible values.


  Sweetness:
  1   2   3   4   5   6   7   8   9

  Within our range (1 - 7), we can conduct a binary search to find a valid distribution in which
  each chunk is distributed with minimal value M.

  M = (R + L + 1)/2 = (7 + 0 + 1)/2 = 8/2 = 4

  -----------------------------------------------------

  M = 4. We will test how we can chunks with minimal value of 4.

  Sweetness:
  1   2   3   4   5   6   7   8   9
  |       |

  Chunks = 1
  Sum = 6
  -----------------------------------------------------

  Sweetness:
  1   2   3   4   5   6   7   8   9
            |   |

  Chunks = 2
  Sum = 4
  
  -----------------------------------------------------

  Sweetness:
  1   2   3   4   5   6   7   8   9
                |   |

  Chunks = 3
  Sum = 4

  -----------------------------------------------------

  Sweetness:
  1   2   3   4   5   6   7   8   9
                        |   |

  Chunks = 5
  Sum = 7

  -----------------------------------------------------

  Sweetness:
  1   2   3   4   5   6   7   8   9
                            |   |

  Chunks = 6
  Sum = 6
  
  -----------------------------------------------------

  Sweetness:
  1   2   3   4   5   6   7   8   9
                                |   |

  Chunks = 7
  Sum = 6

  Since it can split into >= k + 1 chunks, we can try raising the minimal value
  using binary search.

  etc...
'''

class SolutionRef:
  def divideChocolate(self, sweetnessArr, k):
    total = sum(sweetnessArr)
    L = min(sweetnessArr)
    R = total // (k + 1)

    while L < R:
      M = (L + R + 1) // 2
      cuts = 0
      curr = 0

      for sweetness in sweetnessArr:
        curr += sweetness

        if curr >= M:
          cuts += 1
          curr = 0
      
      if cuts >= k + 1: L = M
      else            : R = M - 1

    return L
  
class Solution:
  def divideChocolate(self, sweetnessArr, k):
    self.sweetnessArr, self.k = sweetnessArr, k
    L, R = min(sweetnessArr), sum(sweetnessArr)
    
    while L < R:
      M = L + (R - L + 1)//2
      
      if self.notFeasible(M): L = M
      else                  : R = M - 1
    
    return L  
  
  
  def notFeasible(self, minSweetness):
    chunks = 0
    curr = 0
    
    for sweetness in self.sweetnessArr:
      curr += sweetness
      
      if curr >= minSweetness:
        chunks += 1
        curr = 0
    
    return chunks < self.k + 1
    
  
def runSolution():
  solution = Solution()
  print(solution.divideChocolate([1,2,3,4,5,6,7,8,9], 5))
  # print(solution.divideChocolate([5,6,7,8,9,1,2,3,4], 8))
  # print(solution.divideChocolate([1,2,2,1,2,2,1,2,2], 2))
  pass
runSolution()