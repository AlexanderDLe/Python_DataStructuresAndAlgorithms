'''

  895. Maximum Frequency Stack

'''

from collections import defaultdict


class FreqStack:
  def __init__(self):
    self.freqMap = defaultdict(int)
    self.stack = []

  def push(self, val):
    freqMap, stack = self.freqMap, self.stack
    
    freqMap[val] += 1
    freq = freqMap[val]
    
    if len(stack) < freq: stack.append([])
    stack[freq - 1].append(val)

  def pop(self):
    freqMap, stack = self.freqMap, self.stack
    
    topStack = stack[-1]
    topVal = topStack.pop()
    
    freqMap[topVal] -= 1
    if len(topStack) == 0: stack.pop()
    
    return topVal
  
  
def runSolution():
  freqStack = FreqStack()
  freqStack.push(5) # The stack is [5]
  freqStack.push(7) # The stack is [5,7]
  freqStack.push(5) # The stack is [5,7,5]
  freqStack.push(7) # The stack is [5,7,5,7]
  freqStack.push(4) # The stack is [5,7,5,7,4]
  freqStack.push(5) # The stack is [5,7,5,7,4,5]
  print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
  print(freqStack.pop())   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
  print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
  print(freqStack.pop())   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
  pass

runSolution()