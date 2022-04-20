'''

  So, this question was super confusing I spent 25 minutes just to understand it. The solution is on Leetcode.

  There is a new product launched and its customer ratings are being recorded in an array. 
  The ratings are being monitored and analyzed if there is any decrease in the ratings.

  Find the number of periods in which the rating is consecutively decreasing.

  Example:
  
  Ratings = [4,3,5,4,3]

  Periods (in other words sub arrays in which ratings are decreasing):
  One day periods = [4],[3],[5],[4],[3] (count of subarrays is 5)
  Two day periods = [4,3],[5,4],[4,3] (count of subarrays is 3)
  3 day periods = [5,4,3] (count of subarrays is 1)
  
  So, the output for this example will be 9 (5 + 3 + 1)

'''