'''

  990. Satisfiability of Equality Equations

  Constraints/Assumptions

  1. Assume strings are valid inputs. '{letter}{equality}{letter}'
  2. Assume at least one pair

  _____________________________________________________________________________


  Strategy

  Union Find Algorithm.

  1. Union all equations that are equal.

  2. If we encounter a contradicting union, we return False.
    a: We find equality where it was previously unequal. a!=b and a==b
    b: We find inequality where it was previously equal. a==b and a!=b
    c: There is a contradicting equality. a!=b yet a==c and c==b

  _____________________________________________________________________________

  Example


  [a==b, b==c, a!=c]

  unionRoots: {
    a: a
    b: b
    c: c
  }

  1. a==b

  Since ==, union a and b.
  unionRoots: {
    a: b
    b: b
    c: c
  }

  2. b==c

  Since ==, union b and c
  unionRoots: {
    a: b
    b: c
    c: c
  }

  2. a!=c

  Since !=, find contradiction between a and c.
  root of a: a -> b -> c
  root of c: c -> c

  They share the same root, yet the equality sign is !=, therefore there is a contradition.
  _____________________________________________________________________________


'''


from itertools import product

class Solution:
  def equationsPossible(self, equations):
    roots = self.initRoots(equations)
    
    def find(x):
      if x != roots[x]:
        roots[x] = find(roots[x])
      return roots[x]
  
    def union(x, y):
      xRoot, yRoot = find(x), find(y)
      roots[xRoot] = yRoot
      
    for equation in equations:
      x, sign, _, y = list(equation)
      if sign == '=': union(x, y)
        
    for equation in equations:
      x, sign, _, y = list(equation)
      if sign == '!' and find(x) == find(y):
        return False
    
    return True
  
  def initRoots(self, equations):
    roots = {}
    for equation in equations:
      x, _, _, y = list(equation)
      roots[x] = x
      roots[y] = y
    return roots
    
  
def runSolution():
  solution = Solution()
  
  print(solution.equationsPossible(
    equations = ["a==b","b!=a"]))
  print(solution.equationsPossible(
    equations = ["b==a","a==b"]))
  pass
runSolution()