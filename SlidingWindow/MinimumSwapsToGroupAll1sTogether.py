'''

  1151. Minimum Swaps to Group All 1's Together
  
'''

class Solution:
  def minSwaps(self, data):
    totalOnes = data.count(1)
    L = R = currOnes = maxOnes = 0
    
    while R < len(data):
      currOnes += data[R]
      maxOnes = max(maxOnes, currOnes)
      R += 1
      
      if R >= totalOnes:
        currOnes -= data[L]
        L += 1
      
    return totalOnes - maxOnes
    
    
def runSolution():
  solution = Solution()
  print(solution.minSwaps(data = [1,0,1,0,1]))
  print(solution.minSwaps(data = [0,0,0,1,0]))
  print(solution.minSwaps(data = [1,0,1,0,1,0,0,1,1,0,1]))
  pass
runSolution()
