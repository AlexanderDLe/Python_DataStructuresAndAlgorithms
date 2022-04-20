'''

  523. Continuous Subarray Sum

  ----------------------------------

  k = 7

   nums:  23   2   4   6   6
  total:   2

  rem: {
    0: -1
  }
   
'''

def checkSubarraySum(nums, k):
  remainder = {0: -1}
  moddedSum = 0

  for i, n in enumerate(nums):
    moddedSum += n
    moddedSum %= k

    if moddedSum not in remainder:
      remainder[moddedSum] = i

    elif i - remainder[moddedSum] > 1:
      return True

  return False


print(checkSubarraySum([23,2,4,6,6], 7))
# print(checkSubarraySum([23,2,4,6,7], 6))
# print(checkSubarraySum([23,2,6,4,7], 6))
# print(checkSubarraySum([23,2,6,4,7], 13))