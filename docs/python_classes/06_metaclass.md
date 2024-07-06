# VI. Métaclasse

## Sommaire

1. Définition d'une métaclasse
2. Utilisation de la méthode spéciale __new__
3. Exemples d'utilisation de métaclasse

## 1. Définition d'une métaclasse

Une métaclasse est une classe permettant d'instancier d'autres classes.
En d'autres termes, une métaclasse est une classe dont les instances sont des classes elles-mêmes.

En Python, les classes sont instanciées à partir de métaclass `type`.
Cependant, il est possible de définir des métaclasses personnalisées en définissant une classe qui hérite de `type`.

Exemple de définition d'une métaclasse personnalisée pour définir des classes de véhicules :

```python
class VehicleMeta(type):
    def __new__(cls, name, bases, cls_dict):
        cls_dict["category"] = "Transport"
        return super().__new__(cls, name, bases, cls_dict)
```

Dans cet exemple, la classe `VehicleMeta` est une métaclasse personnalisée qui ajoute un attribut `category` à toutes
les classes définies avec cette métaclasse.

Exemple d'utilisation de la métaclasse `VehicleMeta` pour définir une classe `Car` :

```python
class Car(metaclass=VehicleMeta):
    pass

print(Car.category)  # Affiche: Transport
```

