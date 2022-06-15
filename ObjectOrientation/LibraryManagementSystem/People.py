class Person:
  def __init__(self, name):
    self.name = name

class Member(Person):
  def __init__(self, name):
    super().__init__(name)
    self.booksCheckedOut = []
    
  def checkoutBook(self, book):
    self.booksCheckedOut.append(book)
    
class Librarian(Person):
  def __init__(self, name):
    super().__init__(name)