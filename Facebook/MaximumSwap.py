'''

  670. Maximum Swap

'''

import math


def maxSwapRef(num):
  arr = map(int, str(num))
  arr = list(arr)

  # Make a map with last index occurences for each value
  lastOccurence = {x: i for i, x in enumerate(arr)}
  
  # Loop through each digit in nums
  for i, x in enumerate(arr):

    # Loop from highest digit (9) to current digit exclusive (x)
    for digit in range(9, x, -1):

      # Since we're looping from highest digit, digit should be > x
      # If we find a value y in the map AND it is greater than x, then swap & return
      if digit in lastOccurence and lastOccurence[digit] > i:
        index = lastOccurence[digit]
        arr[i], arr[index] = arr[index], arr[i]
        return int(''.join(map(str, arr)))
  
  return num


def maxSwap(num):
  arr = list(map(int, str(num)))
  lastOccur = {x: i for i, x in enumerate(arr)}
  
  for i, val in enumerate(arr):
    for digit in range(9, val, -1):
      if digit in lastOccur and lastOccur[digit] > i:
        index = lastOccur[digit]
        arr[i], arr[index] = arr[index], arr[i]
        return int(''.join(map(str, arr)))
        
  return num

print(maxSwap(2736))
print(maxSwap(9973))