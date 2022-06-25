'''

  588. Design In-Memory File System

'''

class FileSystem:
  def __init__(self):
    self.trie = {}

  def ls(self, path):
    node = self.trie
    arr = path.split('/')
    prev = None
    
    for item in arr:
      if item == '': continue
      if item not in node: continue
      
      prev = item
      node = node[item]
    
    if 'content' in node: return [prev]
    return sorted(list(node.keys()))

  def mkdir(self, path):
    node = self.trie
    arr = path.split('/')
    
    for item in arr:
      if item == '': continue
      node = node.setdefault(item, {})

  def addContentToFile(self, filePath, content):
    node = self.trie
    arr = filePath.split('/')
    
    for item in arr:
      if item == '': continue
      node = node.setdefault(item, {})
    
    if 'content' in node: node['content'] += content
    else                : node['content'] = content

  def readContentFromFile(self, filePath):
    node = self.trie
    arr = filePath.split('/')
    
    for item in arr:
      if item == '': continue
      if item not in node: return []
      node = node[item]
    
    if 'content' not in node: return []
    return node['content']


def runSolution():
  ["ls","ls","ls"]
  [["/w"],["/"],["/dycete"]]

  fileSystem = FileSystem()
  fileSystem.mkdir("/m")
  print(fileSystem.ls("/m"))                         
  fileSystem.mkdir("/w")
  print(fileSystem.ls("/"))                         
  print(fileSystem.ls("/w"))                         
  print(fileSystem.ls("/"))                         
  fileSystem.addContentToFile("/dycete", "emer")
  print(fileSystem.ls("/w"))                         
  print(fileSystem.ls("/"))                         
  print(fileSystem.ls("/dycete"))
  
  
  # fileSystem = FileSystem()
  # print(fileSystem.ls("/"))                         # return []
  # fileSystem.mkdir("/a/b/c")
  # print(fileSystem.ls("/a/b"))                         # return ["a"]
  # fileSystem.mkdir("/a/b/a")
  # print(fileSystem.ls("/a/b"))                         # return ["a"]
  
  
  # fileSystem = FileSystem()
  # print(fileSystem.ls("/"))                         # return []
  # fileSystem.mkdir("/a/b/c")
  # fileSystem.addContentToFile("/a/b/c/d", "hello")
  # print(fileSystem.ls("/"))                         # return ["a"]
  # print(fileSystem.ls("/a/b/c/d"))                  # return 'd'
  # print(fileSystem.ls("/a/b/c"))                    # return ['d']
  # print(fileSystem.readContentFromFile("/a/b/c/d")) # return "hello"
  pass
runSolution()
