from abc import ABC

class Account(ABC):
  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    
class Passenger(Account):
  def __init__(self, name, email, phone, passengerID, itinerary):
    super().__init__(name, email, phone)
    self.passengerID = passengerID
    self.itinerary = itinerary
  
class Employee(Account):
  def __init__(self, name, email, phone, employeeID):
    super().__init__(name, email, phone)
    self.employeeID = employeeID
  
class Attendant(Employee):
  def __init__(self, name, email, phone, employeeID):
    super().__init__(name, email, phone, employeeID)
  def provideService(): pass
    
class Pilot(Employee):
  def __init__(self, name, email, phone, employeeID):
    super().__init__(name, email, phone, employeeID)
  def flyPlane(): pass  

class Crew():
  def __init__(self, pilots, attendants):
     self.pilots = pilots
     self.attendants = attendants

