'''

  As part of a stock clearance exercise at an Amazon store, given many piles
  of fresh products, follow the rules given to stack the products in order.
  
  - There are a total of n piles of products
  
  - The number of products in each pile if represented by the array numProducts
  
  - Select any subarray from the array numProducts and pick up products from that
    subarray such that the number of products you pick from the ith pile is strictly
    less than the number of products you pick from the ith + 1 pile for all indices
    i of the subarray.
    
  Find the maximum number of products that can be picked
  
  --------------------------------------------------------------------------------
  
  Example:
  numProducts = [7, 4, 5, 2, 6, 5]
  
  There are some ways strictly increasing subarrays can be chosen (1-based index):
  
  Option 1 - Choose subarray from indices (1, 3) and products [3,4,5] respectively from each index.
    [7, 4, 5, 2, 6, 5] 
     3  4  5           <--- Select 12 total (strictly increasing)
     
  Option 2 - Choose subarray from indices (3,6) and pick products [1,2,4,5]
    [7, 4, 5, 2, 6, 5] 
           1  2  4  5  <---- Select 12 total
  
  --------------------------------------------------------------------------------

  [7, 4, 5, 2, 6, 5]
  
  

'''

from collections import deque


class SolutionBruteForce:
  def stackProducts(self, products):
    maxVal = 0
    
    for i in range(len(products) - 1, -1, -1):
      maxVal = max(maxVal, self.helper(products, i))
    
    return maxVal
  
  def helper(self, products, end):
    num  = products[end]
    curr = products[end]
    
    if end == 0: return num
    
    for i in range(end - 1, -1, -1):
      if products[i] >= curr: curr = curr - 1
      else                  : curr = products[i]
      num += curr
      
      if curr == 0: break
    
    return num
  
class Solution:
  def stackProducts(self, products):
    n = len(products)
    ans = products[-1]
    maxAns = last = ans
    
    for i in range(n - 2, -1, -1):
      curr, next = products[i], products[i + 1]
      print('---')
      print(curr, next)
      
      if curr > next:
        # If curr is greater than (ans + next - 1) combined, then just restart
        if curr > (ans + next - 1):
          ans = curr
          last = curr
        
        # Otherwise, decrement ans
        else:
          ans += next - 1
          last = next - 1
      else:
        if last == 1:
          ans = curr
          last = curr
        else:
          ans += min(curr, last - 1)
          last = min(curr, last - 1)
      
      print(ans)
      maxAns = max(maxAns, ans)
    
    return maxAns
  
def runSolution():
  solution = Solution()
  print(solution.stackProducts([2, 7, 4, 5, 2, 6, 5]))
  pass
runSolution()