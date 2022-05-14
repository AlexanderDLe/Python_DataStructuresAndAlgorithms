'''

  211. Design Add and Search Words Data Structure

'''

from collections import deque


class WordDictionary:  
  def __init__(self):
    self.trie = {}

  def addWord(self, word):
    node = self.trie
    
    for char in word:
      if char not in node: node[char] = {}
      node = node[char]
    
    node['word'] = True

  def search(self, word):
    queue = deque([self.trie])
    
    for char in word:
      if len(queue) == 0: break
      if char == '.':
        for _ in range(len(queue)):
          n = queue.popleft()
          for key in n.keys():
            if key != 'word': queue.append(n[key])
      else:
        for _ in range(len(queue)):
          n = queue.popleft()
          if char in n: queue.append(n[char])
    
    for item in queue:
      keys = set(item.keys())
      if 'word' in keys: return True
    return False
    
def runSolution():
  # wordDictionary = WordDictionary()
  # wordDictionary.addWord("bad")
  # wordDictionary.addWord("dad")
  # wordDictionary.addWord("mad")
  # print(wordDictionary.search("pad"))
  # print(wordDictionary.search("bad"))
  # print(wordDictionary.search(".ad"))
  # print(wordDictionary.search("b.."))
  # print(wordDictionary.search("bad."))
  
  wordDictionary2 = WordDictionary()
  wordDictionary2.addWord("at")
  wordDictionary2.addWord("and")
  wordDictionary2.addWord("an")
  wordDictionary2.addWord("add")
  print(wordDictionary2.search("a"))
  print(wordDictionary2.search(".at"))
  print(wordDictionary2.search("bat"))
  print(wordDictionary2.search(".at"))
  print(wordDictionary2.search("an."))
  print(wordDictionary2.search("a.d."))
  print(wordDictionary2.search("b."))
  print(wordDictionary2.search("a.d"))
  print(wordDictionary2.search("."))
  pass
runSolution()

