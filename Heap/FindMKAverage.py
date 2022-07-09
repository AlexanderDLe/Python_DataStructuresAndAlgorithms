'''

  355. Design Twitter

'''

from heapq import heapify, heappush


class MKAverage:
  def __init__(self, m, k):
    self.m, self.k = m, k
    self.arr = [0] * m
    self.lh1, self.rh1 = self.initHeap(m, k)
    self.lh2, self.rh2 = self.initHeap(m, m - k)
    self.score = 0
    
  def initHeap(self, p1, p2):
    h1 = [(0, i) for i in range(p1 - p2, p1)]
    h2 = [(0, i) for i in range(p1 - p2)]
    heapify(h1)
    heapify(h2)
    return (h1, h2)

  def update(self, lh, rh, m, k, num):
    score , T = 0, len(self.arr)
    
    # if num > rh[0][0]:
    #   heappush(rh, (num, T))
    #   if self.arr[T - m] <= T - m: score += rh[0][0]:
    #     if rh[0][1]

  def addElement(self, num):
    t1 = self.update(self.lh1, self.rh1, self.m, self.k, num)
    t2 = self.update(self.lh2, self.rh2, self.m, self.k, num)
    self.arr.append(num)
    self.score += (t2 - t1)
    

  def calculateMKAverage(self):
    if len(self.arr) < 2 * self.m: return -1
    return self.score // (self.m - 2*self.k)
      
def runSolution():
  objpre = MKAverage(7, 2) 
  obj = MKAverage(3, 1) 
  obj.addElement(3)         # current elements are [3]
  obj.addElement(1)         # current elements are [3,1]
  obj.calculateMKAverage()  # return -1, because m = 3 and only 2 elements exist.
  obj.addElement(10)        # current elements are [3,1,10]
  obj.calculateMKAverage()  # The last 3 elements are [3,1,10].
                            # After removing smallest and largest 1 element the container will be [3].
                            # The average of [3] equals 3/1 = 3, return 3
  obj.addElement(5)         # current elements are [3,1,10,5]
  obj.addElement(5)         # current elements are [3,1,10,5,5]
  obj.addElement(5)         # current elements are [3,1,10,5,5,5]
  obj.calculateMKAverage()  # The last 3 elements are [5,5,5].
                            # After removing smallest and largest 1 element the container will be [5].
                            # The average of [5] equals 5/1 = 5, return 5
  pass
runSolution()