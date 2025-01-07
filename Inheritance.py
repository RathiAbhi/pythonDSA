class Vehicle:
    def __init__(self,wheels):
        self.wheels = wheels

    def display(self):
        print(f"Vehicle has {self.wheels} wheels")

class Car(Vehicle):
    def __init__(self,wheels,brand):
        super().__init__(wheels)
        self.brand = brand

    def display(self):
        super().display()
        print(f"Brand: {self.brand}")


car = Car (4,"Tesla")
car.display()