'''
  Problem

  There is a robot on an m x n grid. 

  The robot is initially located at the bot-left corner (i.e., grid[rows-1][0]). The robot tries to move to the top-right corner. 

  The robot can only move either up, right, or diagonally up-right.

  Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

  The test cases are generated so that the answer will be less than or equal to 2 * 109.

  Follow-up: Set of points that must be reached.

  _____________________________________________________________________________

  Example:


  _____________________________________________________________________________

  Constraints

  1. The set of points are valid - subsequent points are able to be accessed within the
  up-right-up+right directions.
  2. The set of cells of contained with the grid.
  3. M and N are greater than 0.

  _____________________________________________________________________________


  Strategy

  1. Create overall DP grid.

  r=3, c=4
  [
    [1, 5, 13, 25],
    [1, 3,  5,  7],
    [1, 1,  1,  1],
  ]

  Each cell must account for all the unique paths that can be used to get there.
  (UP, RIGHT, UP+RIGHT)

  2. If the set of points does not include the very last cell, it must be included as last.

  3. Convert the set of points into matrices where the rows is the x distance between the previous/current row and cols is the distance between previous/current col.

  r=4, c=4
  points = [(2,1), (1, 1), (0, 3)]

  submatrices
  x = rows - (prev[0] - x) - 1
  y = y - prev[1]

  prev = (3, 0) and curr = (2, 1)
  x = 4 - (3 - 2) - 1 = 4 - (1) -1 = 2
  y = 1 - 0 = 1
  append((2, 1))

  prev = (2, 1) and curr = (1, 1)
  x = 4 - (2 - 1) - 1 = 2
  y = 1 - 1 = 0
  append((2, 0))

  prev = (1, 1) and curr = (0, 3)
  x = 4 - (1 - 0) - 1 = 2
  y = 3 - 1 = 2
  append(2, 2)

  submatrices = [(2, 1), (2, 0), (2, 2)]

  4. Keep a running product. For each iteration over the set of points, access its
  unique paths by doing a scan on the sub matrix. When you get the unique paths of the submatrix, multiply it with the running product.

  Ex. If there are x unique paths to get to cellA and y paths to get to cellB, then there are a total of x*y paths.

  _____________________________________________________________________________


'''

class Solution:
  def main(self, rows, cols, points):
    distancesFromStart = self.initDistancesFromStart(rows, cols, points)
    DP = self.initDP(rows, cols)
    print(points)
    result = 1
    for xDistance, yDistance in distancesFromStart:
      result *= DP[rows - xDistance - 1][yDistance]

    return result

  def initDP(self, rows, cols):
    DP = [[0]*cols for _ in range(rows)]	
    for i in range(rows): DP[i][0] = 1
    for i in range(cols): DP[rows-1][i] = 1

    for row in range(rows - 2, -1, -1):
      for col in range(1, cols):
        DP[row][col] += DP[row + 1][col]
        DP[row][col] += DP[row][col - 1]
        DP[row][col] += DP[row + 1][col - 1]

    return DP


  def initDistancesFromStart(self, rows, cols, points):
    if points[-1] != (0, cols-1): 
      points.append((0, cols-1))

    distancesFromStart = []
    prev = (rows - 1, 0)
    for x, y in points:
      distancesFromStart.append((prev[0] - x, y - prev[1]))
      prev = (x, y)

    return distancesFromStart

  
def runSolution():
  solution = Solution()
  print(solution.main(4, 5, [(2,1), (1, 1), (0, 3)]))
  pass
runSolution()