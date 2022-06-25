class Guest:
  def __init__(self):
    pass
  def signIn(self):
    pass
  def registerAccount(self):
    pass

  
class Member():
  def __init__(self, name, email, userID, points):
    pass
  def postQuestion(self, title, question, tags):
    pass
  def postAnswer(self, questionID, answer):
    pass  
  def postComment(self, contentID, comment):
    pass
  def editQuestion(self):
    pass
  def editAnswer(self):
    pass
  def editComment(self):
    pass
  def upvote(self):
    pass
  def downvote(self):
    pass
  

class Moderator(Member):
  def __init__(self, name, email, userID, points):
    super().__init__(name, email, userID, points)
  def closeQuestion(self):
    pass
  def openQuestion(self):
    pass
  def deleteQuestion(self):
    pass
  def editQuestion(self):
    pass