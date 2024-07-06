# III. Méthodes

## Sommaire

1. Méthodes d’Instance
2. Méthodes de Classe
3. Méthodes Statiques

## 1. Méthode d’Instance

Les méthodes d'instance sont des méthodes qui agissent sur les attributs d'une instance spécifique de la classe.
Elles prennent toujours `self` comme premier paramètre, qui fait référence à l'instance sur laquelle la méthode est
appelée.

> NOTE: `self` n'est pas un mot clef, mais une convention de nommage largement utilisée en Python.

Voici un exemple de définition d'une méthode d'instance `accelerate` dans la classe `Vehicle` :

```python
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
```

Nous pouvons appeler la méthode `accelerate` sur une instance de la classe `Vehicle` pour augmenter
la vitesse du véhicule :

```python
car = Vehicle("Toyota", "Corolla", 2020)
car.accelerate()
car.print_speed()  # Affiche : 10 km/h
```

## 2. Méthode de Classe

Les méthodes de classe sont des méthodes qui agissent sur la classe elle-même, plutôt que sur une instance spécifique.
Elles prennent `cls` comme premier paramètre, qui fait référence à la classe sur laquelle la méthode est appelée.
On utilise le décorateur `@classmethod` pour définir une méthode de classe.

Voici un exemple de définition d'une méthode de classe `from_string` dans la classe `Vehicle` :

```python
class Vehicle:
    def __init__(self, trademark: str, model: str, year: int):
        self.trademark = trademark
        self.model = model
        self.year = year
        self._speed = 0

    @classmethod
    def from_string(cls, vehicle_string: str):
        trademark, model, year = vehicle_string.split(",")
        return cls(trademark, model, int(year))
```

Nous pouvons appeler la méthode de classe `from_string` sur la classe `Vehicle` pour créer une instance
à partir d'une chaîne de caractères :

```python
car = Vehicle.from_string("Toyota,Corolla,2020")
print(car)  # Affiche : Toyota Corolla (2020)
```

Lorsqu'on définit une sous-classe, les méthodes de classe sont héritées par la sous-classe.

Voici un exemple de classe `Car` qui hérite de la classe `Vehicle` et ne redéfinit pas
la méthode de classe `from_string` :

```python
class Car(Vehicle):
    def honk(self) -> None:
        print("Pouet pouet")
```

Nous pouvons appeler la méthode de classe `from_string` sur la classe `Car` pour créer une instance
de la sous-classe `Car` à partir d'une chaîne de caractères :

```python
noisy_car = Car.from_string("Toyota,Corolla,2020")
noisy_car.honk()  # Affiche : Pouet pouet
```

## 3. Méthode Statique

Les méthodes statiques sont des méthodes qui n'agissent ni sur l'instance ni sur la classe.
Elles sont définies à l'intérieur de la classe, mais ne prennent ni `self` ni `cls` comme premier paramètre.
On utilise le décorateur `@staticmethod` pour définir une méthode statique.

Voici un exemple de définition d'une méthode statique `is_valid_year` dans la classe `Vehicle` :

```python
class Vehicle:
    def __init__(self, trademark: str, model: str, year: int):
        self.trademark = trademark
        self.model = model
        self.year = year
        self._speed = 0

    @staticmethod
    def is_valid_year(year: int) -> bool:
        return 1900 <= year <= 2024
```

Nous pouvons appeler la méthode statique `is_valid_year` sur la classe `Vehicle` sans instancier un objet :

```python
Vehicle.is_valid_year(2020)  # Retourne : True
Vehicle.is_valid_year(2025)  # Retourne : False
```

Nous pouvons aussi appeler une méthode statique sur une instance de la classe :

```python
car = Vehicle("Toyota", "Corolla", 2020)
car.is_valid_year(2020)  # Retourne : True
```

Les méthodes statiques sont souvent utilisées pour des fonctions utilitaires qui ne dépendent
pas de l'état de l'instance ou de la classe. Ces fonctions utilitaires seront hérités par les sous-classes.

> IMPORTANT ❗: Les méthodes statiques ne peuvent pas accéder aux attributs de l'instance ou de la classe.

> ✅ ASTUCE : il est souvent préférable d'utiliser une fonction normale à l'extérieur de la classe,
> car cela rend le code plus lisible, plus efficace et plus facile à tester.
