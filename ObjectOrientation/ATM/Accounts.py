from abc import ABC

class Account(ABC):
  def __init__(self, name, email, phone, address, id):
    self.name = name
    self.email = email
    self.phone = phone
    self.address = address
    self.id = id
    
class Card:
  def __init__(self, customer, cardNumber, PIN):
    self.customer = customer
    self.cardNumber = cardNumber
    self.PIN = PIN    

class User(Account):
  def __init__(self, name, email, phone, address, id):
    super().__init__(name, email, phone, address, id)
    
class Admin(Account):
  def __init__(self, name, email, phone, address, id):
    super().__init__(name, email, phone, address, id)
