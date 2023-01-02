from abc import ABC
from enum import Enum

class RentalStatus(Enum):
  Available = 1
  Unavailable = 2
  Reserved = 3
  Rented = 3
  

class Vehicle(ABC):
  def __init__(self, vehicleID, make, model, year, color, mileage, status = RentalStatus.Available):
    self.vehicleID = vehicleID
    self.make = make
    self.model = model
    self.year = year
    self.color = color
    self.mileage = mileage
    self.status = status
    
  def updateInformation(self): pass
  def updateStatus(self): pass
  
class Car(Vehicle): None
class Truck(Vehicle): None
class Van(Vehicle): None
class SUV(Vehicle): None
class Motorcycle(Vehicle): None