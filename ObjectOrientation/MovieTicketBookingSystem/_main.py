import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from enum import Enum
from abc import ABC
##############################################

class Account():
  def __init__(self, id, password, name, email, phone):
    self.id = id
    self.password = password
    self.name = name
    self.email = email
    self.phone = phone
  
class User(Account):
  def __init__(self, id, password, name, email, phone):
    super().__init__(id, password, name, email, phone)
  def createBooking():pass
  def getBookings(): pass
  def createOrder():pass
  def cancelOrder():pass
  

class Admin(Account):
  def __init__(self, id, password, name, email, phone):
    super().__init__(id, password, name, email, phone)
  def addMovie():pass
  def removeMovie():pass
  def createShowing(): pass
  def removeShowing(): pass
  def blockCustomer(): pass

class BookingStatus(Enum):
  Pending = 1
  Complete = 2
  Cancelled = 3

class Order:
  def __init__(self, orderID, name, email, theater, price, status = BookingStatus.Pending ):
    self.orderID = orderID
    self.name = name
    self.email = email
    self.theater = theater
    self.price = price
    self.status = status
def makePayment(): pass
def cancelOrder(): pass


class Showing:
  def __init__(self, movie, timeStart, timeEnd, price, seats, theaterID, roomNumber):
    self.movie = movie
    self.timeStart = timeStart
    self.timeEnd = timeEnd
    self.price = price
    self.seats = seats
    self.theaterID = theaterID
    self.roomNumber = roomNumber
    
  def reserveSeats(): pass

class Movie:
  def __init__(self, title, description, duration, movieID, language, releaseDate, genre):
    self.title = title
    self.description = description
    self.duration = duration
    self.movieID = movieID
    self.language = language
    self.releaseDate = releaseDate
    self.genre = genre

class Room():
  def __init__(self, seatMap, roomNumber):
    self.seatMap = seatMap
    self.roomNumber = roomNumber

class Theater(Account):
  def __init__(self, id, password, name, email, phone, theaterID, rooms):
    super().__init__(id, password, name, email, phone)
    self.theaterID = theaterID
    self.rooms = rooms

class SearchSystem:
  def __init__(self, catalog):
    self.catalog = catalog
  def searchByTitle(): pass
  def searchByCategory(): pass
  def searchByGenre(): pass
  def searchByReleaseData(): pass
  def searchByCity(): pass
  
class Catalog:
  def __init__(self, movies):
    self.movies = movies

def main():
  print('Run Program...')
  
main()