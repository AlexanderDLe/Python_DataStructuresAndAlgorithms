from abc import ABC

class Account(ABC):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    
class Player(Account):
  def __init__(self, name, email):
    super().__init__(name, email)
    self.chips = 100
    
  def obtainHand(self, hand):
    self.hand = hand
    
  def getHand(self):
    return self.hand