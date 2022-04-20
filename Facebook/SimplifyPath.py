'''

  71. Simplify Path

  /home/edit/../

  home -> edit -> home = /home
  
'''


import re


def simplify(s):
  s = re.sub('/+', '/', s)
  s = s.split('/')
  stack = []
  print(s)
  for item in s:
    if item == '' or item == '.': 
      continue

    elif item == '..': 
      if len(stack) > 0: stack.pop()
      
    else: 
      stack.append(item)
  
  print(stack)
  return '/' + '/'.join(stack)

  
  


# print(simplify('/home/'))
# print(simplify('/../'))
# print(simplify('/home//foo/'))
print(simplify("/a/./b/../../c/"))