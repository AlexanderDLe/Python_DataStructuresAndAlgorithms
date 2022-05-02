'''

  1060. Missing Element in Sorted Array

'''

def printAll(nums, L, M, R, missing, k):
  rangeOfElements = nums[M] - nums[L]
  numOfElements = M - L
  print(f'L: {L} | M: {M} | R: {R} | missing: {missing} | k: {k}')
  print(f'rangeOfElements: {nums[M]} - {nums[L]} | numOfElements: {M} - {L} = {missing}')
  print(f'rangeOfElements = {rangeOfElements}    | numOfElements: {numOfElements}')
  print(f'missingElements = {rangeOfElements} - {numOfElements} = {rangeOfElements - numOfElements}')
  print('----------------------------------------------')


def missingElement(nums, k):
  if not nums or k == 0: return 0

  diff = nums[-1] - nums[0] + 1
  missing = diff - len(nums)

  if k > missing: return nums[-1] + k - missing

  L, R = 0, len(nums) - 1
  while L + 1 < R:
    M = (L + R)//2

    # The full number of elements 
    rangeOfElements = nums[M] - nums[L]

    # The number of elements to the left of M until L (not including M)
    numOfElements = M - L

    # Calculate the missing elements.
    # Ex: 4,7,9,10 <-- missing 5,6,8
    # Range = 10 - 4 = 6, numElements [L, M) = 3
    missing = rangeOfElements - numOfElements
    printAll(nums, L, M , R, missing, k)

    if missing < k:
      L = M
      # If we do not have enough missing elements, we must search for
      # a greater number. However, we need to exclude the missing numbers 
      # that are accounted up until this point when we search right
      k -= missing
    else:
      R = M
      
  print(L, R)
  return nums[L] + k


# print(missingElement(nums = [4,7,9,10], k = 1))
print(missingElement(nums = [4,7,9,10,12,15,18], k = 7))
# print(missingElement(nums = [1,2,4],    k = 3))