# VIII. Classes de données (Dataclasses)

## Sommaire

1. Introduction aux Dataclasses
2. Création et utilisation de Dataclasses
3. Avantages des Dataclasses par rapport aux classes traditionnelles
4. Les tuples nommés (Named Tuples)
5. Alternatives open-source : pydantic, attrs…

## 1. Introduction aux Dataclasses

Les Dataclasses sont une fonctionnalité introduite dans Python 3.7 pour simplifier la création de classes de données.
Elles permettent de définir des classes avec des attributs de données sans avoir à écrire des méthodes spéciales
comme `__init__`, `__repr__`, `__eq__`, etc.

Les Dataclasses sont similaires aux Named Tuples, mais offrent plus de flexibilité et de fonctionnalités.

## 2. Création et utilisation de Dataclasses

Pour créer une Dataclass, on utilise le décorateur `@dataclass` fourni par le module `dataclasses`.

Voici un exemple de définition d'une Dataclass `Camion` avec des attributs `marque`, `modèle` et `année` :

```python
from dataclasses import dataclass

@dataclass
class Camion:
    marque: str
    modèle: str
    année: int
```

Nous pouvons maintenant créer des instances de la classe `Camion` sans avoir à définir explicitement les
méthodes `__init__`, `__repr__`, etc.

```python
camion1 = Camion("Volvo", "FH16", 2021)
camion2 = Camion("Scania", "R730", 2020)

print(camion1)  # Affiche: Camion(marque='Volvo', modèle='FH16', année=2021)
print(camion2)  # Affiche: Camion(marque='Scania', modèle='R730', année=2020)
```

## 3. Avantages des Dataclasses par rapport aux classes traditionnelles

Les Dataclasses offrent plusieurs avantages par rapport aux classes traditionnelles :

- **Moins de code** : l'implémentation des méthodes spéciales comme `__init__`, `__repr__`, `__eq__`, etc., est
  automatique.
- **Lisibilité** : les Dataclasses sont plus faciles à lire et à comprendre.
- **Immutabilité** : les Dataclasses peuvent être rendues immuables en utilisant le
  décorateur `@dataclass(frozen=True)`.
- **Comparaison** : les Dataclasses prennent en charge la comparaison entre instances avec les opérateurs de
  comparaison (`==`, `!=`, etc.).

> ATTENTION : La conversion et la validation des données ne sont pas gérées par les Dataclasses.
> Il est recommandé d'utiliser des bibliothèques comme `pydantic` ou `attrs` pour ces fonctionnalités.

Voici comment il est néanmoins possible de définir une méthode de validation dans une Dataclass :

```python
import sys
from dataclasses import dataclass


def validate_year(year: int) -> int:
    if not 1900 <= year <= 2024:
        raise ValueError("L'année doit être comprise entre 1900 et 2024.")
    return year


@dataclass
class Vehicle:
    marque: str
    modèle: str
    année: int

    def __post_init__(self):
        self.année = validate_year(self.année)


# L'année 2020 est valide
véhicule = Vehicle("Toyota", "Corolla", 2020)

try:
    # L'année 2025 est invalide
    véhicule = Vehicle("Toyota", "Corolla", 2025)  # Lève une ValueError
except ValueError as e:
    print(e, file=sys.stderr)
else:
    print("L'année est valide.")
```

## 4. Les tuples nommés (Named Tuples)

Les Named Tuples sont une autre façon de définir des classes de données en Python.
Elles sont similaires aux Dataclasses, mais se comportent comme des tuples immuables avec des noms d'attributs.

Pour définir une Named Tuple, on utilise la fonction `namedtuple` du module `collections`.

Voici un exemple de définition d'une Named Tuple `GPS` avec des attributs `latitude` et `longitude` :

```python
from collections import namedtuple

GPS = namedtuple("GPS", ["latitude", "longitude"])

gps1 = GPS(48.8566, 2.3522)
gps2 = GPS(37.7749, -122.4194)
```

Avec le module `typing`, il est maintenant plus simple et claif de définir des Named Tuples :

```python
import typing as t

class GPS(t.NamedTuple):
    latitude: float
    longitude: float

gps1 = GPS(48.8566, 2.3522)
gps2 = GPS(37.7749, -122.4194)
```

> ATTENTION : Comme pour les Dataclasses, les Named Tuples ne gèrent pas la conversion et la validation des données.

Voici comment il est possible de définir une méthode de validation dans une Named Tuple :

```python
import sys
import typing as t

class _GPS(t.NamedTuple):
    latitude: float
    longitude: float


class GPS(_GPS):
    def __new__(cls, latitude: float, longitude: float):
        if not -90 <= latitude <= 90:
            raise ValueError("La latitude doit être comprise entre -90 et 90.")
        if not -180 <= longitude <= 180:
            raise ValueError("La longitude doit être comprise entre -180 et 180.")
        return super().__new__(cls, latitude, longitude)


# Les coordonnées de Paris sont valides
gps1 = GPS(48.8566, 2.3522)

try:
    gps2 = GPS(91, 2.3522)  # Lève une ValueError
except ValueError as e:
    print(e, file=sys.stderr)
else:
    print("Les coordonnées sont valides.")
```

## 5. Alternatives open-source : pydantic, attrs…

En plus des Dataclasses et des Named Tuples, il existe d'autres bibliothèques open-source pour la définition de classes
de données en Python :

- **pydantic** : une bibliothèque de validation de données et de conversion de types.
- **attrs** : une bibliothèque pour la définition de classes Python sans répétition de code.

Exemple d'implémentation d'une classe de données avec `pydantic` :

```python
from pydantic import BaseModel

class Camion(BaseModel):
    marque: str
    modèle: str
    année: int
```

Exemple d'implémentation d'une classe de données avec `attrs` :

```python
import attr

@attr.s
class Camion:
    marque: str = attr.ib()
    modèle: str = attr.ib()
    année: int = attr.ib()
```

Avantages de `pydantic` et `attrs` :

- **Validation des données** : ces bibliothèques permettent de valider et de convertir les données en fonction des types
  définis.
- **Conversion des types** : elles offrent des fonctionnalités avancées pour la conversion des types de données.
- **Personnalisation** : elles permettent de personnaliser le comportement des classes de données en fonction des
  besoins.
- **Interopérabilité** : elles sont compatibles avec d'autres bibliothèques et frameworks Python.
