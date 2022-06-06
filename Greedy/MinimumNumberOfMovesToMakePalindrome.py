'''

  2193. Minimum Number of Moves to Make Palindrome

  letelt
  L    R
  
  When unmatched, you want to find the closest match for each side.
  In this case: We want to find the closest 'l' to the right and the
  closest 't' to the left.
  
  
  letelt
  L | |R
    j i <- Swap R and i
    
  letetl
   L  R
    ji  <- Swap L and j
  
  lteetl
    
'''

class Solution:
  def minMovesToMakePalindrome(self, s):
    s = list(s)
    n = len(s)
    count = 0
    
    for L in range(n // 2):
      R = n - L - 1
      
      if s[L] != s[R]:      
        i, j = L, R
        
        while s[j] != s[L]: j -= 1
        while s[i] != s[R]: i += 1
        distanceToL = i - L
        distanceToR = R - j
        
        if distanceToL < distanceToR:
          count += distanceToL
          for x in range(i, L, -1):
            s[x] = s[x - 1]
            
        else:
          count += distanceToR
          for x in range(j, R):
            s[x] = s[x + 1]
    
    return count
      
      


def runSolution():
  solution = Solution()
  print(solution.minMovesToMakePalindrome(s = "aabb"))
  print(solution.minMovesToMakePalindrome(s = "letelt"))
  pass
runSolution()
