'''

  735. Asteroid Collision

'''


class SolutionFirstAttempt:
  def asteroidCollision(self, asteroids):
    stack = []
    
    for asteroid in asteroids:
      if not stack or asteroid > 0:
        stack.append(asteroid)
        continue
        
      while stack:
        top = stack[-1]
        
        # If incoming negative asteroid is equal to top, then both will be destroyed
        if top > 0 and top == abs(asteroid):
          stack.pop()
          break
        
        # If incoming negative asteroid is bigger than top, then it will destroy top
        elif top > 0 and top < abs(asteroid): 
          stack.pop()
          
          if not stack:
            stack.append(asteroid)
            break
          
        
        # If incoming negative asteroid is smaller than top, then it will be destroyed
        elif top > 0 and top > abs(asteroid): break
        
        # If top is a negative asteroid, then it will be ignored. Incoming will be added
        else:
          stack.append(asteroid)
          break
      
        
    return stack
  
class Solution:
  def asteroidCollision(self, asteroids):
    stack = []
    
    for num in asteroids:
      if num > 0:
        stack.append(num)
      else:
        # While top positive value is smaller than incoming negative value, destroy top
        while stack and stack[-1] > 0 and stack[-1] < abs(num):
          stack.pop()
        
        # If stack is empty or top is negative, then append to stack
        if not stack or stack[-1] < 0:
          stack.append(num)
          
        # If top is equal in value, destroy both
        elif stack[-1] == -num:
          stack.pop()
    
    return stack
  
  
def runSolution():
  solution = Solution()
  print(solution.asteroidCollision(asteroids = [5,10,-5]))
  print(solution.asteroidCollision(asteroids = [8,-8]))
  print(solution.asteroidCollision(asteroids = [10,2,-5]))
  print(solution.asteroidCollision(asteroids = [-2,-1,1,2]))
  print(solution.asteroidCollision(asteroids = [1,-2,-2,-2]))
  pass

runSolution()