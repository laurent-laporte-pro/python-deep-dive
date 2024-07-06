class Vehicle:
    def __init__(self, trademark: str, model: str, year: int):
        self.trademark = trademark
        self.model = model
        self.year = year
        self._speed = 0

    def __str__(self) -> str:
        return f"{self.trademark} {self.model} ({self.year})"

    def start(self) -> None:
        print(f"{self.trademark} {self.model} démarre.")
        self._speed = 10

    def accelerate(self) -> None:
        print(f"{self.trademark} {self.model} accélère.")
        self._speed += 10

    def slow_down(self) -> None:
        print(f"{self.trademark} {self.model} freine.")
        self._speed = self._speed - 10 if self._speed >= 10 else 0

    def print_speed(self) -> None:
        print(f"{self._speed} km/h")


car = Vehicle("Toyota", "Corolla", 2020)

print(car)  # Affiche : Toyota Corolla (2020)
car.start()  # Affiche : Toyota Corolla démarre.
car.accelerate()  # Affiche : Toyota Corolla accélère.
car.print_speed()  # Affiche : 10 km/h
car.accelerate()  # Affiche : Toyota Corolla accélère.
car.print_speed()  # Affiche : 20 km/h
car.slow_down()  # Affiche : Toyota Corolla freine.
car.print_speed()  # Affiche : 10 km/h
