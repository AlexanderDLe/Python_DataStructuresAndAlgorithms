'''

  981. Time Based Key Value Store

'''

from collections import defaultdict


class TimeMap:
  def __init__(self):
    self.dict = defaultdict(list)
        
  def set(self, key, value, timestamp):
    self.dict[key].append((value, timestamp))
        
  def get(self, key, timestamp):
    array = self.dict[key]
    L, R = 0, len(array)
    
    while L < R:
      M = L + (R - L)//2
      time = array[M][1]
      
      if time > timestamp: R = M
      else               : L = M + 1
    
    index = L - 1
    if index < 0: return ''
    return array[index][0]


def runSolution():
  # timeMap = TimeMap()
  # timeMap.set("foo", "bar", 1)   # store the key "foo" and value "bar" along with timestamp = 1.
  # print(timeMap.get("foo", 1))   # return "bar"
  # print(timeMap.get("foo", 3))   # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
  # timeMap.set("foo", "bar2", 4)  # store the key "foo" and value "bar2" along with timestamp = 4.
  # print(timeMap.get("foo", 4))   # return "bar2"
  # print(timeMap.get("foo", 5))   # return "bar2"
  
  timeMap2 = TimeMap()
  timeMap2.set("love", "high", 10)
  timeMap2.set("love", "low", 20)
  print(timeMap2.get("love", 5))
  print(timeMap2.get("love", 10))
  print(timeMap2.get("love", 15))
  print(timeMap2.get("love", 20))
  print(timeMap2.get("love", 25))
  pass
runSolution()
