class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def describe(self):
        return f'{self.name} - транспортное средство c максимальной скоростью {self.max_speed} км/ч'


class Car(Vehicle):
    def __init__(self, name, max_speed, doors):
        super().__init__(name, max_speed)
        self.doors = doors

    def describe(self):
        return (f"Автомобиль {self.name} имеет {self.doors} двери "
                f"и развивает максимальную скорость {self.max_speed} км/ч")


class Bicycle(Vehicle):
    def __init__(self, name, max_speed, gears):
        super().__init__(name, max_speed)
        self.gears = gears

    def describe(self):
        return (f'Велосипед {self.name} имеет {self.gears} скоростей '
                f'и развивает максимальную скорость {self.max_speed} км/ч')


class Plane(Vehicle):
    def __init__(self, name, max_speed, altitude):
        super().__init__(name, max_speed)
        self.altitude = altitude

    def describe(self):
        return (f'Самолёт {self.name}: летает на высоте до {self.altitude} м '
                f'и развивает максимальную скорость {self.max_speed} км/ч')


vehicles = [
    Car("Toyota Camry", 210, 4),
    Bicycle("Stels Navigator", 35, 21),
    Plane("Boeing 737", 850, 12000),
]

for vehicle in vehicles:
    print(vehicle.describe())

# Автомобиль Toyota Camry: едет по дорогам, 4 двери, макс. скорость 210 км/ч
# Велосипед Stels Navigator: движется силой ног, 21 скоростей, макс. скорость 35 км/ч
# Самолёт Boeing 737: летает на высоте до 12000 м, макс. скорость 850 км/ч
