'''

  1166. Design File System
  
'''

from functools import cmp_to_key

class FileSystem:
  def __init__(self):
    self.trie = {}

  def createPath(self, path, value):
    node = self.trie
    arr = path.split('/')
    n = len(arr)
    
    for i, dir in enumerate(arr):
      if dir == '': continue
      if dir not in node and i < n - 1: return False
      node = node.setdefault(dir, {})
      
    if 'path' in node: return False
    node['path'] = value
    return True
    

  def get(self, path):
    node = self.trie
    arr = path.split('/')
    
    for dir in arr:
      if dir == '': continue
      if dir not in node: return -1
      node = node[dir]
    
    if 'path' in node: return node['path']
    else: return -1
    
    

def runSolution():
  fileSystem1 = FileSystem() 
  print(fileSystem1.createPath("/leet", 1))       # return true
  print(fileSystem1.createPath("/leet/code", 2))  # return true
  print(fileSystem1.get("/leet/code"))            # return 2
  print(fileSystem1.createPath("/leet/code", 3))  # return true
  print(fileSystem1.get("/leet/code"))            # return 2
  print(fileSystem1.createPath("/c/d", 1))        # return false because the parent path "/c" doesn't exist.
  print(fileSystem1.get("/c"))                    # return -1 because this path doesn't exist.
  pass
runSolution()
