class CardReader:
  def readCard(self, card): pass  

class ScreenDisplay:
  def displayMessage(self, message): pass

class Keypad:
  def getInput(self, key): pass
  
class CashDispenser:
  def dispenseCash(self):
    pass

class NetworkManager:
  def verifyAccount(self, card, PIN): pass
  def validateTransaction(self, customer, transaction): pass

class ATMMachine:
  def __init__(self, id, location):
    self.id = id
    self.location = location

    self.cardReader = CardReader()
    self.screenDisplay = ScreenDisplay()
    self.keypad = Keypad()
    self.cashDispenser = CashDispenser()
    self.networkManager = NetworkManager()
    
  def authenticateUser(self):
    PIN = self.keypad.getInput()
    card = self.cardReader.readCard()
    validated = self.networkManager.verifyAccount(card, PIN)
    self.screenDisplay.displayMessage('User is validated.')
    return validated
  
  def makeTransaction(self, customer, transaction):
    valid = self.networkManager(customer, transaction)
    
    if not valid:
      self.screenDisplay.displayMessage('Transaction denied')
      return
    
    if valid:
      self.screenDisplay.displayMessage('Transaction approved')
      
      