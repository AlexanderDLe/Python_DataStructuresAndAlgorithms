from collections import deque
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from abc import ABC
##############################################

class Entry():
  def __init__(self, name, size, isDir):
    self.name = name
    self.size = size
    self.isDir = isDir    
  def getName(self):
    return self.name
  def getSize(self):
    return self.size
  def getIsDirectory(self):
    return self.isDir

class File(Entry):
  def __init__(self, name, size, extension):
    super().__init__(name, size, False)
    self.extension = extension
  def getExtension(self):
    return self.extension
    
    
class Directory(Entry):
  def __init__(self, name, size):
    super().__init__(name, size, True)
    self.entries = []
  def addEntry(self, entry):
    self.entries.append(entry)
    
class SearchParameters:
  def __init__(self, name=None, extension=None, minSize=0, maxSize=float('inf')):
    self.name = name
    self.extension = extension
    self.sizes = (minSize, maxSize)
    
class Filter(ABC):
  def isValid():
    pass
  
class NameFilter(Filter):
  def isValid(self, param, file: File):
    fileName = file.getName()
    return param in fileName
  
class ExtensionFilter(Filter):
  def isvalid(self, param, file: File):
    fileExtension = file.getExtension()
    return param == fileExtension
  
class SizeFilter(Filter):
  def isValid(self, param, file: File):
    min, max = param
    fileSize = file.getSize()
    return min <= fileSize <= max
  
    
class SearchSystem:
  def __init__(self):
    self.filters = [
      NameFilter(),
      ExtensionFilter(),
      SizeFilter()
    ]
  
  def search(self, directory, params):
    files = []
    queue = deque([directory])
    
    while queue:
      dir = queue.popleft()
    
    return files
  
  def buildFilters(self, params):
    filters = []


def main():
  print('Run Program...')
  system = SearchSystem()
  
  
main()