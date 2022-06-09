'''

  634. Find the Derangement of An Array

  Let D(N) be the required answer. 
  
  The recursion for the number of derangements of N is: 
  D(N) = (N-1) * (D(N-1) + D(N-2)). 
  
  With this recursion in hand, the problem becomes similar to finding 
  the N-th fibonacci number.

  ---------------------------------

  To prove it, suppose there are people and hats labelled 1...N. 
  
  We want the number of ways to put a hat on each person such that no 
  person is wearing their hat. 
  
  The first person has N-1 choices to put on a hat, say he wears hat X. 
  Now consider what hat person X is wearing. 
  
  Either he takes hat 1, and we have D(N-2) ways to arrange the remaining 
  hats among people; or he doesn't take hat 1, which if we relabelled it 
  as hat X, would have D(N-1) ways to arrange the remaining hats.
  
  ---------------------------------
  
  Example:
  
  [1, 2, 3, 4, 5, 6]
   ^
  Person one has 5 (n-1) other hats he can try.
  Say he wears 2's hat.
  
   swap hats
   V  V
  [1, 2, 3, 4, 5, 6]
  
  Person 2 is wearing person 1's hat.
  Now that he's wearing hat 1, he has 4 (n-2) other hats he can try.
  
'''

class Solution:
  def findDerangement(self, n):
    if n < 2: return 0
    mod = 10 ** 9 + 7
    
    DP = [0] * (n + 1)
    DP[2] = 1
    
    for i in range(3, n + 1):
      DP[i] = (i - 1) * (DP[i - 1] + DP[i - 2]) % mod
      
    return DP[-1]
  
def runSolution():
  solution = Solution()
  print(solution.findDerangement(n = 3))
  print(solution.findDerangement(n = 2))
  print(solution.findDerangement(n = 4))
  pass
runSolution()