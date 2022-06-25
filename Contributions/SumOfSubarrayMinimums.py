'''

  907. Sum of Subarray Minimums

  Input: arr = [3,1,2,4]
  Output: 17

  Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
  Minimums  are  3    1    2    4      1    1      2        1      1          1
  Sum is 17.

  --------------------------------------------------------------------------------------

  Contributions Strategy. Precompute boundaries to efficiently discover how each number
  contributes to the total end result.

  Ex.

  2   9   7   8   3   4   6   1
                  ^
  How often does 3 contribute to the overall result? 

  3 contributes to the overall result when 3 is the MINIMAL element with a subarray.

  Ex.

  2   9   7   8   3   4   6   1
              |   |                 In subarray [8,3], 3 is the minimal result, so it contributes here.

  2   9   7   8   3   4   6   1
              |       |             In subarray [8,3,4], 3 is the minimal result, so it contributes here.

  2   9   7   8   3   4   6   1
  |               |                 However, in subarray [2,9,7,8,3], 3 is NOT the minimal result, so no contribution

  Pattern? Find the boundaries in which 3 is the MINIMAL element.
  Boundary for 3 in which it is the MINIMAL element:

  2   9   7   8   3   4   6   1
  |                           |    We see that boundaries end at 2 and 1.
                                   If we include either 2 or 1 in our subarray, 3 is no longer the minimal element.

  So how can we find the boundaries for the PREVIOUS/NEXT LESSER ELEMENTS?

  -------------------------------------------------------------------------------------------------

  NOTE: PLE has to initialize to [1,2,3,4,etc...] to show the distance from start
        NLE has to initialize to [4,3,2,1,etc...] to show the distance from end
        But in the example below, we will simply use -1 to denote no PLE

  We can use a stack and build PLE (Previous Lesser Element) and NLE (Next Lesser Element)
  Start from the LEFT.

  2   9   7   8   3   4   6   1
  ^

  stack = [0]
  PLE   = [-1]

  Stack is empty, therefore it has no next lesser element. We push the INDEX.

  -------------------------------------------------------------------------------------------------

  2   9   7   8   3   4   6   1
      ^

  stack = [0, 1]
  PLE   = [-1, 0]

  Since stack.top has an element less than 9, we know stack.top is the next lesser element.

  -------------------------------------------------------------------------------------------------

  2   9   7   8   3   4   6   1
      ^

  stack = [0, 1]
  PLE   = [-1, 0]

  Since stack.top has an element less than 9, we know stack.top is the next lesser element.

  -------------------------------------------------------------------------------------------------

  2   9   7   8   3   4   6   1
          ^

  stack = [0, 1]
  PLE   = [-1, 0]

  Since stack.top has an element greater than 7, we should pop off stack.top.

  stack = [0]

  After popping, we see that the stack.top has an element less than curr (7). 
  Therefore that is the next lesser element. Update PLE  and push index onto the stack.
  
  stack = [0, 2]
  PLE   = [-1, 0, 0]

  -------------------------------------------------------------------------------------------------

  2   9   7   8   3   4   6   1
              ^

  stack = [0, 2]
  PLE   = [-1, 0, 0]

  stack.top has an element less than curr (7 < 8), therefore that is the next lesser element.

  stack = [0, 2, 3]
  PLE   = [-1, 0, 0, 2]

  -------------------------------------------------------------------------------------------------

  Eventually, it should look like this:

  2   9   7   8   3   4   6   1
                              ^

  stack = []
  PLE   = [-1, 0, 0, 2, 0, 4, 5, -1]

  -------------------------------------------------------------------------------------------------

  Once you get both PLE and NLE

    2   9   7   8   3   4   6   1
  [-1,  0,  0,  2,  0,  4,  5, -1]
  [ 7,  2,  4,  4,  7,  7,  7,  8]
                    ^
                    |
  The element 3 with index 4 has a boundary of 0 - 7

  Amount of left subarrays  = (i - PLE[i]) = (4 - 0) = 4
  Amount of right subarrays = (NLE[i] - i) = (7 - 4) = 3

  It's important to note that for every left subarray, it creates a multiplicative product
  with all right subarrays.
  
  Ex.

  2   9   7   8   3   4   6   1

  Say leftsubarray is [8,3]

  There are 3 (NLE[i] - i) right subarrays with 3 as minimal element.
  [8,3]
  [8,3,4]
  [8,3,4,6]

  Since we're adding the minimal value itself, every value will be:

  totalSubarrays = (i - PLE[i]) * (NLE[i] - i)
  totalValue     = minimalValue * totalSubarrays

  result += TotalValueOfMinimum

'''

def buildPLE(nums, n):
  stack = []
  PLE = [-1]  * n

  for i in range(n):
    curr = nums[i]
    while stack and curr < nums[stack[-1]]: stack.pop()    
    PLE[i] = (i - stack[-1]) if stack else (i + 1)
    stack.append(i)

  return PLE

def buildNLE(nums, n):
  stack = []
  count = 1
  NLE = [n] * n

  for i in range(n - 1, -1, -1):
    curr = nums[i]
    while stack and curr <= nums[stack[-1]]: stack.pop()
    NLE[i] = (stack[-1] - i) if stack else (count)
    stack.append(i)
    count += 1

  return NLE

def sumofSubarrayMinimums(nums):
  n = len(nums)

  PLE = buildPLE(nums, n)
  NLE = buildNLE(nums, n)

  print(PLE)
  print(NLE)

  totalSum = 0
  for i in range(n):
    totalSubarrays = PLE[i] * NLE[i]
    totalValue = nums[i] * totalSubarrays
    totalSum = (totalSum + totalValue) % (1e9 + 7)

  return int(totalSum)


class Solution:
  def buildPLE(self, nums, n):
    stack = []
    PLE = [-1]  * n

    for i in range(n):
      curr = nums[i]
      while stack and curr < nums[stack[-1]]: stack.pop()    
      PLE[i] = (i - stack[-1]) if stack else (i + 1)
      stack.append(i)

    return PLE

  def buildNLE(self, nums, n):
    stack = []
    count = 1
    NLE = [n] * n

    for i in range(n - 1, -1, -1):
      curr = nums[i]
      while stack and curr <= nums[stack[-1]]: stack.pop()
      NLE[i] = (stack[-1] - i) if stack else (count)
      stack.append(i)
      count += 1

    return NLE

  def sumofSubarrayMinimums(self, nums):
    n = len(nums)

    PLE = self.buildPLE(nums, n)
    NLE = self.buildNLE(nums, n)

    print(PLE)
    print(NLE)

    totalSum = 0
    for i in range(n):
      totalSubarrays = PLE[i] * NLE[i]
      totalValue = nums[i] * totalSubarrays
      totalSum = (totalSum + totalValue) % (1e9 + 7)

    return int(totalSum)


  
def runSolution():
  solution = Solution()
  print(solution.sumofSubarrayMinimums([71,55,82,55]))
  print(solution.sumofSubarrayMinimums([2, 9, 7, 8, 3, 4, 6, 1]))
  pass
runSolution()