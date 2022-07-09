'''

  1209. Remove All Adjacent Duplicates in String II
  
'''

class Solution:
  def removeDuplicates(self, s, k):
    stack = []
    
    for char in s:
      if stack and stack[-1][0] == char:
        char, freq = stack.pop()
        freq += 1
        if freq < k: stack.append((char, freq))
        continue
    
      stack.append((char, 1))
        
    result = ''
    for char, freq in stack:
      result += char * freq
      
    return result
    
  
def runSolution():
  solution = Solution()
  print(solution.removeDuplicates(s = "abcd", k = 2))
  print(solution.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
  print(solution.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))
  pass
runSolution()