'''

  1628. Design an Expression Tree With Evaluate Function

'''

class Node(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
  def __repr__(self):
    return f'({self.left} {self.val} {self.right})'
    
  def ops(self, char, left, right):
    left, right = int(left), int(right)
    
    if char == '+': return left + right
    if char == '-': return left - right
    if char == '*': return left * right
    if char == '/': return left / right
    
  def evaluate(self):
    left = self.left
    right = self.right
    
    if type(self.left) != str:
      left = left.evaluate()
    
    if type(self.right) != str:
      right = right.evaluate()
      
    return int(self.ops(self.val, left, right))

class TreeBuilder:
  def buildTree(self, s):
    nodes = []
    
    for char in s:
      if char.isdigit():
        nodes.append(char)
        continue
    
      if char in '+-/*':
        right = nodes.pop()
        left  = nodes.pop()
        node = Node(char, left, right)
        nodes.append(node)
    
    return nodes[-1]
      

def runSolution():
  solution = TreeBuilder()
  print(solution.buildTree(s = ["3","4","+","2","*","7","/"]).evaluate())
  print(solution.buildTree(s = ["4","5","2","7","+","-","*"]).evaluate())
  pass
runSolution()

