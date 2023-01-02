'''
  A mountain can be simplified as an isoceles right triangle, whose base 
  rests on the x-axis. The two sides of the mountain are both at 45 degress 
  to the base so the peak of the mountain forms a right angle.
  
  All the mountains are the same color so a mountian is invisible if its peak 
  lies on or within the triangular shape of any other mountain.
  
  Given a list of positions of all the mountain's peaks (x-y coordinates). 
  Output the number of visible mountains.

  Example:

  Input:

  (4, 6)
  (7, 2)
  (2, 5)
  Output: 2

  Point to note:

  here the peak visible are 1 and 3
  Mountains are of the same colour so you have to find the peaks which are visible. 
  The question eventually was about the area covered by a triangle; if any peak 
  point comes into that triangle, then that peak is not visible.
  
  1. Get x axis intersection points for each mountain. 
  i.e start and end pos of each mountain on x axis.
  
  for (x,y) as mountain's peak, its left x axis intersection point will be x-y and 
  right x axis intersection point will be x+y, put these as a pair in a vector <pair <int,int> >

  2. Sort them by pair.first

  3. Now problem reduces to merge interval problem with a twist that we will only merge intervals if one lies completely into another
'''


from math import sqrt


class Solution:
  def main(self, peaks):
    intersections = []
    
    for x, y in peaks:
      intersectL = x - y
      intersectR = x + y
      intersections.append((intersectL, intersectR))
      
    intersections.sort()
    prev = intersections[0]
    result = len(peaks)
    area = self.calculateArea(prev)
    
    for i in range(1, len(intersections)):
      prevL, prevR = prev
      currL, currR = intersections[i]
      
      if currR < prevR:
        result -= 1
      else:
        newArea = self.calculateArea(intersections[i])
        overlap = self.calculateArea((currL, prevR))
        area += newArea - overlap
        prev = intersections[i]
      
    return result, area
  
  def calculateArea(self, intersections):
    length = abs((intersections[0] - intersections[1]) // 2)
    hypotenuse = sqrt(length**2 + length**2)
    squareArea = hypotenuse * 2
    mountainArea = squareArea / 2
    return mountainArea
  
def runSolution():
  solution = Solution()
  print(solution.main(peaks = [(4,6), (7,2), (2,5)]))
  pass
runSolution()