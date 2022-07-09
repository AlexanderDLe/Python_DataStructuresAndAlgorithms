from enum import Enum

class Airline:
  def __init__(self, name, airlineID, location, scheduledFlights):
    self.name = name
    self.airlineID = airlineID
    self.location = location
    self.scheduledFlights = scheduledFlights
  
class Aircraft:
  def __init__(self, seats, aircraftID):
    self.seats = seats
    self.aircraftID = aircraftID
  
class SeatType(Enum):
  Economy = 1
  Business = 2
  FirstClass = 3
  
class Seat:
  def __init__(self, seatId, seatType): pass
  
