# 1851. Minimum Interval to Include Each Query

from functools import cmp_to_key


def minInterval(intervals, queries):
  def compare(x, y):
     return x[1] - y[1]
 
  intervals.sort(key=lambda x:x[0])
  print(intervals)



minInterval([[2, 3], [1,4],[2,4],[3,6],[4,4]], [2,3,4,5])