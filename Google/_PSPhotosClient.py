'''

  Problem statement:
  Suppose you are working on Google Photos. you are wring the client application. Request comes to you to upload N photos. you fire the request to server to upload those N photos to server. Then the server responds back with acknowledgements that a particular photo is uploaded.
  Example. Suppose you are uploading 10 Photos, The server can respond back in any order, such as 1,2,4,5,3,7,6,10,9,8 . Now at any given point of time we need to check what is the maximum photo number which has been uploaded continously.
  Example.

  ack(1),
  getMax()-> returns 1, because the maximum photo uploaded is 1
  ack(2),
  getMax()-> returns 2, because the maximum photo uploaded is 2
  ack(4)
  getMax()-> returns 2 only because 3 has not been recieved yet
  ack(5)
  getMax()-> returns 2 again because 3 has not been recieved yet
  ack(3)
  getMax()-> returns 5 because we recieved 3 and 4 and 5 also we recieved eralier. using this example you have to complete the following class

'''

class PhotosClient:
  def __init__(self, n):
    self.array = (n + 1) * [0]
    self.array[0] = 1
    self.curr = 0
  
  def ack(self, x):
    self.array[x] = 1
    if x == self.curr + 1:
      self.curr = self.traverse()
      
  def traverse(self):
    curr, array = self.curr, self.array
    
    while curr < len(array) and array[curr + 1] == 1:
      curr += 1
    
    return curr
  
  def getMax(self):
    return self.curr

  

def runSolution():
  photosClient = PhotosClient(10)
  print(photosClient.getMax())
  photosClient.ack(1)
  print(photosClient.getMax())
  photosClient.ack(2)
  print(photosClient.getMax())
  photosClient.ack(4)
  print(photosClient.getMax())
  photosClient.ack(5)
  print(photosClient.getMax())
  photosClient.ack(3)
  print(photosClient.getMax())
  
  pass
runSolution()