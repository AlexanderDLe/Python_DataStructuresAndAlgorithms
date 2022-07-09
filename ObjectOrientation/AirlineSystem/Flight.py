from enum import Enum

class Schedule:
  def __init__(self, date, time, source, destination):
    self.date = date
    self.time = time
    self.source = source
    self.destination = destination

class FlightStatus:
  Scheduled = 1
  Delayed = 2
  Cancelled = 3
  Departed = 4
  Completed = 5

class Flight:
  def __init__(self, flightID, schedule, crew):
    self.flightID = flightID
    self.shcedule = schedule
    self.crew = crew
    
class Reservation:
  def __init__(self, flight, ):
    pass

class Itinerary:
  def __init__(self, passenger, reservation):
    pass