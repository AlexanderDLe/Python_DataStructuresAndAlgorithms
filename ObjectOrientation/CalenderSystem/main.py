from calendar import Calendar
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
##################################################
from Events import EventSystem

class User:
  def __init__(self, userID, name, email, phone): 
    pass
  


class NotificationSystem:
  def __init__(self):
    pass
  
class CalendarSystem:
  def __init__(self, calendarID, calendarType, User):
    self.calenderID = calendarID
    self.eventSystem = EventSystem()
    self.notificationSystem = NotificationSystem()
    
    
def runSolution():
  calendarSystem = CalendarSystem()
  