'''

  715. Range Module

'''

from collections import deque
from bisect import bisect_left, bisect_right

class RangeModuleRef:
    def __init__(self):
      self.range = [0, 10**9]
      self.valid = [False] * 2
      print(self.range)
      print(self.valid)
      
    def addRange(self, left, right, track=True):
      def index(val):
        i = bisect_left(self.range, val)
        if self.range[i] != val:
          self.range.insert(i, val)
          self.valid.insert(i, self.valid[i - 1])
        return i
      
      if track: print('addRange', left, right)
      else    : print('removeRange', left, right)
      L = index(left)
      print(self.range, self.valid)
      R = index(right)
      print(self.range, self.valid)
      print(L, R)
      self.range[L:R] = [left]
      self.valid[L:R] = [track]
      print(self.range, self.valid)
          

    def queryRange(self, left, right):
      i = bisect_right(self.range, left) -1
      j = bisect_left(self.range, right)
      print('queryRange:', left, right, ' indexes: ', i, j)
      print(self.range)
      print(self.valid)
      print(self.range[i:j], self.valid[i:j])
      return all(self.valid[i:j])

    def removeRange(self, left, right):
      self.addRange(left, right, False)
  
class RangeModule:
    def __init__(self):
      self.range = [0, 10**9]
      self.valid = [False, False]
      
    def addRange(self, left, right, track=True):
      # Binary search for indexes of left & right
      # Create entries if they don't exist
      L = self.index(left)
      R = self.index(right)
      
      # Collapse and set arrays
      self.range[L:R] = [left]
      self.valid[L:R] = [track]
          

    def queryRange(self, left, right):
      L = bisect_right(self.range, left) - 1
      R = bisect_left(self.range, right)
      return all(self.valid[L:R])

    def removeRange(self, left, right):
      self.addRange(left, right, False)
    
    def index(self, val):
      i = bisect_left(self.range, val)
      if val != self.range[i]:
        self.range.insert(i, val)
        self.valid.insert(i, self.valid[i - 1])
      return i
  
def runSolution():
  # rangeModule = RangeModuleRef()
  # rangeModule.addRange(10, 20)
  # rangeModule.removeRange(14, 16)
  # rangeModule.queryRange(10, 14) # return True,(Every number in [10, 14) is being tracked)
  # rangeModule.queryRange(13, 15) # return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
  # rangeModule.queryRange(16, 17) # return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
  # rangeModule.queryRange(18, 21) # return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
  
  rangeModule2 = RangeModule()
  rangeModule2.addRange(5, 8)
  rangeModule2.queryRange(3, 4)
  rangeModule2.removeRange(5, 6)
  rangeModule2.removeRange(3, 6)
  rangeModule2.addRange(1, 3)
  rangeModule2.queryRange(2, 3)
  rangeModule2.addRange(4, 8)
  rangeModule2.queryRange(2, 3)
  rangeModule2.removeRange(4, 9)
  
  pass
runSolution()