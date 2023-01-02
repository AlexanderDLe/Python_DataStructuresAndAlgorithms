from collections import deque
from enum import Enum

class CallStatusEnum(Enum):
  Active = 1
  Hold = 2
  Dropped = 3

class CallEvent:
  def __init__(self, phone, timestamp, status = CallStatusEnum.Active):
    self.phone = phone
    self.timestamp = timestamp
    self.status = status

class CallQueue:
  def __init__(self):
    self.queue = deque[CallEvent]()
  
  def enqueueCall(self, callEvent): 
    self.queue.append(callEvent)
    
  def getNextCall(self): 
    return self.queue.popleft()
    
  def isCallAvailable(self):
    while self.queue[0].status == CallStatusEnum.Dropped:
      self.queue.popleft()
      
    return len(self.queue) > 0



class Worker:
  def __init__(self, id, callCenterSystem):
    self.callCenterSystem = callCenterSystem
    self.id = id
    
  def handleCall(self, callEvent): pass
  
  def completeCall(self):
    self.callCenterSystem.completeCall(self)
  
class WorkerSystem:
  def __init__(self, employeeCount, callCenterSystem):
    self.availableWorkers = deque[Worker]()
    self.busyWorkers = set()
    
    for i in range(employeeCount):
      self.availableWorkers.append(Worker(i, callCenterSystem))
      
  def assignWorker(self, callEvent):
    nextWorker = self.availableWorkers.popleft()
    nextWorker.handleCall(callEvent)
    self.busyWorkers.add(nextWorker)
      
  def enqueueWorker(self, worker):
    self.busyWorkers.discard(worker)
    self.availableWorkers.append(worker)      
      
  def isWorkerAvailable(self):
    return len(self.availableWorkers) > 0



class CallCenterSystem:
  def __init__(self, employeeCount):
    self.callQueue = CallQueue()
    self.workerSystem = WorkerSystem(employeeCount, self)
    
  def receiveCall(self, phone, timestamp):
    callEvent = CallEvent(phone, timestamp)
    
    if self.workerSystem.isWorkerAvailable():
      self.workerSystem.assignWorker(callEvent)
    else:
      self.callQueue.enqueueCall(callEvent)
      
  def completeCall(self, worker: Worker):
    if self.callQueue.isCallAvailable():
      nextCall = self.callQueue.getNextCall()
      worker.handleCall(nextCall)
    else:
      self.workerSystem.enqueueWorker(worker)