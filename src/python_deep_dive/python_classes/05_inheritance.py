class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Nom : {self.name}, Âge : {self.age}"


class Employee(Person):
    def __init__(self, name: str, age: int, team: str):
        super().__init__(name, age)
        self.team = team

    def __str__(self) -> str:
        info = super().__str__()
        return f"{info}, Équipe : {self.team}"


paul = Employee("Paul", 45, "HR")
print(paul)  # Affiche : Nom : Paul, Âge : 45, Équipe : HR

print(isinstance(paul, Person))  # Affiche : True
print(isinstance(paul, Employee))  # Affiche : True


class S
