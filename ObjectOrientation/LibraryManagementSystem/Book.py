from enum import Enum

class BookEnum(Enum):
  Available = 0
  Reserved = 1
  CheckedOut = 2
  
class Book:
  def __init__(self, id, title, author, status = BookEnum.Available):
    self.id = id
    self.title = title
    self.author = author
    self.status = status
    
  def reserve(self):
    self.status = BookEnum.Reserved
    
  def checkout(self):
    self.status = BookEnum.CheckedOut
  
  def returnBook(self):
    self.status = BookEnum.Available
    
books = [
  Book(1, 'Harry Potter', 'JK Rowling', BookEnum.Available),
  Book(2, 'Golden Compass', 'Christopher Paoli', BookEnum.Reserved),
  Book(3, 'Dumbledore Dinner', 'JK Rowling', BookEnum.Available),
  Book(4, 'Lord of the Rings', 'Einstein', BookEnum.Available),
  Book(5, 'Toy Story', 'Disneyworld', BookEnum.CheckedOut),
  Book(6, 'Dune', 'Henry Ford', BookEnum.Available),
  Book(7, 'Random Age', 'Neil Pink', BookEnum.Available),
]