'''

  Given an array a, your task is to convert it into a non-increasing form 
  such that we can either increment or decrement the array value by 1 in 
  minimum changes possible.

  ---------------------------------------------------------------------------

  Input : a[] = {3, 1, 2, 1}
  Output : 1

  Explanation:

  We can convert the array into 3 1 1 1 by
  changing 3rd element of array i.e. 2
  into its previous integer 1 in one step
  hence only one step is required.

  ---------------------------------------------------------------------------

  Input : a[] = {3, 1, 5, 1}
  Output : 4
  We need to decrease 5 to 1 to make array sorted
  in non-increasing order.

  ---------------------------------------------------------------------------

  Input : a[] = {1, 5, 5, 5}
  Output : 4
  We need to increase 1 to 5.

  ---------------------------------------------------------------------------

  pq = minHeap

  [3, 1, 2, 1]
         ^

  val = 2
  pq: 3, 1

  val > pq.top().

  That means it is no longer non-increasing and we must change val.
  increase switches++

  pq: 3, 2, 2

  ---------------------------------------------------------------------------

  [3, 1, 2, 1]
            ^

  val = 2
  pq: 3,2, 2

  val > pq.top().

  That means it is no longer non-increasing and we must change val.
  increase switches++

  pq: 3, 2, 2, 1

  ---------------------------------------------------------------------------

  Ex2.

  2   3   4   7
  ^

  val = 2
  pq: 

  pq is empty. Just push into pq

  ---------------------------------------------------------------------------

  2   3   4   7
      ^

  val = 2
  pq  = 2
  s   = 1

  3 > 2, therefore we must add to switches to accomodate non-increasing.
  We add  3 onto the pq. However, we must also convert the 2 (top) into 3 as well.

  pq = 3, 3

  ---------------------------------------------------------------------------

  2   3   4   7
          ^

  val = 4
  pq  = 3, 3
  s   = 2

  4 > 3, therefore we must add to switches to accomodate non-increasing. (4 - 3 = 1)
  We add 4 onto the pq. However, we must also convert the 3 (top) into 4 as well.

  pq = 3, 4, 4

  --------------------------------------------------------------------------

  Why do we need to convert? If we pop out the 2 without readding the incremented version,
  then it will not account for the next minimal change.

  TIP: 2, 3, 4, 7

  2, 3        -> One change to make 3, 3
  3, 3, 4     -> One change to make 3, 3, 3
  3, 3, 3, 7  -> 4 changes to make 3, 3, 3, 3

  The converting step helps us keep track of the previous value to compare the next value with.

  ---------------------------------------------------------------------------

  2   3   4   7
              ^

  val = 7
  pq  = 3, 4, 4
  s   = 2

  7 > 3, therefore we must add to switches to accomodate non-increasing. (7 - 3 = 4)
  We add 4 onto the pq. However, we must also convert the 3 (top) into 4 as well.

  pq = 4, 4, 7, 7


'''

import heapq


def minChangesRef(nums):
  pq = []
  pqTop = lambda: pq[0]

  n = len(nums)
  s = 0

  for i in range(n):
    val = nums[i]

    if pq and pqTop() < val:
      s += (val - pqTop())
      heapq.heappush(pq, val)
      heapq.heappop(pq)

    heapq.heappush(pq, val)
    print(pq)
  
  return s

def minChanges(nums):
  pq = []
  switches = 0

  for num in nums:
    if pq and num > pq[0]:
      switches += (num - pq[0])
      heapq.heappop(pq)
      heapq.heappush(pq, num)

    heapq.heappush(pq, num)
    print(pq)
  
  return switches

# print(minChanges([3, 1, 2, 1]))
# print(minChanges([3, 1, 5, 1]))
print(minChanges([1, 1, 5, 5, 5]))
# print(minChanges([5,2,11,4,2,6]))
# print(minChanges([2,3,4,7]))
# print(minChanges([2,2,2,7]))
# print(minChanges([2,7,2,7]))
# print(minChanges([7,2,2,2,7,2]))
# print(minChanges([2,7,2,2,7,2]))
# print(minChanges([22,44,2,5,15,35,46,2,5,35]))