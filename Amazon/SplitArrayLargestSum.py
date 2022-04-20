'''
  410. Split Array Largest Sum

  Given an array nums which consists of non-negative integers and an integer m, 
  you can split the array into m non-empty continuous subarrays.

  Write an algorithm to minimize the largest sum among these m subarrays.

  --------------------------------------------------------
  
  Example 1:

  [7,2,5,10,8], m = 2

  There are four ways to split nums into two subarrays.
  The best way is to split it into [7,2,5] and [10,8],
  where the largest sum among the two subarrays is only 18.

  Total sum = 32

  --------------------------------------------------------
  
  Parametric Search

  lo = max(nums)
  hi = sum(nums)

'''

def splitArraysRef(nums, m):
  L = min(nums)
  R = sum(nums)
  
  while L < R:
    M = (L + R) // 2
    total = 0
    count = 0
    print(L, M, R)

    for num in nums:
      total += num

      if total > M:
        total = num
        count += 1

    if count >= m: L = M + 1
    else         : R = M

  return R
    
def splitArrays(nums, m):
  L = max(nums)
  R = sum(nums)

  while L < R:
    M = (L + R + 1)//2
    total = 0
    count = 0
    print(L, M, R)
    for num in nums:
      total += num
      
      if total >= M:
        count += 1
        total = num

    print(f"count: {count}")
    if count >= m: L = M
    else         : R = M - 1

  return L

# print(splitArraysRef([7,2,5,10,8], 2))
print(splitArrays([7,2,5,10,8], 2))
# print(splitArrays([1,4,4], 3))