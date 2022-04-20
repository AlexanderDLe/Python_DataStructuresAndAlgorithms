'''

  You are an amazon delivery and you have some boxes that you have to deliver, 
  but there are some conditions -

  > You can take 2 boxes of same weight in one round
  > You can take 3 boxes of same weight in one round

  You have to find the minimum number of rounds to deliver the boxes or -1 if it 
  is not possible to deliver them.

  Example cases -
  Input: boxes - [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
  Output: 4
  Explanation: 3 boxes of weight 2 in 1st round, 2 boxes of weight 3 in 2nd round, 
  3 boxes of wt 4 in 3rd and 2 boxes of wt 4 in 4th round.

  Input: boxes - [2, 3, 3]
  Output: -1

  Explanation: There is only one box with weight 2 and we can only take either 2
  or 3 boxes in one round not lesser.

  ----------------------------------------------------------------

  2, 2, 3, 3, 2, 4, 4, 4, 4, 4

  FreqMap: {
    2: 3
    3: 2
    4: 5
  }

  Most frequent = 5

  Build a DP array for minimum rounds per frequency up to the most frequent.

  [0, INF, INF, INF, INF, INF] <---- Array of length 5 (most frequent)
                               <---- Base case [0] is set to 0. Zero rounds to achieve zero frequency.
  
  Options for boxes per round = [2, 3]
  
  frequency = 1
       |
       v
  [0, INF, INF, INF, INF, INF] 
       
       2 and 3 are the minimum amount of boxes per round. Cannot only take 1.

  ----------------------------------------------------------------

  frequency = 2
           |
           v
  [0, INF, 1, INF, INF, INF] 
           
          We can take all 2 boxes when frequency is 2. 
          We iterate through the boxOptions (2 and 3) and compare to frequency
          
  ----------------------------------------------------------------

  frequency = 3
              |
              v
  [0, INF, 1, 1, INF, INF] 
           
          We can take all 3 boxes when frequency is 3. 
          We iterate through the boxOptions (2 and 3) and compare to frequency

  ----------------------------------------------------------------

  frequency = 4
                 |
                 v
  [0, INF, 1, 1, 2, INF] 
           
          We can make 2 rounds of 2 boxes when frequency is 4. 

          To determine best way to set DP value, we look at DP[frequency - boxTrip] DP[4 - 2]
          We see that DP[4 - 2] is already set to 1, therefore we can increment that.
  ----------------------------------------------------------------

  frequency = 5
                    |
                    v
  [0, INF, 1, 1, 2, 2] 
           
          We can make 2 rounds of 3 & 2 boxes when frequency is 5. 

          To determine best way to set DP value, we look at DP[frequency - boxTrip] DP[5 - 3]
          We see that DP[5 - 3] is already set to 1, therefore we can increment that.
  ----------------------------------------------------------------
  (Bonus: Increase Frequency by 1)

  frequency = 6
                       |
                       v
  [0, INF, 1, 1, 2, 2, 2] 
           
          We can make 2 rounds of 3 & 3 boxes when frequency is 6. 

          To determine best way to set DP value, we look at DP[frequency - boxTrip] DP[6 - 3]
          We see that DP[6 - 3] is already set to 1, therefore we can increment that.


'''

import math


def getTrips(frequency):
  if (frequency == 1):
    return -1
  if (frequency % 3 == 0):
    return frequency / 3
  if (frequency % 3 == 2 or frequency % 3 == 1):
    return math.floor((frequency / 3)) + 1

def amazonBoxes(weights: list[int]):

  map = {}
  for weight in weights:
    map[weight] = map.get(weight, 0) + 1

  totalTrips = 0
  for key in map:
    trips = getTrips(map[key])    

    if trips == -1:
      return -1

    totalTrips += trips

  return totalTrips


result = amazonBoxes([2, 2, 3, 3, 2, 4, 4, 4, 4, 4])
print(result)