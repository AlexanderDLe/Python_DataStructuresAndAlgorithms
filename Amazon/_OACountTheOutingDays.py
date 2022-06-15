'''

  Count the Outing Days

  Amazon Alexa AI team is working to add feature that suggest days for camping based on 
  the weather forecast. According to survey, a day is ideal for camping if the amount of
  rainfall has been non-increasing for the prior k days from the considered day and will 
  be non-decreasing for the following k days from the considered day. Given the predicted 
  rainfall for the next n days, find all ideal days. 
  
  Formally a day is ideal if the following is true:
  day[i-k]>=day[i-k+1]>=....>=day[i-1]>=day[i]<=day[i+1]<=....<=day[i+k-1]<=day[i+k]

  Return the ideal days in ascending order. The ith element of the array represents the data for the day i+1.

  -----------------------------------------------------------

  Example: Rainfall = [3,2,2,2,3,4], k=2

  day1 >= day2 >= day3 <= day4 <= day5 --- so day 3 is ideal
  day2 >= day3 >= day4 <= day5 <= day6 --- so day 4 is ideal
  
  Output: [3,4]

  ------------------------------------------------------------

  Example: Rainfall = [1,0,1,0,1], k=1
  day1 >= day2 <= day3
  day3 >= day4 <= day5
  
  Output: [2,4]

  L: 0 0 1 0 1
  R: 1 0 1 0 0
  
  ------------------------------------------------------------

  Example: Rainfall = [1,0,0,0,1], k=2
  
  day1>=day2>=day3 <=day4<=day5
  
  Output: [3]

  L: 0 0 1 2 3
  R: 3 2 1 0 0

  ------------------------------------------------------------

  Theory

  3   2   2   2   3   4

          ^               From any position, how can we efficiently know:
                          > i to (i + k) is non-decreasing?
                          > i to (i - k) is non-decreasing?

  L   0   0   1   2   3   4
  R   3   2   1   0   0   0
  
  We can create two other arrays for precomputation.
  L array represents the running increasing days from the left
  R array represents the running increasing days from the right

'''

class SolutionRef:
  def countOutingDays(self, rainfall, k):
    n = len(rainfall)

    fromLeft = n * [0]
    fromRight = n * [0]

    for i in range(1, n):
      if (rainfall[i] >= rainfall[i - 1]):
        fromLeft[i] = fromLeft[i - 1] + 1
    
    for i in range(n - 2, -1, -1):
      if (rainfall[i] >= rainfall[i + 1]):
        fromRight[i] = fromRight[i + 1] + 1

    # [3,2,2,2,3,4] n = 6, k = 2; n - k = 4
    #      ^ ^
    #      k n-k
    result = []
    for i in range(k, n - k):
      rightIdeal = fromLeft[i + k] >= k
      leftIdeal = fromRight[i - k] >= k

      if (rightIdeal and leftIdeal):
        result.append(i + 1)
    
    return result
  
class Solution:
  def countOutingDays(self, rainfall, k):
    pass
  
  
def runSolution():
  solution = Solution()
  print(solution.countOutingDays([3,2,2,2,3,4],2))
  print(solution.countOutingDays([1,0,1,0,1],1))
  print(solution.countOutingDays([1,1,1,1,1,1,1,1,1,1], 3))
  pass
runSolution()