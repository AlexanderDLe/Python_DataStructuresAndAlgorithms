'''

  56. Merge Intervals

'''


def merge(intervals):
  intervals.sort(key=lambda x: x[0])
  res = []
  prev = intervals[0]

  for i in range(1, len(intervals)):
    curr = intervals[i]
    currStart, currEnd = curr
    prevEnd = prev[1]
    
    if currStart > prevEnd:
      res.append(prev)
      prev = curr
    else:
      prev[1] = max(currEnd, prevEnd)
  
  res.append(prev)

  return res
    




print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[0,4]]))