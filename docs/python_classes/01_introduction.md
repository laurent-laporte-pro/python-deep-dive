# I. Introduction aux Classes

## Sommaire

1. Définition d'une classe
2. Création d'une classe
3. Instanciation d'objets à partir d'une classe
4. Utilité des classes en programmation

## 1. Définition d'une classe

Une classe est un modèle qui définit les attributs et les méthodes communs à un ensemble d'objets.
Elle permet de créer des objets (instances) qui partagent les mêmes caractéristiques et comportements.

Une class possède un nom, des attributs définissant ses caractéristiques et des méthodes définissant ses comportements.

Par exemple, une application gérant un parc de véhicules pourrait avoir une classe `Vehicle` avec des attributs
comme `trademark`, `modèle`, `année`, etc. et des méthodes comme `start`, `accelerate`, `slow_down`, etc.

## 2. Création d'une classe

En Python, la création d'une classe se fait à l'aide du mot-clé `class` suivi du nom de la classe.
Les attributs de la classe sont définis dans la méthode spéciale `__init__` qui est appelée lors de l'instanciation
d'un objet à partir de la classe.
Les méthodes sont définies comme des fonctions à l'intérieur de la classe.

Voici un exemple de définition d'une classe `Vehicle` en Python :

```python
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
```

## 3. Instanciation d'objets à partir d'une classe

Une fois la classe définie, on peut créer des objets (instances) à partir de cette classe en utilisant le nom de la
classe
comme une fonction.

Voici un exemple d'instanciation d'un objet `car` à partir de la classe `Vehicle` et d'appel de ses méthodes :

```python
car = Vehicle("Toyota", "Corolla", 2020)

print(car)  # Affiche : Toyota Corolla (2020)
car.start()  # Affiche : Toyota Corolla démarre.
car.accelerate()  # Affiche : Toyota Corolla accélère.
car.print_speed()  # Affiche : 10 km/h
car.accelerate()  # Affiche : Toyota Corolla accélère.
car.print_speed()  # Affiche : 20 km/h
car.slow_down()  # Affiche : Toyota Corolla freine.
car.print_speed()  # Affiche : 10 km/h
```

## 4. Utilité des classes en programmation

Les classes permettent de structurer le code en regroupant les données et les opérations associées dans un même objet.

Elles facilitent la réutilisation du code en permettant de créer de nouveaux objets à partir d'une classe existante.

Avec la composition et l'agrégation, elles permettent de modéliser des relations complexes entre les objets.

L'héritage est un moyen puissant de partager du code entre les classes et de créer des hiérarchies de classes.
