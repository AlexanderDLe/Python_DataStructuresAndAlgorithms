'''

  31. Next Permutation

  Lexicographic ordering is the ordering in which smaller values appear before greater values.
  The ordering starts from ascending order and ends in descending order, ie.
  
  123 -> 321
  
  The next permutation in the lexicographic ordering is the order which has the 
  lowest possible greater value.
  
  For example
  
  Source = 123
  NextPermutation = 132 - not 213 which has a greater value.
  
  We can calculate the next permutation by using a pivot, swap, and reversal.
  
  
  ---------------------------------------

  pivot can start at -1, simply sort array if there is no pivot
  
  1. pivot is the last index whose value is smaller than the next value.
  2. swap  is the last index whose value is greater than the pivot value.
  3. Swap pivot and swap values and reverse the array starting from pivot + 1

  1  2  4  3
     p     s
     
  1  3  4  2
     p     s    <--- swap pivot and swap
     
  1  3  4  2
     p     s    <--- reverse pivot+1:end
     
  1  3  2  4
     p     s    <--- reverse pivot+1:end
     
  ---------------------------------------

  1  3  2  4
        p  s
        
  1  3  4  2
        p  s
     
  ---------------------------------------
        
  1  3  4  2
     p  s   
     
  1  4  3  2
     p  s
     
  1  4  2  3
     p  s
     
  ---------------------------------------
     
     
'''


class SolutionRef:
  def reverse(self, nums, L, R):
    print(nums,L, R)
    while L < R:
      nums[L], nums[R] = nums[R], nums[L]
      L += 1
      R -= 1

  def nextPermutation(self, nums):
    n = len(nums)
    
    pivot = -1
    for i in range(n - 1):
      if nums[i] < nums[i + 1]: pivot = i

    swap = -1
    for i in range(n):
      if nums[i] > nums[pivot]: swap = i

    if pivot == -1: 
      nums.sort()
      return

    nums[pivot],nums[swap] = nums[swap],nums[pivot]
    self.reverse(nums, pivot + 1, n - 1)
    return


class Solution:
  
  '''

    Time Complexity
    O(n) to iterate through nums
    
    Space Complexity
    O(1) not utilizing any scaling data structures
  
  '''
  
  def reverse(self, nums, L, R):
    while L < R:
      nums[L], nums[R] = nums[R], nums[L]
      L += 1
      R -= 1

  def nextPermutation(self, nums):
    n = len(nums)
    pivot, swap = -1, -1
    
    for i in range(n - 1):
      if nums[i] < nums[i + 1]: pivot = i
      
    for i in range(pivot + 1, n):
      if pivot == -1: break
      if nums[i] > nums[pivot]: swap = i
      
    if pivot == -1:
      nums.sort()
      return nums
    
    nums[pivot], nums[swap] = nums[swap], nums[pivot]
    self.reverse(nums, pivot + 1, n - 1)
    
    return nums
    
  
def runSolution():
  solution = Solution()
  print(solution.nextPermutation([1,2,4,3]))
  print(solution.nextPermutation([3,2,1]))
  print(solution.nextPermutation([1,1,5]))
  pass
runSolution()
