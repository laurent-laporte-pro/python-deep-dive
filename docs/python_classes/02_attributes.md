# II. Attributs

## Sommaire

1. Définition et utilisation des attributs d'instance
2. Définition et utilisation des attributs de classe
3. Différences entre les deux types d'attributs
4. Utilisation des propriétés

## 1. Définition et utilisation des attributs d'instance

Les attributs d'instance sont des attributs qui sont propres à chaque instance d'une classe.
Ces attributs définissent l'état interne de chaque objet et peuvent varier d'une instance à l'autre.
Ils sont définis à l'intérieur de la méthode `__init__` de la classe et sont accessibles via `self`.

Voici un exemple de définition d'attributs d'instance `trademark`, `model` et `year` dans une classe `Vehicle` :

```python
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
```

Nous pouvons instancier plusieurs objets qui auront des valeurs différentes pour ces attributs d'instance.
Chaque objet aura son propre état interne et pourra exécuter des méthodes qui agiront sur cet état.

```python
car1 = Vehicle("Toyota", "Corolla", 2020)
car2 = Vehicle("Honda", "Civic", 2019)
car1.run(100)
car2.run(150)
car2.run(270)

print(car1.mileage)  # Affiche : 100
print(car2.mileage)  # Affiche : 420
```

## 2. Définition et utilisation des attributs de classe

Les attributs de classe sont des attributs qui sont partagés par toutes les instances d'une classe.
Ils sont définis à l'intérieur de la classe, mais à l'extérieur des méthodes, en dehors de la méthode `__init__`.

Voici un exemple de définition d'un attribut de classe `count` dans une classe `RegisteredVehicle` :

```python
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
```

À chaque fois qu'une nouvelle instance de la classe `RegisteredVehicle` est créée,
l'attribut de classe `count` est incrémenté de 1.

Cet attribut est accessible à la fois par la classe et par les instances de la classe :

```python
car1 = RegisteredVehicle("Toyota", "Corolla", 2020)
car2 = RegisteredVehicle("Renault", "Clio", 2018)
car3 = RegisteredVehicle("Peugeot", "208", 2019)
car3.reset_count(880)

print(RegisteredVehicle.count)  # Affiche : 3
print(car1.count)  # Affiche : 3
print(car2.count)  # Affiche : 3
print(car3.count)  # Affiche : 880
print(car1.plate)  # Affiche : TOY-COR-2020-001
```

## 3. Différences entre les deux types d'attributs

Les attributs d'instance sont **propres à chaque instance** de la classe et peuvent varier d'une instance à l'autre.
Ils sont définis à l'intérieur de la méthode `__init__` et sont accessibles via `self`.

Les attributs de classe sont généralement utilisés pour stocker des informations **partagées par toutes les instances**
de la classe. En pratique, on utilise les attributs de classe pour stocker des constantes ou des valeurs par défaut.

Un attribut de classe peut être surchargé par une instance, mais cela ne modifie pas la valeur de l'attribut de classe.

## 4. Utilisation des propriétés

Les propriétés sont des attributs qui permettent de contrôler l'accès en lecture et en écriture à des données d'une
classe.
Elles sont définies à l'aide des décorateurs `@property`, `@attribut.setter` et `@attribut.deleter`.

> REMARQUE : La suppression d'attributs avec `@attribut.deleter` est rarement utilisée en pratique.

Voici un exemple de définition d'une propriété `mileage` dans la classe `Vehicle2` :

```python
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
```

Dans cet exemple, la propriété `mileage` permet de contrôler l'accès en lecture et en écriture à l'attribut `_mileage`.

```python
car = Vehicle2("Toyota", "Corolla", 2020)
print(car.mileage)  # Affiche : 0
car.mileage = 100
print(car.mileage)  # Affiche : 100
car.mileage = -50  # Lève une exception ValueError
```
