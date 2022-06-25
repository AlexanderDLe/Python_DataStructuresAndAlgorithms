'''

  926. Flip String to Monotone Increasing

 000110000
    ^----- Increment one
 ones = 1
 flips = 0
 
  ------------------------------- 

 000110000
     ^----- Increment one again
 ones = 2
 flips = 0
 
  ------------------------------- 
 
 000110000
      ^----- Increment flips
 ones = 2
 flips = 1  
 
  ------------------------------- 
 
 000110000
       ^----- Increment flips
 ones = 2
 flips = 2  
 
  ------------------------------- 
 
 000110000
        ^----- Increment flips
 ones = 2
 flips = 3  
 flips = min(ones, flips) = 2
 
  ------------------------------- 
 
 000110001
         ^----- Increment ones
 ones = 3
 flips = 2  
 flips = min(ones, flips) = 3
 
  ------------------------------- 
 
 0001100010
          ^----- Increment flips
 ones = 3
 flips = 4  
 flips = min(ones, flips) = 3
 
 Conceptual Summary:
 
  -------------------------------****** 
 
 When we process the next "char", we have two choices:
 1. If it's '1' - we can simply increment "ones", as it would meet the
    requirement of increasing.
 2. If it's '0' - we increment flips. 
 
 Now, we have two options. Either to flip the new zero to one or to flip all previous ones to zeros.
 Math.min(ones, flips) will make that decision. Taking ones will flip all ones, whereas taking flips
 will flip all zeroes encountering the one.
 
 0110001101 
  
'''

class Solution:
  def minFlipsMonoIncr(self, s):
    flips = ones = 0
    
    for char in s:
      if char == '1': ones += 1
      if char == '0': flips += 1
      flips = min(ones, flips)
      
    return flips
  
  
  
def runSolution():
  solution = Solution()
  print(solution.minFlipsMonoIncr("00110"))
  print(solution.minFlipsMonoIncr('010110'))
  print(solution.minFlipsMonoIncr('00011000'))
runSolution()