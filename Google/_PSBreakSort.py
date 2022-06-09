'''

  Given an arry arr of n positive integers, the following operations can be performed 0 or more times:

  Choose an index i where 0<=i<n
  choose 2 integers, x and y, such that x+y=arr[i]
  replace arr[i] with two elements, the two values x and y
  Determine the minimum number of operations required to sort the array.

  _____________________________________________________________________________
  
  Example

  input = [3,4,3]

  [3,4,3] -> [1,2,4,3] -> [1,2,2,2,3]

  return 2 (the array cannot be sorted in fewer than 2 operations)

  _____________________________________________________________________________

  Constraints

  No zeroes. Unless leading zeroes, they will break.
  No negatives. Negatives between positives will break.

  _____________________________________________________________________________


  Strategy

  [5,4,3]
      ^
  Start from the end since it is in ascending order.

  [5,4,3]
    ^
  Since 4 is greater than next (3 on right), then we must break this to keep ascending order.

  The goal is to break it in such a way that for (x + y) = 4, it satisfies the condition that y <= next. 
  In this case we also want the greatest x possible because we want the greatest "next" possible for next iteration. 

  4 can break into (3 + 1), (1 + 3) or (2 + 2), however, we choose (2 + 2) because 2 will be 
  the greater next for the next iteration. 
  
  Having a greater next for the next iteration is necessary because we want to least breaks possible, 
  and a smaller next will require more breaks.

  [5,4,3]
    ^
  Once we determine the x that we need, we can add x to the left of curr.

  [5,2,2,3]
      ^

  [5,2,2,3]
    ^

  [5,2,2,3]
  ^
  Here 5 is greater than next (2). Valid operations are (4 + 1) or (3 + 2).
  Edge case: If this is the last item, we want the smallest x possible that still satisfies the condition.

  [3,2,2,2,3]
    ^

  [3,2,2,2,3]
  ^

  Break into (1 + 2)
  [1,2,2,2,2,3]
  ^

  (Assume y <= next)
  1. If curr is first element, break in such a way that x is least
  2. If curr is not first, break in such a way that x is greatest

  _____________________________________________________________________________
  
    
  5, 2, True
  x = 1, y = 4 return (1, 4)
  x = 2, y = 3 return (2, 3)
  x = 3, y = 2 return (3, 2)
  x = 4, y = 1 return (4, 1)


  5, 2, False
  x = 4, y = 1 return (4, 1)
  x = 3, y = 2 return (3, 2)
  x = 2, y = 3 return (2, 3)
  x = 1, y = 4 return (1, 4)


'''

class Solution:
  def getXandY(self, curr, next, isFirst):
    print(curr, next, isFirst)
    if isFirst:
      for x in range(1, curr):
        y = curr - x
        if y <= next: return (x, y)

    else:
      for x in range(curr - 1, 0, -1):
        y = curr - x
        if y <= next: return (x, y)
  
  def minOperations(self, arr):
    n = len(arr)
    i = n - 2
    res = 0

    while i >= 0:
      curr, next = arr[i], arr[i + 1]

      if curr <= next:
        i -= 1
        continue

      if curr > next:
        x, y = self.getXandY(curr, next, i == 0)
        res += 1

        arr[i] = y
        arr.insert(i, x)

    print(arr)
    return res



  
def runSolution():
  solution = Solution()
  print(solution.minOperations([5,4,3]))
  # print(solution.minOperations([3,4,3]))
  # print(solution.minOperations([1,2,3]))
  pass
runSolution()