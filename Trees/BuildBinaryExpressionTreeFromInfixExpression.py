'''

  1597. Build Binary Expression Tree From Infix Expression

'''

class Node(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class SolutionRef:
  def expTree(self, s):
    nodes, ops = [], []
    
    for char in s:
      if char.isdigit():
        nodes.append(char)
        continue
      
      if char == '(':
        ops.append(char)
        continue
      
      # If closing, then process until reach matching open
      # Then remove the matching '('
      if char == ')':
        while ops and ops[-1] != '(':
          nodes.append(self.buildNode(ops.pop(), nodes.pop(), nodes.pop()))
        ops.pop()
        continue
        
      # If operator
      while ops and self.compare(ops[-1], char):
        nodes.append(self.buildNode(ops.pop(), nodes.pop(), nodes.pop()))
      ops.append(char)
      
    while ops:
      nodes.append(self.buildNode(ops.pop(), nodes.pop(), nodes.pop()))
    
    return nodes[-1]
    
    
  def buildNode(self, op, right, left):
    return Node(op, left, right)
  
  def compare(self, prev, curr):
    if prev == '(' or prev == ')': return False
    return prev == '*' or prev == '/' or curr == '+' or curr == '-'

  
class Solution:
  def expTree(self, s):
    nodes, ops = [], []
    
    for char in s:
      if char.isdigit():
        nodes.append(char)
        continue
      
      if char == '(':
        ops.append(char)
        continue
      
      if char in '+-/*':
        while ops and self.compare(ops[-1], char):
          nodes.append(self.buildNode(ops.pop(), nodes.pop(), nodes.pop()))
        ops.append(char)
        continue
      
      if char == ')':
        while ops[-1] != '(':
          nodes.append(self.buildNode(ops.pop(), nodes.pop(), nodes.pop()))
        ops.pop()
        
    while ops:
      nodes.append(self.buildNode(ops.pop(), nodes.pop(), nodes.pop()))       
    
    return nodes[-1]
  
  def compare(self, prev, curr):
    if prev == '(' or prev == ')': return False
    if prev == '*' or prev == '/': return True
    if curr == '+' or curr == '-': return True
    return False
  
  def buildNode(self, op, right, left):
    return Node(op, left, right)


  

def runSolution():
  solution = Solution()
  print(solution.expTree("3*4-2*5"))
  print(solution.expTree("2-3/(5*2)+1"))
  print(solution.expTree("1+2+3+4+5"))
  pass
runSolution()

