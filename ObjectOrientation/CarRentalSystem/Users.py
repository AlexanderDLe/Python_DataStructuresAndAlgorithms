from abc import ABC

class Account(ABC):
  def __init__(self, userID, name, phone, email):
    self.userID = userID
    self.name = name
    self.phone = phone
    self.email = email
  
class Customer(Account):
  def __init__(self, userID, name, phone, email):
    super().__init__(userID, name, phone, email)
    self.rentals = {}
    self.reservations = {}
    
  def addRental(self): None
  def removeRental(self): None
  
  def addReservation(self): None
  def removeReservation(self): None
  
class Admin(Account):
  def __init__(self, userID, name, phone, email):
    super().__init__(userID, name, phone, email)