class Vehicle:
    def __init__(self, trademark: str, model: str, year: int):
        self.trademark = trademark
        self.model = model
        self.year = year
        self._speed = 0

    def accelerate(self) -> None:
        print(f"{self.trademark} {self.model} accélère.")
        self._speed += 10

    def print_speed(self) -> None:
        print(f"{self._speed} km/h")

    @classmethod
    def from_string(cls, vehicle_string: str):
        trademark, model, year = vehicle_string.split(",")
        return cls(trademark, model, int(year))

    @staticmethod
    def is_valid_year(year: int) -> bool:
        return 1900 <= year <= 2024


car = Vehicle("Toyota", "Corolla", 2020)
car.accelerate()
car.print_speed()  # Affiche : 10 km/h


class Car(Vehicle):
    def honk(self) -> None:
        print("Pouet pouet")


noisy_car = Car.from_string("Toyota,Corolla,2020")
noisy_car.honk()  # Affiche : Pouet pouet

print(Car.is_valid_year(2020))  # Affiche : True
print(Car.is_valid_year(2025))  # Affiche : False
car = Vehicle("Toyota", "Corolla", 2020)
car.is_valid_year(2020)
