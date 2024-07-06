# IV. Encapsulation

## Sommaire

1. Attributs et méthodes publics
2. Attributs et méthodes protégés
3. Attributs et méthodes privés
4. Utilisation des conventions pour l'encapsulation

## 1. Attributs et méthodes publics

En Python, on ne peut pas déclarer des attributs ou des méthodes comme étant privés ou protégés.
Tous les attributs et méthodes d'une classe sont publics par défaut, ce qui signifie qu'ils peuvent
être accessibles et modifiés à partir de n'importe où dans le code.

Voici une classe simple avec des attributs et des méthodes publics :

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Nom : {self.name}, Âge: {self.age}")


# Création d'un objet de la classe Person
p = Person("Alice", 30)

# Appel de la méthode display_info
p.display_info()
```

Dans cet exemple, les attributs `name` et `age` ainsi que la méthode `display_info` sont publics,
ce qui signifie qu'ils peuvent être utilisés à partir de l'extérieur de la classe.

Par exemple, on peut lire pou écrire directement les attributs `name` et `age` de l'objet `p` :

```python
print(p.name)  # Affiche: Alice
print(p.age)  # Affiche: 30

p.age += 1
p.display_info()  # Affiche: Name: Alice, Age: 31
```

En python, tout est publique. Par conséquent, il est possible d'ajouter ou de supprimer des attributs
ou des méthodes à un objet à tout moment.

```python
p.city = "Paris"
print(p.city)  # Affiche: Paris


def say_hello(this: Person) -> None:
    print(f"Bonjour, je m'appelle {this.name} et j'habit à {this.city}")


p.display_more_info = say_hello
p.display_more_info()  # Affiche : Bonjour, je m'appelle Alice et j'habite à Paris
```

> IMPORTANT ❗: En pratique, il est recommandé de ne pas ajouter ou modifier des attributs ou des méthodes
> à un objet en dehors de la classe, car cela peut rendre le code difficile à comprendre et à maintenir.

## 2. Attributs et méthodes protégés

En Python, il n'existe pas de véritable notion d'attributs ou de méthodes protégés comme dans d'autres langages
de programmation orientée objet.
Cependant, il est possible de simuler cette notion en utilisant une convention de nommage spécifique.

Les attributs ou méthodes protégés sont généralement nommés avec un préfixe `_` (un seul tiret bas),
ce qui indique qu'ils ne doivent pas être accédés directement à partir de l'extérieur de la classe.

Voici un exemple de classe avec des attributs et des méthodes protégés :

```python
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
```

En pratique, il est toujours possible d'accéder aux méthodes protégées, par exemple, on peut afficher le nom
de la personne en utilisant l'attribut `_name`, mais cela est déconseillé.

## 3. Attributs et méthodes privées

En python, il est aussi possible de simuler la notion d'attribut ou de méthode privée en utilisant le préfixe
`__` (deux tirets bas). Comme pour la convention sur les membres protégés, cette convention
signifie que les attributs et les méthodes ne doivent pas être accédées de l'extérieur de la classe.

Mais contrairement à la méthode précédente, l'interpréteur Python va _maquiller_ les noms des membres privés
afin de rendre l'accès beaucoup plus difficile.

Voici un exemple de classe avec des attributs et des méthodes privées :

```python
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
```

En pratique, il est toujours possible d'accéder aux méthodes privées, par exemple, on peut afficher le nom
de la personne en utilisant l'attribut `_Person__name`, mais cela est fortement déconseillé.

L'utilisation des méthodes privées est peu répendu et on préfèrera utiliser des méthodes protégées.
