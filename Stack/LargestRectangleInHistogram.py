'''

  84. Largest Rectangle in Histogram

'''


class Solution:
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
  
def runSolution():
  solution = Solution()
  print(solution.largestRectangleArea([2,1,5,6,2,3]))
  print(solution.largestRectangleArea([1,1]))
  pass
runSolution()
