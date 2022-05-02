'''

  20. Valid Parentheses

'''
class MinStack:
    def __init__(self):
      self.stack = []
      self.minStack = []

    def push(self, val):
      self.stack.append(val)
      
      if not self.minStack or val <= self.minStack[-1]:
        self.minStack.append(val)

    def pop(self):
      popped = self.stack.pop()
      if popped == self.minStack[-1]:
        self.minStack.pop()

    def top(self):
      return self.stack[-1]

    def getMin(self):
      return self.minStack[-1]
    
def runSolution():
  minStack = MinStack() 
  minStack.push(-2) 
  minStack.push(0) 
  minStack.push(-3) 
  print(minStack.getMin())  # return -3
  minStack.pop() 
  print(minStack.top())     # return 0
  print(minStack.getMin())  # return -2
  pass
runSolution()
