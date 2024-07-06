# V. Héritage

## Sommaire

1. Héritage simple
2. Héritage multiple
3. Ordre de résolution des méthodes (MRO)

## 1. Héritage simple

L'héritage est un concept fondamental en programmation orientée objet qui permet de créer de nouvelles classes
en réutilisant les attributs et les méthodes d'une classe existante. La classe existante est appelée la classe
de base ou la classe parente, tandis que la nouvelle classe est appelée la classe dérivée ou la classe enfant.

Lorsqu'une classe hérite d'une seule classe parente, on parle d'héritage simple.

Voici un exemple de classe `Car` qui hérite de la classe `Vehicle` :

```python
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
```

La classe fille hérite des membres de la classe mère et peut aussi surcharger les méthodes de la classe de base
pour ajouter des comportements spécifiques.

## 2. Héritage multiple

En Python, il est possible de mettre en œuvre l'héritage multiple : une classe fille peut hériter de plusieurs
classes parentes.

# TODO: terminer le paragraphe