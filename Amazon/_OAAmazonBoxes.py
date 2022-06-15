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

from collections import Counter
import math



class SolutionRef:
  def getTrips(self, frequency):
    if (frequency == 1):
      return -1
    if (frequency % 3 == 0):
      return frequency / 3
    if (frequency % 3 == 2 or frequency % 3 == 1):
      return math.floor((frequency / 3)) + 1

  def amazonBoxes(self, weights: list[int]):
    map = {}
    for weight in weights:
      map[weight] = map.get(weight, 0) + 1

    totalTrips = 0
    for key in map:
      trips = self.getTrips(map[key])    

      if trips == -1:
        return -1

      totalTrips += trips

    return totalTrips

class Solution1:
  def amazonBoxes(self, weights: list[int]):
    freqMap = Counter(weights)
    totalTrips = 0
    
    for freq in list(freqMap.values()):
      trips = int(self.getTrips(freq))
      if trips == -1: return -1
      totalTrips += trips
    
    return totalTrips
  
  def getTrips(self, freq):
    if freq == 1: 
      return -1
    if freq % 3 == 0:
      return freq // 3
    if freq % 3 > 0:
      return (freq // 3) + 1
    '''
      Ex 4: 2 + 2 = 4
      Ex 5: 3 + 2 = 5
      Ex 7: 3 + 4 = 7
      
      We take freq // 3 to determine how many times we can remove packs of 3.
      The +1 will add a trip taking 2 packages.
      
      For example: 
      We can take 1 pack of 3 from 4, which leaves one.
      
      4 - 3 = 1
      
      That leaves 1, but 1 is not divisible by 3 or 2. This is fine since we can take a 
      pack of two instead of the previous 3 - the 3 that was taken will automatically be 
      converted into a pack of 2
      
      4 - 2 = 2 (which leaves another pack of 2).
      
      In essence, every value greater than 1 can be broken down into multiples of 2 and 3.
    '''
    
class Solution:
  def amazonBoxes(self, weights):
    freqMap = Counter(weights)
    totalTrips = 0
    
    for packages in list(freqMap.values()):
      trips = self.getTrips(packages)
      if trips == -1: return -1
      totalTrips += trips
    
    return totalTrips
  
  def getTrips(self, freq):
    if freq == 1: 
      return -1
    if freq % 3 == 0: 
      return freq // 3
    if freq % 3 > 0:
      return freq // 3 + 1
  
def runSolution():
  solution = Solution()
  print(solution.amazonBoxes([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
  pass
runSolution()