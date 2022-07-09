class PaymentSystem:
  def validateTransaction(passenger, transaction): pass
  def processTransaction(passenger, transaction): pass
  def issueRefund(passenger, transaction): pass

class BookingSystem:
  def bookFlight(passenger, flight): pass
  def cancelFlight(passenger, flight): pass
  def modifyFlight(passenger, flight): pass

class SearchSystem:
  def queryFlight(params): pass

class SchedulingSystem:
  def addFlightToSchedule(admin, flight): pass
  def modifyFlightSchedule(admin, flight): pass
  def removeFromSchedule(admin, flight): pass
  
  def createFlight(admin, airline, aircraft, crew, schedule): pass
  def modifyFlight(admin, airline, aircraft, crew, schedule): pass
  def deleteFlight(admin, flight): pass

class NotificationSystem:
  def notify(): pass

class AirlineSystem:
  def __init__(self):
    self.PaymentSystem = PaymentSystem()
    self.BookingSystem = BookingSystem()
    self.SearchSystem  = SearchSystem()
    self.SchedulingSystem = SchedulingSystem()
    
  def bookFlight(passenger, reservation): pass
  def cancelFlight(passenger, reservation): pass