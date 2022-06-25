class Account:
  def __init__(self, name, id, address, email):
    self.name = name
    self.id = id
    self.address = address
    self.email = email


class Member(Account):
  def __init__(self, name, id, address, email):
    super().__init__(name, id, address, email)
    self.shoppingCart = None
    
    
  def addItemToCart(self):
    pass
  
  def removeItemFromCart(self):
    pass
    
  def modifyItemInCart(self):
    pass
  
  def placeOrder(self):
    pass
    
    
class Admin(Account):
  def __init__(self, name, id, address, email):
    super().__init__(name, id, address, email)
    
  def addNewProduct(self):
    pass
  
  def removeProduct(self, productID):
    pass
  
  def modifyProduct(self, productParams):
    pass