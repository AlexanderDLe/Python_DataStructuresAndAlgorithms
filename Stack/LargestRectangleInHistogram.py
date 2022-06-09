'''

  84. Largest Rectangle in Histogram


  2  1  5  6  2  3
              ^
  start = 3
  prevIndex  = 2
  prevHeight = 5
  currArea = 5 * (4 - 2) = 10
  
  
  stack = [(0, 1), (2, 5)]
  maxArea = 10
  
'''


class SolutionRef:
  def largestRectangleArea(self, heights):
    maxArea = 0
    stack = []
    
    for i, h in enumerate(heights):
      start = i
      
      while stack and h < stack[-1][1]:
        prevIndex, prevHeight = stack.pop()
        currArea = prevHeight * (i - prevIndex)
        maxArea = max(currArea, maxArea)
        start = prevIndex
      
      stack.append((start, h))

    for i, h in stack:
      maxArea = max(maxArea, h * (len(heights) - i))      

    return maxArea
  
class Solution:
  def largestRectangleArea(self, heights):
    stack = []
    maxArea = 0
    
    for i, h in enumerate(heights):
      start = i
      
      while stack and h < stack[-1][1]:
        prevIndex, prevHeight = stack.pop()
        currArea = prevHeight * (i - prevIndex)
        maxArea = max(maxArea, currArea)
        start = prevIndex
      
      stack.append((start, h))
    
    for i, h in stack:
      maxArea = max(maxArea, h * (len(heights) - i))
    
    return maxArea

def runSolution():
  solution = Solution()
  print(solution.largestRectangleArea([2,1,5,6,2,3]))
  print(solution.largestRectangleArea([2,4]))
  pass
runSolution()
