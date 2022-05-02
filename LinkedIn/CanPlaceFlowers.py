'''

  605. Can Place Flowers

'''


class Solution:
  def canPlaceFlowers(self, flowerbed, n):
    length = len(flowerbed)
    
    for i in range(len(flowerbed)):
        prev = flowerbed[i - 1] if i > 0 else 0
        curr = flowerbed[i]
        next = flowerbed[i + 1] if i < length - 1 else 0
        
        if prev + curr + next == 0:
          flowerbed[i] = 1
          n -= 1

    return n <= 0
        
  
  
def runSolution():
  solution = Solution()
  print(solution.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
  print(solution.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
  print(solution.canPlaceFlowers(flowerbed = [0,0,1,0,0], n = 1))
  pass
runSolution()