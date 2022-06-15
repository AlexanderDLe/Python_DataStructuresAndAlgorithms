import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
##############################################

from Book import Book, BookEnum, books
from People import Member

class LibrarySystem:
  def __init__(self, books):
    self.bookMap = {}
    for book in books:
      self.bookMap[book.id] = book
  
  def checkOutBookForMember(self, member, bookID):
    if not self.canCheckoutBook(bookID): return
    book = self.bookMap[bookID]
    member.checkoutBook(book)
    book.reserve()
  
  def canCheckoutBook(self, ID):
    if ID not in self.bookMap: return False
    if self.bookMap[ID].status != BookEnum.Available: return False
    return True


def main():
  print('Run Library Management Program...')
  system = LibrarySystem(books)
  member1 = Member('Alex')
  
  system.checkOutBookForMember(member1, books[0])
  system.checkOutBookForMember(member1, books[1])
  print(member1.booksCheckedOut)
  
  
  
  
main()