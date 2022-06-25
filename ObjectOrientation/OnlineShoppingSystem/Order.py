from enum import Enum

class OrderStatus(Enum):
  Pending = 1
  Shipped = 2
  Fulfilled = 3
  Cancelled = 4
  Refunded = 5

class Order:
  def __init__(self, orderID, items, total, status = OrderStatus.Pending):
    self.orderID = orderID
    self.items = items
    self.total = total
    self.status = status
    
  def updateStatus(self, newStatus):
    pass
  
  def makePayment(self):
    pass
  
  