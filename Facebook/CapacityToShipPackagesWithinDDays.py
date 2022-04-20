'''

  1011. Capacity to Ship Packages Within D Days

'''

def shipWithinDays(weights, days):
  def validCapacity(capacity):
    count = 1
    sum   = 0

    for weight in weights:
      sum += weight

      if sum > capacity:
        count += 1
        sum = weight
      
    print(f'capacity: {capacity} | count: {count}')
    return count <= days

  L = max(weights)
  R = sum(weights)

  while L < R:
    capacity = (L + R + 1)//2
    print(L, capacity, R)

    # The binary search framework depends on the condition we are searching for.
    # In this case, once we find a valid capacity - we don't want to remove it in the
    # binary search range. We want to keep it and search lower.
    if validCapacity(capacity): R = capacity
    else                      : L = capacity + 1

  return L


print(shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
# print(shipWithinDays(weights = [3,2,2,4,1,4], days = 3))
# print(shipWithinDays(weights = [1,2,3,1,1], days = 4))