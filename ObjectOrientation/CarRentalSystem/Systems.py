import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
##########################################################

from Vehicle import Vehicle, RentalStatus
from Users import Customer, Admin

class NotificationSystem:
  def __init__(self):
    self.events = []

class CustomerSystem:
  def __init__(self):
    pass

class VehicleSystem:
  def __init__(self):
    self.vehicles = {}
    
  def addNewVehicle(self, vehicle): pass
  def removeVehicle(self, vehicle): pass
  
  def updateVehicleInformation(self, vehicle): pass
  def updateVehicleStatus(self, vehicle, status): pass
  

class CarRentalSystem:
  def __init__(self):
    self.customerSystem = CustomerSystem()
    self.vehicleSystem = VehicleSystem()
    self.notificationSystem = NotificationSystem()
  
  def reserveVehicle(self, customer, vehicle): pass
  def cancelReservation(self, customer, vehicle): pass
  def rentVehicle(self, customer, vehicle): pass