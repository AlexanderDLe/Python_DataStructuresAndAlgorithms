'''

  353. Design Snake Game

'''

from collections import deque


class SnakeGameMyLongSolution:
  def __init__(self, width, height, food):
    self.rows = height
    self.cols = width
    self.food = food
    self.pos = [0, 0]
    self.tailQueue = [(0, 0)]
    self.tailSet = set([(0, 0)])
    self.score = 0

  def move(self, direction):
    nextRow, nextCol = self.getNextPos(direction)    
    
    # We check if food is found first - if not, we pop tail length.
    # We do this first to update the tail end (in case we run into it)
    foundFood = self.foundFood(nextRow, nextCol)
    if foundFood == False: self.popTailEnd()
    
    # After updating tail end position, we check if it is invalid or not
    if self.invalidCell(nextRow, nextCol): return -1
    
    # Update tail by inserting the current head position
    self.appendTail(nextRow, nextCol)
    
    # Update current position
    self.pos = [nextRow, nextCol]
    
    return self.score
    
  def appendTail(self, nextRow, nextCol):
    self.tailQueue.insert(0, (nextRow, nextCol))
    self.tailSet.add((nextRow, nextCol))

  def popTailEnd(self):
    lastRow, lastCol = self.tailQueue.pop()
    self.tailSet.remove((lastRow, lastCol))      

  def foundFood(self, nextRow, nextCol):
    if len(self.food) == 0: return False
    
    nextFood = self.food[0]
    if nextRow == nextFood[0] and nextCol == nextFood[1]:
      self.food.pop(0)
      self.score += 1
      return True
    else:
      return False

  def getNextPos(self, direction):
    row, col = self.pos
    if direction == 'U': row -= 1
    if direction == 'D': row += 1
    if direction == 'R': col += 1
    if direction == 'L': col -= 1
    return (row, col)

  def invalidCell(self, nextRow, nextCol):
    if nextRow < 0 or nextRow == self.rows: return True
    if nextCol < 0 or nextCol == self.cols: return True
    if (nextRow, nextCol) in self.tailSet : return True
    return False
  
class SnakeGame:
  def __init__(self, width, height, food):
    self.snake = deque([[0,0]])
    self.width = width
    self.height = height
    self.food = deque(food)
    self.direct = {'U': [-1,0], 'L': [0,-1], 'R':[0,1], 'D': [1,0]}

  def move(self, direction):
    snake, food, direct = self.snake, self.food, self.direct
    
    nextRow = snake[0][0] + direct[direction][0]
    nextCol = snake[0][1] + direct[direction][1]
    newHead = [nextRow, nextCol]
    
    # Notice that the new head can be equal to self.snake[-1]
    if self.outOfBounds(nextRow, nextCol): return -1
    if newHead in snake and newHead != snake[-1]: return -1
    
    snake.appendleft(newHead) # Move snake head
    
    # Eat food or move tail
    if food and food[0] == newHead: food.popleft()
    else                          : snake.pop()
      
    return len(snake) - 1
  
  def outOfBounds(self, row, col):
    if row < 0 or row == self.height: return True
    if col < 0 or col == self.width : return True
    return False
    


def runSolution():
  snakeGame = SnakeGame(3, 2, [[1, 2], [0, 1]]);
  print(snakeGame.move("R")) # return 0
  print(snakeGame.move("D")) # return 0
  print(snakeGame.move("R")) # return 1, snake eats the first piece of food. The second piece of food appears at (0, 1).
  print(snakeGame.move("U")) # return 1
  print(snakeGame.move("L")) # return 2, snake eats the second food. No more food appears.
  print(snakeGame.move("U")) # return -1, game over because snake collides with border
runSolution()