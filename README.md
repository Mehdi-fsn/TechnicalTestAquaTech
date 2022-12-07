# TestTechniqueAquaTech

Le test a été réalisé dans le cadre d'une candidature auprès de l'entreprise AquaTech. L'objectif étant de créer un générateur de données simulant des données de deux capteurs différents (capteur de niveau d'eau et de pression). Afin de pouvoir analyser ces données, il a fallu les afficher sous forme de graphique. Pour ce faire, j'ai dû créer un frontend et un backend afin de pouvoir récupérer celles-ci et les afficher.

## Les technologies 

#### Base de données - MySQL
> Le choix de la base de données a été fait selon 3 facteurs : la rapidité, la facilité d'utilisation et l'expérience. En effet, une base de données relationnelles n'est pas forcément nécessaire, mais les 3 critères mentionnés ci-dessus m'ont conduit à ce choix.

### Générateur - Python 
> Pour réaliser le générateur de données, j'ai retenu le langage python. Le plus gros facteur était que le langage devait pouvoir utiliser les générateurs afin de ne pas stocker les données entre le moment où elles sont générées et quand elles sont stockées dans la BDD (c'est le cas avec `yield`). De plus, grâce à sa facilité d'apprentissage, mon expérience avec ce langage ainsi que sa polyvalence m'ont conforté dans mon choix.

### BackEnd - Flask (SQLAlchemy)
> Le backend à suivi logiquement puisque j'ai voulu intégrer le générateur à celui-ci. Le fait que flask permet de créer des API claires et bien définies ainsi que sa documentation est bien fournie a été important. De plus, c'est un framework plutôt léger en lui-même avec un routing simplifié. J'ai choisi d'utiliser également l'ORM SQLAlchemy afin de sécuriser la base de données de toute intéraction éxterieure et potentiellement malicieuses.

### Frontend - VueJS
> Léger et minimaliste à la base, la possibilité d'ajouter soit même les outils nécessaires fait de lui un framework flexible pour chaque projet. Sa petite taille ne signifie pas une vitesse inférieure et sa documentation détaillée est un gros +. `Chartjs`, un module de création de graphique a fait également pencher la balance. Ayant déjà une expérience avec celui-ci, mais aussi dû au fait qu'il est un grand avenir devant lui, j'ai choisi de continuer à progresser sur celui-ci.

## Lancement du projet

Grâce à docker, une seule ligne de commande est nécessaire à l'installation du projet sous Linux : 

- Avec docker compose v2 => ```docker compose up```
- Avec docker compose v1 => ```docker-compose up```

> Docker v19.03.0 ou + est requis

Une fois les conteneurs lancés, dans votre navigateur tapé ```localhost:3080``` puis cliquer sur le bouton **Générer les données**.

## Explication du générateur 

Le générateur fonctionne grâce à un système de phase (diminution, stabilité et augmentation) aléatoire. Chaque phase dure entre 1 et 120 minutes aléatoirement. Entre chaque donnée, chaque minute, un step est défini aléatoirement dans une range propre à chaque capteur (0.0 - 1.0 pour le capteur de niveau d'eau et 0.00 - 0.01 pour le capteur de pression). Enfin, un système pour éviter le blocage plus de 120 minutes aux valeurs min et max de chaque capteur a été mis en place.

## Bonus 

Vous pouvez régénérer des données à votre convenance avec le bouton **Refresh**.

## Réalisé par 
- [@Mehdi-fsn](https://github.com/Mehdi-fsn)# Test Technique AquaTech
