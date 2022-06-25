class Product:
  def __init__(self, productID, productName, sellerID, inventoryCount, price, category):
    self.productID = productID
    self.productName = productName
    self.sellerID = sellerID
    self.inventoryCount = inventoryCount
    self.price = price
    self.category = category
    
  def updatePrice(self, newPrice):
    pass
  
  def updateInventory(self, newCount):
    pass