class Vehicle:

    def __init__(self, trademark: str, model: str, year: int):
        self.trademark = trademark
        self.model = model
        self.year = year
        self.mileage = 0

    def __str__(self) -> str:
        return f"{self.trademark} {self.model} ({self.year})"

    def run(self, distance: float) -> None:
        self.mileage += distance
        print(f"{self.trademark} {self.model} a parcouru {distance} km.")


car1 = Vehicle("Toyota", "Corolla", 2020)
car2 = Vehicle("Honda", "Civic", 2019)
car1.run(100)
car2.run(150)
car2.run(270)

print(car1.mileage)  # Affiche : 100
print(car2.mileage)  # Affiche : 150
print()


class RegisteredVehicle:
    count = 0

    def __init__(self, trademark: str, model: str, year: int):
        RegisteredVehicle.count += 1
        self.trademark = trademark
        self.model = model
        self.year = year
        self.plate = self.register_plate()

    def register_plate(self):
        return f"{self.trademark[:3].upper()}-{self.model[:3].upper()}-{self.year}-" + str(self.count).zfill(3)

    def reset_count(self, value: int) -> None:
        self.count = value
        self.plate = self.register_plate()


car1 = RegisteredVehicle("Toyota", "Corolla", 2020)
car2 = RegisteredVehicle("Renault", "Clio", 2018)
car3 = RegisteredVehicle("Peugeot", "208", 2019)
car3.reset_count(880)

print(RegisteredVehicle.count)  # Affiche : 3
print(car1.count)  # Affiche : 3
print(car2.count)  # Affiche : 3
print(car3.count)  # Affiche : 880
print(car1.plate)  # Affiche : TOY-COR-2020-001


class Vehicle2:

    def __init__(self, trademark: str, model: str, year: int):
        self.trademark = trademark
        self.model = model
        self.year = year
        self._mileage = 0

    @property
    def mileage(self) -> float:
        return self._mileage

    @mileage.setter
    def mileage(self, value: float) -> None:
        if value >= 0:
            self._mileage = value
        else:
            raise ValueError("La valeur du kilométrage doit être positive.")


car = Vehicle2("Toyota", "Corolla", 2020)
print(car.mileage)  # Affiche : 0
car.mileage = 100
print(car.mileage)  # Affiche : 100
car.mileage = -50  # Lève une exception ValueError
