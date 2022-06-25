from enum import Enum

class QEnum:
  Open = 1
  Closed = 2
  Deleted = 3
  Archived = 4

class Question:
  def __init__(self, questionID, title, content, tags, status, voteCount):
    pass
  def editTitle(self):
    pass
  def editContent(self):
    pass
  def editTags(self):
    pass
  def editStatus(self):
    pass
  def close(self):
    pass
  def delete(self):
    pass
  

class Answer:
  def __init__(self, answerID, content):
    pass
  def editContent(self):
    pass
  
  
class Comment:
  def __init__(self, commentID, content):
    pass
  def editContent(self):
    pass