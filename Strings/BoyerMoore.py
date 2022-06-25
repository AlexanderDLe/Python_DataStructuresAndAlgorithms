'''

  Boyer Moore String Matching Algo
  
'''

class Solution:
  def partition(self, text, pattern):
    lastOccurMap = {char: i for i, char in enumerate(pattern)}
    tLen, pLen = len(text), len(pattern)
    shifts = 0
    
    while (shifts <= tLen - pLen):
      print(shifts)
      j = pLen - 1
      
      while j >= 0 and pattern[j] == text[shifts + j]:
        j -= 1
      
      if j < 0: return True
      
      mismatch = text[shifts + j]
      mismatchOccurence = lastOccurMap[mismatch] if mismatch in lastOccurMap else -1
      shifts += max(1, j - mismatchOccurence)
      print(mismatch, mismatchOccurence, shifts)
    
    
    return False
      
'''

  lastOccurMap = {
    T: 4
    A: 1
    G: 5
  }
  
  ----------------

  GCAXTGCCTATGTGACC
  TATGTG
     j <-- mismatch
     
  X not in lastOccurMap, therefore mismatchOccurence is -1
  shifts += (j - mismatchOccurence) = 3 + 4
  shifts = 4

  Reasoning: Move the pattern past the mismatch using -1.

  ----------------

  GCAXTGCCTATGTGACC
      TATGTG
           j <-- mismatch
  
  A is in lastOccurMap. 
  mismatchOccurence = lastOccurMap[A] = 1
  shifts += (j - 1) = (5 - 1) = 4
  shifts = 4
  
  Reasoning: Move the pattern until we match the mismatch.
  In this case, we're matching the lastOccurence of A to the
  mismatched A.

  ----------------

  GCAXTGCCTATGTGACC
          TATGTG
         j <-- Complete match. return True.

'''
    
  
def runSolution():
  solution = Solution()
  print(solution.partition(
    text = "GCAXTGCCTATGTGACC", 
    pattern = 'TATGTG'))
  pass
runSolution()
