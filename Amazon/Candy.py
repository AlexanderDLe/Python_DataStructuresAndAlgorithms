'''

  135. Candy

ratings:  1  0  2  3  1  2  2
candy  :  2  1  2  3  1  2  1

'''



class Solution:
  def candy(self, ratings):
    n = len(ratings)
    candy = [1] * n
    
    for i in range(1, n):
      prev = ratings[i - 1]
      curr = ratings[i]
      if curr > prev: candy[i] = candy[i - 1] + 1
    
    for i in range(n - 2, -1, -1):
      next = ratings[i + 1]
      curr = ratings[i]
      # Mistake: Prevent overriding of possible greater value - use max condition
      if curr > next: candy[i] = max(candy[i], candy[i + 1] + 1)
    
    print(ratings)
    print(candy)
    
    return sum(candy)
  
  

def runSolution():
  solution = Solution()
  # print(solution.candy([1,0,2]))
  # print(solution.candy([1,2,2]))
  print(solution.candy([1,3,4,5,2]))
  pass
runSolution()
