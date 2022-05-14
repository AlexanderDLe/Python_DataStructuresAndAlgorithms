'''

  208. Implement Trie (Prefix Tree)

'''

class Trie:
    def __init__(self):
      self.trie = {}

    def insert(self, word):
      node = self.trie
      
      for char in word:
        if char not in node: node[char] = {}
        node = node[char]
      
      node['word'] = True

    def search(self, word):
      node = self.trie
      
      for char in word:
        if char not in node: return False
        node = node[char]
      
      if 'word' in node: return True
      return False

    def startsWith(self, prefix):
      node = self.trie
      
      for char in prefix:
        if char not in node: return False
        node = node[char]
      
      return True
    
def runSolution():
  trie = Trie()
  trie.insert("apple")
  print(trie.search("apple"))
  print(trie.search("app"))
  print(trie.startsWith("app"))
  trie.insert("app")
  print(trie.search("app"))
  pass
runSolution()

