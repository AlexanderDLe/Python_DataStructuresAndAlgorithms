'''
  Given an array containing only 0 and 1 as its elements. 
  We have to sort the array in such a manner that all the 
  ones are grouped together and all the zeros are grouped 
  together. The group of ones can be either at the start 
  of the array or at the end of the array. 
  
  The constraint while sorting is that every one/zero can 
  be swapped only with its adjacent zero/one. Find the 
  minimum number of moves to sort the array as per the description.
  
  --------------------------------------------------------------
  
  Example:
  input array = [0,1,0,1]
  Final array = [0,0,1,1]
  Minimum moves = 1 (1 at index 1 is swapped with 0 at index 2)

  input array = [1101]
  Final array - [1110]
  Minimum moves = 1 [1 at index 2 is swapped with index 3]
  
  -------------------------------------------------------------
  
  Swap via 0 compared to swap via 1.
  
  Swapping via 0. If 0, increment curr, else total += curr
  
  0 0 1 0 0 1
      ^
  
  curr  = 2
  total = 2
  
  ----------------
  
  0 0 1 0 0 1 <-- Why do we increment 2 here? Imagine we actually swap this.
      ^
  
  0 0 1 0 0 1 <-- Because we want to swap this one to the other side.
  0 1 0 0 0 1
  1 0 0 0 0 1
    
  1 0 0 0 0 1 <-- Logically leaves off here. Requires two adjacent swaps.
      ^

  ---------------
      
  1 0 0 0 0 1 
        ^
  
  curr  = 3
  total = 2
  
  ---------------
      
  1 0 0 0 0 1 
          ^
  
  curr  = 4
  total = 2
  
  ---------------
      
  1 0 0 0 0 1   <-- Now we increment total by curr.
            ^
  
  curr  = 4
  total = 2
  
  (after)
  
  curr  = 4
  total = 6
  
  ---------------
      
  1 0 0 0 0 1   <-- We increment by 4 here because we want to 
            ^       swap this one to the other side.
  
  curr  = 4
  total = 2
  
  (after)
  
  curr  = 4
  total = 6
  
  
'''

class Solution:
  def func(self, nums):
    self.nums = nums
    return min(self.group(0), self.group(1))
  
  def group(self, val):
    totalSwaps = currSwaps = 0
    print('')
    for num in self.nums:
      if num == val: currSwaps += 1
      else         : totalSwaps += currSwaps
      print(currSwaps, totalSwaps)
    
    return totalSwaps

  
def runSolution():
  solution = Solution()
  print(solution.func(nums = [0,0,1]))
  # print(solution.func(nums = [0,1,1,1,0]))
  # print(solution.func(nums = [1,1,0,1]))
  # print(solution.func(nums = [1,1,0,1,1]))
  # print(solution.func(nums = [1,1,1,0,1]))
  # print(solution.func(nums = [1,0,1,0,1]))
  pass
runSolution()