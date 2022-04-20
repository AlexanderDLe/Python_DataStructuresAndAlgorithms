'''

  346. Moving Average from Data Stream

'''

class MovingAverage:
  def __init__(self, size: int):
    self.size = size
    self.queue = []
    self.sum = 0

  def next(self, val: int) -> float:
    self.sum += val
    self.queue.append(val)

    if len(self.queue) > self.size:
      self.sum -= self.queue.pop(0)

    return self.sum/len(self.queue)

movingAverage = MovingAverage(3)
print(movingAverage.next(1))
print(movingAverage.next(10))
print(movingAverage.next(3))
print(movingAverage.next(5))
