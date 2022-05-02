'''

  362. Design Hit Counter

'''

class HitCounterRef:
  def __init__(self):
    self.counter = [[0, i + 1] for i in range(300)]

  def hit(self, timestamp):
    #ts = 301 means (301 - 1)%300
    index = int((timestamp - 1) % 300)
    if self.counter[index][1] == timestamp:
      self.counter[index][0] += 1
    else:
      self.counter[index][0] = 1
      self.counter[index][1] = timestamp
    
    return self.counter

  def getHits(self, timestamp):
    totalCount = 0
    for x in self.counter:
      count, time = x[0], x[1]
      if timestamp - time < 300:
        totalCount += count
    
    return totalCount

class HitCounter:
  def __init__(self):
    self.counter = [[0, i + 1] for i in range(300)]

  def hit(self, timestamp):
    '''
      300 -> 300
      301 -> 001
    '''
    index = int((timestamp - 1) % 300)
    if timestamp == self.counter[index][1]:
      self.counter[index][0] += 1
    else:
      self.counter[index][1] = timestamp
      self.counter[index][0] = 1

  def getHits(self, timestamp):
    totalCount = 0
    for hits, time in self.counter:
      if time > timestamp - 300:
        totalCount += hits
    
    return totalCount



def runSolution():
  hitCounter = HitCounter()
  print(hitCounter.hit(1))       # hit at timestamp 1.
  print(hitCounter.hit(2))       # hit at timestamp 2.
  print(hitCounter.hit(3))       # hit at timestamp 3.
  print(hitCounter.getHits(4))   # get hits at timestamp 4, return 3.
  print(hitCounter.hit(300))     # hit at timestamp 300.
  print(hitCounter.getHits(300)) # get hits at timestamp 300, return 4.
  print(hitCounter.hit(305))     # hit at timestamp 300.
  print(hitCounter.getHits(300)) # get hits at timestamp 300, return 4.
  pass
runSolution()
