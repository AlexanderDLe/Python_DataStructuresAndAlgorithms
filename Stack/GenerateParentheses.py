'''

  22. Generate Parentheses

'''


class Solution:
  def generateParenthesis(self, n):
    result = []
    
    def DFS(opens, closes, gen):
      if not opens and not closes:
        result.append(gen)
        return

      if opens:
        DFS(opens - 1, closes, gen + '(')
      if closes > opens:
        DFS(opens, closes - 1, gen + ')')
    
    DFS(n, n, '')
    return result
  
def runSolution():
  solution = Solution()
  print(solution.generateParenthesis(3))
  print(solution.generateParenthesis(1))
  pass
runSolution()
