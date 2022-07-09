'''

  Problem description (core)
  Implement a generic translator class where you can add translations from 
  any language to any other languge to the knowledge base and can query the 
  same way. It should allow multi-level translations.
  
  Multi-level translations: If there's a word translation in the
  knowledgebase for English <-> Spanish and Spanish <-> Hindi, when 
  queried for Hindi -> English for the same word, function should 
  still be able to return it if there's an indirect relation.
  
'''

class UnionFind:
  def __init__(self, words):
    self.translations = {}
    self.roots = {}
    
    for relation in words:
      nodeA, nodeB = relation
      if nodeA not in self.roots: self.roots[nodeA] = nodeA
      if nodeB not in self.roots: self.roots[nodeB] = nodeB
      
      self.union(nodeA, nodeB)
    
    for node in list(self.roots.keys()):
      root = self.find(node)
      language, definition = node
      
      if root not in self.translations: self.translations[root] = {}
      self.translations[root][language] = definition
      
    print(self.translations)
  
  def find(self, node):
    roots = self.roots
    
    if node != roots[node]:
      roots[node] = self.find(roots[node])
    return roots[node]
  
  def union(self, nodeA, nodeB):
    rootA = self.find(nodeA)
    rootB = self.find(nodeB)
    self.roots[rootA] = rootB

class Solution:
  def __init__(self,words):
    self.UF = UnionFind(words)
  
  
def runSolution():
  solution = Solution([
    [('English', 'Thank You'), ('Spanish', 'Gracias')],
    [('Spanish', 'Gracias'), ('Japanese', 'Arigato')],
    [('Spanish', 'Adios'), ('Japanese', 'Sayanora')],
    [('English', 'Bye'), ('Spanish', 'Adios')],
    [('Portuguese', 'Tchau'), ('Spanish', 'Adios')],
  ])
  # print(solution.main())
  pass
runSolution()