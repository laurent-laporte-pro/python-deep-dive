# Python Deep Dive

Plongez dans les méandres de Python et des bibliothèques standards.

## Mise en route

Ce projet utilise [hatch](https://hatch.pypa.io/latest/) pour gérer l'environnement de développement.

Cet outil en ligne de commande vous permettra de générer la documentation rapidement et de lancer les exemples de code.

➢ Pour générer la documentation, exécutez la commande suivante :

```shell
hatch run docs:build
```

Cette commande générera la documentation dans le répertoire `site`.

➢ Pour servir la documentation localement, exécutez la commande suivante :

```shell
hatch run docs:serve
```

Cette commande démarrera un serveur web local pour servir la documentation
à l'adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Pour lancer les exemples de code, exécutez la commande suivante :

