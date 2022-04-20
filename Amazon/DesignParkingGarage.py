class ParkingSystem:
  def __init__(self, big, medium, small) -> None:
    self.parking = {
      1: big,
      2: medium,
      3: small
    }

  def addCar(self, carType: int) -> bool:
    availability = self.parking[carType]

    if availability > 0:
      self.parking[carType] = availability - 1
      return True
    else:
      return False
    


parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))