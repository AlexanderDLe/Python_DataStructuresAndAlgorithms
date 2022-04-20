'''

  227. Basic Calculator 2

'''

import math
import re


def calculate(s):
  stack = []
  op = '+'
  num = 0
  s = re.sub(' ', '', s)
  
  for i, char in enumerate(s):
    if char == ' ': continue

    if char.isnumeric():
      num = (num * 10) + int(char)
      if i < len(s) - 1: continue

    if   op == '+':
      stack.append(num)
      op = char
    elif op == '-':
      stack.append(-num)
      op = char
    elif op == '*':
      top = stack.pop()
      stack.append(top * num)
    elif op == '/':
      top = stack.pop()
      div = top/num
      res = math.floor(div) if div > 0 else math.ceil(div)
      stack.append(res)
      
    op = char
    num = 0
  
  return sum(stack)


# print(calculate("3+2*2"))
# print(calculate(" 3/2 "))
# print(calculate(" 3+5 / 2 "))
print(calculate("14-3/2"))