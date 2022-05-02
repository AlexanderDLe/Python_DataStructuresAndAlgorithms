'''

  716. Max Stack

'''

import heapq

class Node:
  def __init__(self, value, id):
    self.value = value
    self.id = id
    
  def __repr__(self):
    return f'Node({self.value}, {self.id})'
    
  def __lt__(self, other):
    if self.value == other.value: return self.id > other.id
    return self.value > other.value

class MaxStack:
  def __init__(self):
    self.softDeleted = set()
    self.heap = []
    self.stack = []
    self.nextId = 0

  def push(self, x: int):
    node = Node(x, self.nextId)
    
    heapq.heappush(self.heap, node)
    self.stack.append(node)
    self.nextId += 1
    
  def pop(self):
    node = self.stack.pop()
    value, id = node.value, node.id
    
    self.softDeleted.add(id)
    self.cleanup()
    return value

  def top(self):
    return self.stack[-1].value

  def peekMax(self):
    return self.heap[0].value

  def popMax(self):
    node = heapq.heappop(self.heap)
    value, id = node.value, node.id
    
    self.softDeleted.add(id)
    self.cleanup()
    return value
    
  def cleanup(self):
    stack, softDeleted, heap = self.stack, self.softDeleted, self.heap
    
    while stack and stack[-1].id in softDeleted: 
      softDeleted.remove(stack.pop().id)
    while heap and heap[0].id in softDeleted: 
      softDeleted.remove(heapq.heappop(heap).id)
    
  def print(self):
    print(self.stack)
    print(self.heap)
    print(self.softDeleted)       
  
  
stk = MaxStack()
stk.push(5)
stk.push(1)
stk.push(5)
stk.push(7)
stk.push(4)
stk.print()
print(stk.top())         
print(stk.popMax())      
stk.print()
print(stk.top())         
print(stk.peekMax())     
print(stk.pop())         
stk.print()
# print(stk.pop())         
# print(stk.top())         