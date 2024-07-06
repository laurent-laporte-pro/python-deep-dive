class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Création d'un objet de la classe Person
p = Person("Alice", 30)

# Appel de la méthode display_info
p.display_info()

print(p.name)  # Affiche: Alice
print(p.age)  # Affiche: 30

p.age += 1
p.display_info()  # Affiche : Name: Alice, Age: 31


class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def _get_info(self) -> str:
        return f"Nom : {self._name}, Âge : {self._age}"

    def display_info(self) -> None:
        print(self._get_info())


p = Person("Juliette", 16)
p.display_info()

print(f"{p._name=}")  # Affiche : p._name='Juliette'


class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def __get_info(self) -> str:
        return f"Nom : {self.__name}, Âge : {self.__age}"

    def display_info(self) -> None:
        print(self.__get_info())


p = Person("Charles", 16)
p.display_info()

print(f"{p._Person__name=}")  # Affiche : p._Person__name='Charles'
