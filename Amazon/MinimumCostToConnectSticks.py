'''
  1167. Minimum Cost to Connect Sticks
'''

import heapq


def minCost(sticks):
  cost = 0
  heapq.heapify(sticks)

  while len(sticks) > 1:
    stick1 = heapq.heappop(sticks)
    stick2 = heapq.heappop(sticks)
    combined = stick1 + stick2

    cost += combined

    heapq.heappush(sticks, combined)

  return cost

  


print(minCost([2,4,3]))
print(minCost([1,8,3,5]))