'''

  729. My Calendar I

'''

from bisect import bisect_left


class MyCalendar:
  def __init__(self):
    self.starts = []
    self.ends = {}

  def book(self, start, end):
    if start in self.ends: return False
      
    index = bisect_left(self.starts, start)
    prevStartIdx = index - 1
    nextStartIdx = index
    
    if prevStartIdx >= 0:
      prevStart = self.starts[prevStartIdx]
      prevEnd   = self.ends[prevStart]
      if start < prevEnd: return False
    
    if nextStartIdx < len(self.starts):
      nextStart = self.starts[nextStartIdx]
      if end > nextStart: return False
    
    self.ends[start] = end
    self.starts.insert(index, start)
    return True
    
  
def runSolution():
  # myCalendar = MyCalendar()
  # myCalendar.book(10, 20)   # return True
  # myCalendar.book(15, 25)   # return False, It can not be booked because time 15 is already booked by another event.
  # myCalendar.book(20, 30)   # return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
  
  myCalendar2 = MyCalendar()
  print(myCalendar2.book(37, 50))
  print(myCalendar2.book(33, 50))
  print(myCalendar2.book(4, 17))
  print(myCalendar2.book(35, 48))
  print(myCalendar2.book(8, 25))
  
  
  pass
runSolution()
