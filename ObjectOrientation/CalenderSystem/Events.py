from abc import ABC
from enum import Enum

class Event(ABC):
  def __init__(self, title, location, startDate, endDate):
    self.title = title
    self.location = location
    self.startDate = startDate
    self.endDate = endDate

class RecurringEvent(Event):
  def __init__(self, title, location, startDate, endDate):
    super().__init__(title, location, startDate, endDate)
    
class SingleEvent(Event):
  def __init__(self, title, location, startDate, endDate, recurringRate):
    super().__init__(title, location, startDate, endDate)
    self.recurringRate = recurringRate

class EventType(Enum):
  SingleEvent = 1
  RecurringEvent = 2

class EventFactory:
  def createEvent(self, title, location, startDate, endDate, recurringRate, type):
    if type == EventType.SingleEvent:
      return SingleEvent(title, location, startDate, endDate)
    if type == EventType.RecurringEvent:
      return RecurringEvent(title, location, startDate, endDate, recurringRate)

class EventCollection:
  def __init__(self):
    self.archivedEvents = []
    self.upcomingEvents = []
    
  def queryEvents(): pass
  def addEvent(): pass
  def removeEvent(): pass

class EventSystem:
  def __init__(self, events):
    self.eventCollection = EventCollection()
    self.eventFactory = EventFactory()
    
    def addEvent(): pass
    def removeEvent(): pass
    def getEvents(): pass