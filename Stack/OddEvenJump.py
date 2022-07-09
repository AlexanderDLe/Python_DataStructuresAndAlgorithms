'''

  975. Odd Even Jump

'''


class Solution:
  def oddEvenJumps(self, A):
    
    # Sort indices of A by values of A
    # Generate list of indices we can jump to on next odd Jump
    sortedIndices = sorted(range(len(A)), key = lambda i: A[i])
    oddNext = self.makeStack(sortedIndices)
    
    # Generate list of indices we can jump to on next odd Jump
    sortedIndices.sort(key = lambda i: A[i], reverse = True)
    evenNext = self.makeStack(sortedIndices)
    
    # Initialize odd and even lists that will contain the 
    # information of if the end can be reached
    # from the respective index
    odd = [False] * len(A)
    even = [False] * len(A)
    
    # The last index is always counted
    odd[len(A) - 1] = even[len(A) - 1] = True
    
    # Iterate through A backwards, starting at next to last element
    for i in range(len(A) - 2, -1, -1):
      
      # If an odd jump is available from current index,
      # check if an even jump landed on the index of the available
      # odd jump and set current index in odd to True if it did
      if oddNext[i] is not None:
        odd[i] = even[oddNext[i]]
      
      if evenNext[i] is not None:
        even[i] = odd[evenNext[i]]
      
    return sum(odd)
    
  
  def makeStack(self, sortedIndices):
    result = [None] * len(sortedIndices)
    stack = []
    
    for i in sortedIndices:
      while stack and i > stack[-1]:
        result[stack.pop()] = i
      stack.append(i)
    
    del stack
    return result
  
def runSolution():
  solution = Solution()
  print(solution.oddEvenJumps(A = [10,13,12,14,15]))
  # print(solution.oddEvenJumps(A = [2,3,1,1,4]))
  # print(solution.oddEvenJumps(A = [5,1,3,4,2]))
  pass
runSolution()
