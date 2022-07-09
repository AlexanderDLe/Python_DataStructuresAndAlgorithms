from abc import ABC
from enum import Enum

class TransactionStatus:
  Pending = 1
  Complete = 2
  Cancelled = 3

class Transaction(ABC):
  def __init__(self, id, timestamp, status = TransactionStatus.Pending):
    self.id = id
    self.timestamp = timestamp
    self.status = status
  
  def processTransaction(self):
    pass

class Withdrawl(Transaction):
  def __init__(self, id, timestamp, status, amount):
    super().__init__(id, timestamp, status, amount)
    self.amount = amount
    
  def processTransaction(self):
    return self.amount
  
class Deposit(Transaction):
  def __init__(self, id, timestamp, status, amount):
    super().__init__(id, timestamp, status, amount)
    self.amount = amount
    
  def processTransaction(self):
    return self.amount
  
class Transfer(Transaction):
  def __init__(self, id, timestamp, status=TransactionStatus.Pending):
    super().__init__(id, timestamp, status)