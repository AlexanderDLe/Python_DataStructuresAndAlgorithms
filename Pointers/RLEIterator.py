'''

  900. RLE Iterator

'''

class RLEIterator:
  def __init__(self, encoding):
    self.encoding = encoding
    self.index = 0

  def next(self, n):
    encoding = self.encoding
    
    while n and self.index < len(encoding):
      instances = encoding[self.index]
      
      if n <= instances:
        encoding[self.index] -= n
        return encoding[self.index + 1]
      else:
        n -= encoding[self.index]
        self.index += 2
      
    return -1
  
def runSolution():
  rleIterator = RLEIterator([3, 8, 0, 9, 2, 5])  # This maps to the sequence [8,8,8,5,5].
  print(rleIterator.next(2))  # exhausts 2 terms of the sequence, returning 8. The remaining sequence is now [8, 5, 5].
  print(rleIterator.next(1))  # exhausts 1 term of the sequence, returning 8. The remaining sequence is now [5, 5].
  print(rleIterator.next(1))  # exhausts 1 term of the sequence, returning 5. The remaining sequence is now [5].
  print(rleIterator.next(2))  # exhausts 2 terms, returning -1. This is because the first term exhausted was 5,
                       #but the second term did not exist. Since the last term exhausted does not exist, we return -1.
  pass
runSolution()
