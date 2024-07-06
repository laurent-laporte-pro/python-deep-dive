# VII. Classes abstraites

## Sommaire

1. Définition d'une classe abstraite
2. Utilisation des classes abstraites en Python
3. Avantages et inconvénients des classes abstraites

## 1. Définition d'une classe abstraite

Une classe abstraite est une classe qui ne peut pas être instanciée directement,
c'est-à-dire qu'on ne peut pas créer d'objets à partir de cette classe.
Les classes abstraites sont utilisées comme des modèles pour définir des classes dérivées
qui implémentent des méthodes spécifiques.

En Python, les classes abstraites sont définies à l'aide du module `abc` (Abstract Base Classes).
Ce module fournit une classe de base `ABC` et un décorateur `abstractmethod` pour définir des méthodes abstraites.

Voici un exemple de définition d'une classe abstraite de véhicule avec une méthode abstraite `move` :

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self) -> None:
        pass
```

La classe `Vehicle` est une classe abstraite qui doit être dérivée pour implémenter la méthode `move`.

Si on tente d'instancier la classe `Vehicle`, une erreur sera levée :

```python
v = Vehicle()  # Lève une erreur TypeError
```

## 2. Utilisation des classes abstraites en Python

Pour utiliser une classe abstraite en Python, il est nécessaire de définir une classe dérivée qui implémente les
méthodes abstraites.

Voici un exemple de classe `Car` dérivée de la classe abstraite `Vehicle` :

```python
class Car(Vehicle):
    def move(self) -> None:
        print("La voiture se déplace sur la route.")


taxi = Car()
taxi.move()  # Affiche: La voiture se déplace sur la route.
```

## 3. Avantages et inconvénients des classes abstraites

Les classes abstraites permettent de définir des interfaces communes pour des classes dérivées,
ce qui facilite la conception et la maintenance du code.

Cependant, l'utilisation de classes abstraites peut rendre le code plus complexe et nécessiter une compréhension
plus approfondie de la hiérarchie des classes. Il est aussi plus difficile de déboguer des erreurs liées à l'utilisation
de classes abstraites, car elles sont plus difficiles à suivre.

Il est recommandé d'utiliser des classes abstraites lorsque plusieurs classes partagent des méthodes communes
qui doivent être implémentées de manière spécifique par chaque classe dérivée.

> IMPORTANT ❗: Afin d'éviter la sur-conception, il est recommandé de ne pas abuser des classes abstraites,
> en particulier s'il n'y a qu'une seule classe dérivée ou si les classes dérivées n'implémentent pas
> de méthodes abstraites spécifiques.

