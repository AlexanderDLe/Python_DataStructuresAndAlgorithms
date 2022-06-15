'''

  Determine all possible segments, where a segment has: max - min <= k. 
  
  You are given k and a list of numbers. A segment is a consecutive subarray of the list.

  Ex:

  [3,7,12,8,4,1,10] k = 4

  Valid segments that are those where max-min is less than or equal to 4:

  [3, 7]  = 7  - 3  = 4 <= 4  <--- Valid
  [12, 8] = 12 - 8  = 4 <= 4  <--- Valid
  [8, 4]  = 8  - 4  = 4 <= 4  <--- Valid
  [4, 1]  = 4  - 1  = 3 <= 4  <--- Valid
  ... + all lone nums         <--- Valid

  Valid segments = [3,7], [12,8], [8, 4], [4,1], [3], [7], [12]...

  --------------------------------------------------------------------------------

  Sliding window approach utilized for non-overlapping solution.
  However, the overlapping solution is more difficult.

  --------------------------------------------------------------------------------

  Contributions Method:

  Instead of n^2 solution where we create nested loops, we can use preprocessing to
  discover the valid contributions each number can make.

  [3,7,12,8,4,1,10] k = 4

  Ex.

  3  can make 2 contributions = [3] and [3, 7]. However, once it reaches 12, it can no longer contribute.
  7  can make 2 contributions = [7] and [3, 7]. However we can see that [3,7] is duplicated.
  12 can make 2 contributions = [12] and [12, 8].
  8  can make 3 contributions = [8], [12,8], and [8,4]. [12,8] is a duplicate.
  4  can make 2 contributions = [4], [4, 1].
  1  can make 2 contributions = [1], [4, 1]. [4, 1] is a duplicate.
  10 can make 1 contribution  = [10]

  To avoid make duplicates, we can focus on the contribution of nums[i] and its subsequent contributions.

  Example: at num 8, we can focus on [8] and [8, 4] - and not [12, 8]

  However, how can we form boundaries so that each ith position knows when it can no longer contribute?
  
  3  7  12  8  4  1  10
            |  |<-------------- 8 needs to know ahead of time the subsequent position in which it can't contribute.

  ---------------------------------------------------------------------------------

  BEGIN SAMPLE OPERATION
  Data Structure: QUEUE
  
  3  7  12  8  4  1  10
         ^

  contributionsArray
  []

  queue<(index, value)> = [
    (0, 3),
    (1, 7),
  ]

  (0, 3) is pushed since queue is empty. 
  (1, 7) is pushed because abs(7 - 3) < k (4)

  ---------------------------------------------------------------------------------

  3  7  12  8  4  1  10
         ^

  curr = (2, 12)

  queue<(index, value)> = [
    (0, 3),
    (1, 7),
  ]

  At (2, 12), we see that the value (12) is greater than the front of the the queue by at least k (4)
  (12 - 3) = 9 and 9 > 4 = TRUE
  Therefore, the jth position for (0, 3) is the current index 2 
  
  (optional: Include index of 12 because it can help subtraction later)

  --------------------------

  contributionsArray
  [2]

  queue<(index, value)> = [
    (1, 7),
  ]

  At (2, 12), we still see that the value (12) is greater than the front of the the queue by at least k (4)
  (12 - 7) = 5 and 5 > 4 = TRUE
  Therefore, the jth position for (1, 7) is the current index 2

  --------------------------

  contributionsArray
  [2, 2]

  queue<(index, value)> = [
    (2, 12)
  ]

  Since queue is empty, we can simply push it into the queue.

  ---------------------------------------------------------------------------------

  3  7  12  8  4  1  10
            ^

  contributionsArray
  [2, 2]

  curr = (3, 8)

  queue<(index, value)> = [
    (2, 12)
  ]

  We see the abs Diff of 12 - 8 is <= k (4), therefore we can push next into queue.

  ---------------------------------------------------------------------------------

  3  7  12  8  4  1  10
               ^

  contributionsArray
  [2, 2]

  curr = (4, 4)

  queue<(index, value)> = [
    (2, 12)
    (3, 8)
  ]

  We see the abs Diff of 4(curr) - 12(frontOfQueue) is > k (4), therefore 12 can no longer contribute.
  Set frontOfQueue's index to current index (4)

  contributionsArray
  [2, 2, 4]

  ---------------------------------------------------------------------------------

  3  7  12  8  4  1  10
               ^

  queue<(index, value)> = [
    (3, 8)
    (4, 4)
  ]

  We see the abs Diff of 4(curr) - 8(frontOfQueue) is <= k (4), therefore we can keep frontOfQueue and push curr.

  contributionsArray
  [2, 2, 4]

  ---------------------------------------------------------------------------------

  3  7  12  8  4  1  10
                  ^

  curr: (5, 1)

  queue<(index, value)> = [
    (3, 8)
    (4, 4)
  ]

  We see the abs Diff of 1(curr) - 8(frontOfQueue) is > k (4), therefore 8 can no longer contribute
  Remove frontOfQueue and update contributions array

  contributionsArray
  [2, 2, 4, 5]

  ---------------------------------------------------------------------------------

  3  7  12  8  4  1  10
                  ^

  curr: (5, 1)

  queue<(index, value)> = [
    (3, 8)
    (4, 4)
  ]

  We see the abs Diff of 1(curr) - 8(frontOfQueue) is > k (4), therefore 8 can no longer contribute
  Remove frontOfQueue and update contributions array

  contributionsArray
  [2, 2, 4, 5]

  ---------------------------------------------------------------------------------

  3  7  12  8  4  1  10
                      ^

  curr: (6, 10)

  queue<(index, value)> = [
    (4, 4)
    (5, 1)
  ]

  We see the abs Diff of 10(curr) - 4(frontOfQueue) is > k (4), therefore 4 can no longer contribute
  Remove frontOfQueue and update contributions array

  contributionsArray
  [2, 2, 4, 5, 6]

  -----------------------

  We see the abs Diff of 10(curr) - 1(frontOfQueue) is > k (4), therefore 1 can no longer contribute
  Remove frontOfQueue and update contributions array

  queue<(index, value)> = [
    (5, 1)
  ]

  contributionsArray
  [2, 2, 4, 5, 6, 6]

  -----------------------

  Since queue is now empty, push curr tuple

  queue<(index, value)> = [
    (6, 10)
  ]

  contributionsArray
  [2, 2, 4, 5, 6, 6]

  -----------------------

  Now that there are no next element. We need a default for (6, 10). It should be len of nums
  since that will allow (6, 10) to have a contribution of 1.

  contributionsArray
  [2, 2, 4, 5, 6, 6, 7]

  ---------------------------------------------------------------------------------

  Now we need to convert the contributions array into actual contributions.

  [2, 2, 4, 5, 6, 6, 7]
   ^
   | This index (0) can contribute all the way up to (but not including index 2).
     Therefore, the contribution it can make is 2 - 0. Itself and itself + index 1


'''

from collections import deque


class SolutionRef:
  def determineSegments(nums, k):
    n = len(nums)
    contributions = [n] * n
    queue = deque()
    getQVal = lambda : nums[queue[0]]

    for i in range(n):
      num = nums[i]

      while queue and abs(num - getQVal()) > k:
        qIndex = queue.popleft()
        contributions[qIndex] = i

      queue.append(i)


    print(contributions)
    total = 0
    for i in range(n):
      total += contributions[i] - i

    return total
  
class Solution:
  def determineSegments(self, nums, k):
    n = len(nums)
    nextContributables = [n] * n
    queue = deque()
    getQFirst = lambda: nums[queue[0]]
    
    for i, num in enumerate(nums):
      while queue and abs(num - getQFirst()) > k:
        prevIndex = queue.popleft()
        nextContributables[prevIndex] = i
      
      queue.append(i)
    
    result = 0
    for i in range(n):
      nextIndex = nextContributables[i]
      result += nextIndex - i
      
    return result
  
def runSolution():
  solution = Solution()
  print(solution.determineSegments([3,7,12,8,4,1,10], 4))
  pass
runSolution()