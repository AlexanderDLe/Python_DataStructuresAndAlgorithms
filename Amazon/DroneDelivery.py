'''

  Question

  A certain store is testing drone delivery. A drone can
  carry multiple items within its maximum weight capacity it can
  carry. There are certain items to be delivered from the store to
  the customers and the store decides to use two drones to
  deliver the items and the remaining items will be delivered by
  John manually. Help John to save his effort by making him carry
  minimal weight.

  Input:

  The first line contains the capacities of each drone and number
  of items W1, W2,i

  The second line contains an array of item weights W1,W2,W3...Wi

  Output:

  Print the minimum weight that John will be carrying
  i belongs to N (Natural Numbers) and wi belongs to W (Whole Numbers)
  O< < 2000. 0<= wi <=3000.
  0<=W1.W2<=2000000

  TestCase

  (drone1Capacity, drone2Capacity, itemCount)
  25 13 5
  2 5 7 10 17

  **Explanation: **

  Items with weights 7 and 17 can be carried by
  Drone 1 and items with weights 2 and 10 can be carried by
  Drone 2 and John will be carrying the remaining item with
  weight 5

=============================
  Example: 

  Drone1 Capacity: 3
  Drone2 Capacity: 2
  Item Weights: [1,2,3,4]

  We start off with weight 1 and use the DP matrix to see if
  the item can fit into the capacity of the drones.

  Base Case: [0][0] = Both drones hold 0 weight

  [
      [ 1 | 0 | 0 ]
      [ 0 | 0 | 0 ]
      [ 0 | 0 | 0 ]
      [ 0 | 0 | 0 ]
  ]


    weight: 1
    ----------------------
    3 2
    ----------------------
    3 1
    ----------------------
    3 0
    ----------------------
    2 2
    ----------------------
    2 1
    ----------------------
    2 0
    ----------------------
    1 2
    ----------------------
    1 1
    ----------------------
    1 0
    [
        [ 1 | 0 | 0 ]
        [ 1 | 0 | 0 ]
        [ 0 | 0 | 0 ]
        [ 0 | 0 | 0 ]
    ]

    drone1: 1 | drone2: 0 | weight: 1
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: 1
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: false

    We start at the botton right corner and iterate backwards towards the top left.
    At row 1 and col 0, we see that drone 1 is able to hold the item of weight 1.

    Why do we wait until row 1 and col 0? Since drone1 has a capacity of 3, surely we
    would've been able to place the item of 1 anywhere in drone 1.

    However, we wait until we reach the base case because we want to slowly build the
    contents of drone 1 over time - item by item.

    ----------------------
    0 2
    ----------------------
    0 1
    [
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 0 ]
        [ 0 | 0 | 0 ]
        [ 0 | 0 | 0 ]
    ]

    drone1: 0 | drone2: 1 | weight: 1
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: false
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: 1

    Similarly for drone 2, we want to package the item of weight 1 into drone2 as
    much as we can utilizing the base case. 

    The condition DP[drone1][drone2 - weight] checks for the "shortest available spot".
    Imagine you were stuffing a suit case, as you incrementally place items, the
    "floor" of the suitcase would rise.

    ----------------------
    0 0
    =============================
    weight: 2
    ----------------------
    3 2
    ----------------------
    3 1
    ----------------------
    3 0
    [
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 0 ]
        [ 0 | 0 | 0 ]
        [ 1 | 0 | 0 ]
    ]

    drone1: 3 | drone2: 0 | weight: 2
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: 1
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: false

    Here, we can see that the weight is 2, yet the row is 3. Why is that?

    That is because the DP matrix places the item on TOP of weight 1 - for a TOTAL
    of weight 3. 

    ----------------------
    2 2
    ----------------------
    2 1
    [
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 0 ]
        [ 0 | 1 | 0 ]
        [ 1 | 0 | 0 ]
    ]

    drone1: 2 | drone2: 1 | weight: 2
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: 1
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: false
    ----------------------
    2 0
    [
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 0 ]
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 0 ]
    ]

    drone1: 2 | drone2: 0 | weight: 2
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: 1
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: false
    ----------------------
    1 2
    [
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 1 ]
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 0 ]
    ]

    drone1: 1 | drone2: 2 | weight: 2
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: false
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: 1
    ----------------------
    1 1
    ----------------------
    1 0
    ----------------------
    0 2
    [
        [ 1 | 1 | 1 ]
        [ 1 | 0 | 1 ]
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 0 ]
    ]

    drone1: 0 | drone2: 2 | weight: 2
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: false
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: 1
    ----------------------
    0 1
    ----------------------
    0 0
    =============================
    weight: 3
    ----------------------
    3 2
    [
        [ 1 | 1 | 1 ]
        [ 1 | 0 | 1 ]
        [ 1 | 1 | 0 ]
        [ 1 | 0 | 1 ]
    ]

    drone1: 3 | drone2: 2 | weight: 3
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: 1
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: false
    ----------------------
    3 1
    [
        [ 1 | 1 | 1 ]
        [ 1 | 0 | 1 ]
        [ 1 | 1 | 0 ]
        [ 1 | 1 | 1 ]
    ]

    drone1: 3 | drone2: 1 | weight: 3
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: 1
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: false
    ----------------------
    3 0
    [
        [ 1 | 1 | 1 ]
        [ 1 | 0 | 1 ]
        [ 1 | 1 | 0 ]
        [ 1 | 1 | 1 ]
    ]

    drone1: 3 | drone2: 0 | weight: 3
    drone1 - weight >= 0 && DP[drone1 - weight][drone2]: 1
    drone2 - weight >= 0 && DP[drone1][drone2 - weight]: false
    ----------------------
    2 2
    ----------------------
    2 1
    ----------------------
    2 0
    ----------------------
    1 2
    ----------------------
    1 1
    ----------------------
    1 0
    ----------------------
    0 2
    ----------------------
    0 1
    ----------------------
    0 0

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from _utils import printMatrix

def itemCanFit(d1, d2, weight, DP):
  if d1 - weight >= 0 and DP[d1 - weight][d2]:
    return True
  if d2 - weight >= 0 and DP[d1][d2 - weight]:
    return True
  return False

def droneDelivery(capacity1, capacity2, weights):
  DP = []
  for i in range(capacity1 + 1):
    DP.append([0] * (capacity2 + 1))
  DP[0][0] = 1
  
  for weight in weights:
    for d1 in range(capacity1, -1, -1):
      for d2 in range(capacity2, -1, -1):
        if itemCanFit(d1, d2, weight, DP):
          DP[d1][d2] = 1

  printMatrix(DP)
  totalWeight = sum(weights)
  minCarry = totalWeight

  for d1 in range(capacity1 + 1):
    for d2 in range(capacity2 + 1):
      if (DP[d1][d2] == 1):
        minCarry = min(minCarry, totalWeight - d1 - d2)

  return minCarry

  
  

print(droneDelivery(3, 2, [1,2,3,4]))