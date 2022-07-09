'''

  2018. Check if Word Can Be Placed In Crossword

'''

class Solution:
  def placeWordInCrosswordStar(self, board, word):
    n = len(word)
    words = [word,word[::-1]]
    
    for B in board, zip(*board):
      for row in B:
        candidates = ''.join(row).split('#')
        
        for w in words:
          for cand in candidates:
            if len(cand) != n: continue
            if all(cand[i] == w[i] or cand[i] == ' ' for i in range(n)): return True
            
    return False
    
    
  
def runSolution():
  solution = Solution()
  print(solution.placeWordInCrosswordStar(
    board = [
      ["#", " ", "#"],
      [" ", " ", "#"],
      ["#", "c", " "]],
    word = "abc"
  ))
  print(solution.placeWordInCrosswordStar(
    board = [
      [" ", "#", "a"],
      [" ", "#", "c"],
      [" ", "#", "a"]],
    word = "ac"
  ))
  print(solution.placeWordInCrosswordStar(
    board = [
      ["#", " ", "#"], 
      [" ", " ", "#"], 
      ["#", " ", "c"]], 
    word = "ca"
  ))
  pass
runSolution()