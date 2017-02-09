import pickle

class CarRecord:
    def __init__(self):
        self.registration = None
        self.mileage = None

ThisCar = CarRecord()
Car = [ThisCar for i in range(100)]

CarFile = open('Cars.DAT','wb')

for i in range(100):
    pickle.dump(Car[i],CarFile)

CarFile.close()

CarFile = open('Cars.DAT','rb')
while True:
    try:
        Car.append(pickle.load(CarFile))

    except EOFError:
        CarFile.close()
        break
g ggg 
