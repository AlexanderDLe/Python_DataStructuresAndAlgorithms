'''

  1041. Robot Bounded in Circle


  Circle if:

  1. Robot ends in same position
  2. Robot has different direction
'''

def robotBoundedInCircle(instructions):
  dirX, dirY = 0, 1
  x, y = 0, 0

  for d in instructions:
    if d == 'G':
      x, y = x + dirX, y + dirY 
    elif d == 'L':
      dirX, dirY = (dirY * -1), dirX
    elif d == 'R':
      dirX, dirY = dirY, (dirX * -1)

  return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)

print(robotBoundedInCircle('GGLLGG'))