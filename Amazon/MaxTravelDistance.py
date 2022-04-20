'''
  Given max. travel distance and forward and backward route list, return pair 
  of ids of forward and backward routes that optimally utilized the max travel distance.:

  eg: max travel distance is : 11000
  forward route list :    [1,3000],[2,5000],[3,4000],[4,10000]
  backward route list : [1,2000],[2,3000],[3,4000]

  Result : [2,3]  ...2 is from forward and 3 is from backward...total distance is 9000...


  no other combination is there which is >9000 and <=11,000.......0(n^2) solution is 
  straight forward, thinking that sorting both might help.

'''

def maxDistance(forward, backward, maxDistance):
  forward.sort(key=lambda x: x[1], reverse=True)
  backward.sort(key=lambda x: x[1])

  result = [-1, -1]
  max = 0
  f = 0
  b = 0

  while f < len(forward) and b < len(backward):
    Fid, Fdistance = forward[f]
    Bid, Bdistance = backward[b]
    currDistance = Fdistance + Bdistance

    if currDistance > max and currDistance <= maxDistance:
      max = currDistance
      result = [Fid, Bid]

    if currDistance > maxDistance: f += 1
    else                         : b += 1

  return result


print(maxDistance(
  [[1,3000],[2,5000],[3,4000],[4,10000]], 
  [[1,2000],[2,3000],[3,4000]],
  11000
))