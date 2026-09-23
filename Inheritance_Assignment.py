class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


# Objects
car = Car("Toyota", "Fortuner", 7)
bike = Bike("Yamaha", "R15", 155)

print("Car:")
print(car.brand)
print(car.model)
print(car.seats)

print("\nBike:")
print(bike.brand)
print(bike.model)
print(bike.engine_cc)