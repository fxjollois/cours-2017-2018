---
title: Introduction à MongoDB
---

Dans cette introduction, nous allons aborder l'utilisation de MongoDB, via l'interrogation de données dans le `shell`. MongoDB utilise le langage `JavaScript`.

## MongoDB

*MongoDB* est une base de données NoSQL distribué de type *Document Store* ([site web](http://www.mongodb.com/))

Objectifs :

- Gérer de gros volumes
- Facilité de déploiement et d'utilisation
- Possibilité de faire des choses complexes tout de même

### Modèle des données

Principe de base : les données sont des `documents`

- stocké en *Binary JSON* (`BSON`)
- documents similaires rassemblés dans des `collections`
- pas de schéma des documents définis en amont
	- contrairement à un BD relationnel ou NoSQL de type *Column Store*
- les documents peuvent n'avoir aucun point commun entre eux
- un document contient (généralement) l'ensemble des informations
	- pas (ou très peu) de jointure à faire
- BD respectant **CP** (dans le théorème *CAP*)
	- propriétés ACID au niveau d'un document


### Point sur `JSON`

- `JavaScript Object Notation`
- Créé en 2005
- On parle de **littéral**
- Format d'échange de données structurées léger
- Schéma des données non connu
    - contenu dans les données
- Basé sur deux notions :
	- collection de couples clé/valeur
	- liste de valeurs ordonnées
- Structures possibles :
	- objet (couples clé/valeur) :
	   - `{}`
	   - `{ "nom": "jollois", "prenom": "fx" }`
	- tableau (collection de valeurs) :
	   - `[]`
	   - `[ 1, 5, 10]`
	- une valeur dans un objet ou dans un tableau peut être elle-même un littéral
- Deux types atomiques (`string` et `number`) et trois constantes (`true`, `false`, `null`)

Validation possible du JSON sur [jsonlint.com/](http://jsonlint.com/)

```json
{
	"tubd": {
		"formation": "DU Analyste Big Data",
		"responsable": { "nom": "Poggi", "prenom": "JM" },
		"etudiants" : [
			{ "id": 1, "nom": "jollois", "prenom": "fx" },
			{ "id": 2, "nom": "aristote", "details": "délégué" },
			{ "id": 5, "nom": "platon" }
		],
		"ouverte": true
	},
	"tudv": {
		"formation": "DU Data Visualisation",
		"ouverte": false,
		"todo": [
			"Creation de la maquette",
			"Validation par le conseil"
			],
		"responsable": { "nom": "Métivier" }
	}
}
```

### Compléments

`BSON` : extension de `JSON`

- Quelques types supplémentaires (identifiant spécifique, binaire, date, ...)
- Distinction entier et réel

**Schéma dynamique**

- Documents variant très fortement entre eux, même dans une même collection
- On parle de **self-describing documents**
- Ajout très facile d'un nouvel élément pour un document, même si cet élément est inexistant pour les autres
- Pas de `ALTER TABLE` ou de redesign de la base

**Pas de jointures entre les collections**


### Langage d'interrogation

- Pas de SQL (bien évidemment), ni de langage proche
- Définition d'un langage propre (basé sur `JS`)
- Langage permettant plus que les accès aux données
	- définition de variables
	- boucles
	- ...

## Connection au serveur distant

Pour pouvoir accéder au `shell` de Mongo, il faut se connecter en *SSH* au serveur distant. Voici la commande à réaliser dans un terminal de commande. Le `login` est à remplacer par le vôtre, fourni en début de cours.

```sh
ssh login@193.51.82.104 -p2342
```

## Accès à MongoDB

Pour lancer le `shell` de Mongo, il suffit d'exécuter la commande suivante dans le terminal de commande.

```sh
mongo
```

Vous devriez voir apparaître des avertissements diverses. Il ne faut pas en tenir compte.

Une fois connecté au `shell`, il est possible de connaître l'ensemble des bases de données présentes sur le serveur. Pour ceci, vous devez utiliser la commande `show dbs` comme ci-dessous.

```js
show dbs
```

Pour choisir la base sur laquelle vous voulez travailler, il faut la sélectionner à l'aide de la commande `use db` (`db` étant à remplacé par le nom de la base de données choisie - ici `test`).

```js
use test
```

Une base de données est constitué d'une ou plusieurs collections. Chacune de celles-ci contient un ensemble de documents. Pour lister celles-ci, on utilise la commande `show collections`.

```js
show collections
```

Vous devriez avoir une liste à deux éléments : `restaurants` et `test`.

Dans MongoDB, comme nous le verrons par la suite, nous utilisons un formalisme de type `db.collection.fonction()` :

- `db` représente la base de données choisie grâce à la commande `use` (ce mot clé est non modifiable)
- `collection` représente la colletion dans laquelle nous allons effectuer l'opération, et doit donc correspondre à une des collections présentes dans la base
- `fonction()` détermine l'opération à effectuer sur la collection.

En premier lieu, on peut dénombrer le nombre de documents de chaque collection, grâce à la fonction `count()`.

```js
db.restaurants.count()
```

Les documents présents dans une collection n'ont pas de schémas prédéfinis. Si nous souhaitons avoir une idée de ce que contient la collection, il est possible d'afficher un document (le premier trouvé), avec `findOne()`. Cette opération permet de comprendre la structure global d'un document, même s'il peut y avoir des différences entre documents.

```js
db.restaurants.findOne()
```

Il est possible d'inclure des critères de sélection dans cette fonction, que nous verrons dans la suite. De même pour la sélection des items à afficher.

Une autre fonction très utile pour mieux appréhender les données est de lister les valeurs prises par les différents items de la collection, grâce à `distinct()`. Pour spécifier un sous-item d'un item, il est nécessaire d'utiliser le formalisme `item.sousitem`.  

```js
db.restaurants.distinct("borough")
db.restaurants.distinct("cuisine")
db.restaurants.distinct("address.zipcode")
db.restaurants.distinct("grades.grade")
```

## Recherche d'informations

Pour faire des recherches, il existe la fonction `find()`. Sans paramètre, elle renvoie l'ensemble des documents. Il faut donc l'utiliser avec précautions. Mais celle-ci peut aussi prendre deux paramètres :

- les critères de sélection des documents
- les choix d'items des documents à afficher

Ces deux paramètres doivent être écrits sous la forme d'objets `JSON`.

### Restriction

Dans ce premier exemple, on cherche le restaurant s'appelant `"La Grenouille"`.

```js
db.restaurants.find({ name: "La Grenouille" })
```

L'affichage rendu par `find()` est compact et peu lisible directement. On peut *aérer* ce rendu en ajoutant la fonction `pretty()` pour avoir une présentation propre.

```js
db.restaurants.find({ name: "La Grenouille" }).pretty()
```

### Projection

Si l'on désire n'afficher que certains éléments, il est possible d'ajouter un deuxième argument spécifiant les items que l'on veut (avec `1`) ou qu'on ne veut pas (avec `0`).

```js
db.restaurants.find({ cuisine: "French" }, { name: 1 })
```

Par défaut, l'identifiant du document, toujours nommé `_id`, est renvoyé. Pour ne pas l'avoir, il faut ainsi le préciser avec `"_id": 0`.

```js
db.restaurants.find({ cuisine: "French" }, { _id: 0, name: 1 })
```

### Sous-item

Les documents peuvent être complexes (c'est même le but), et les critères portent donc souvent sur des sous-items. Il faut utiliser le même formalisme déjà vu (`"item.sousitem"`). Il faut noter deux choses :
- on peut aller aussi loin que nécessaire dans l'utilisation du `.` ;
- il est obligatoire d'utiliser des '""' pour les items.

```js
db.restaurants.find({ "grades.grade" : "A" }, { _id: 0, name: 1 })
```

Ce formalisme est le même pour indiquer un sous-item à afficher. Nous ajoutons à la requête précédent l'affichage des scores. Nous voyons que le résultat inclu tous les scores.

```js
db.restaurants.find({ "grades.grade" : "A" }, { _id: 0, name: 1, "grades.grade" : 1 })
```

### Comparaison autre que l'égalité

Le test d'égalité est aussi réalisable avec une variable numérique.

```js
db.restaurants.find({ "grades.score": 90 }, { _id: 0, name: 1 })
```

Pour les comparaisons, nous disposons des opérateurs `$eq`(*equal*), `$gt` (*greater than*), `$gte` (*greater than or equal*), `$lt` (*less than*), `$lte` (*less than or equal*) et `$ne` (*not equal*). 

```js
db.restaurants.find({ "grades.score": { $gte: 90 } }, { _id: 0, name: 1 })
```

En plus de ces comparaisons simples, nous disposons d'opérateurs de comparaisons à une liste : `$in` (présent dans la liste) et `$nin` (non présent dans la liste).

```js
db.restaurants.find({ "grades.score": { $in: [ 90, 98 ] } }, { _id: 0, name: 1 })
```

Par défaut, si on ajoute des critères de restriction dans le premier paramètre, la recherche se fait avec un *ET* entre les critères. 

```js
db.restaurants.find({ "grades.grade" : "A", cuisine : "French" }, { _id: 0, name: 1 })
```

Mais si on veut faire des combinaisons autres, il existe des opérateurs logiques : `$and`, `$or` et `$nor`. Ces trois opérations prennent un tableau de critères comme valeur. 

```js
db.restaurants.find({ "$or": [ { "grades.grade" : "Z" }, { cuisine : "French" } ] },
                    { _id: 0, name: 1, cuisine: 1, "grades.grade": 1 })
```

### Présence d'un item

Comme précédemment indiqué, il est courant qu'un document ne contienne pas tous les items possibles. Si l'on cherche à tester la présence ou non d'un item, on utilise l'opérateur `$exists` (avec `true` si on teste la présence, et `false` l'absence). 

```js
db.restaurants.find({ french : { "$exists" : true } }, { _id: 0, name: 1 })
```

### Dénombrement

Il est souvent nécessaire de faire des dénombrements suite à des sélections, pour faire des vérifications de code ou des estimations de charge (ou autre). La fonction `count()` peut ainsi s'ajouter à la suite d'une fonction `find()` pour connaître la taille du résultat. 

```js
db.restaurants.find({ cuisine : "French" }).count()
```

### Limitation du résultat

On peut aussi limiter le nombre de documents renvoyés par la fonction `find()` en lui ajoutant la fonction `limit()`, comme ici où nous nous restreignons aux 5 premiers résultats.

```js
db.restaurants.find({ cuisine : "French" }, { _id: 0, name: 1 }).limit(5)
```

### Tri

Une autre opération classique est le tri des résultats, réalisable avec la fonction `sort()`. On doit indiquer les items de tri et leur attribuer une valeur de `1` pour un tri ascendant et une valeur de `-1` pour un tri descendant. 

```js
db.restaurants.find({ cuisine : "French" }, { _id: 0, name: 1 }).sort({ name: 1 })
```

Idem que précédemment, mais dans l'ordre décroissant.

```js
db.restaurants.find({ cuisine : "French" }, { _id: 0, name: 1 }).sort({ name: -1 })
```

Bien évidemment, il est possible de mettre plusieurs critères de tri, en indiquant croissant ou décroissant pour chaque item de tri.

```js
db.restaurants.find({ cuisine : "French" }, { _id: 0, name: 1, borough: 1 }).sort({ borough: -1, name: 1 })
```

Enfin, il est possible d'écrire les commandes sur plusieurs lignes, avec des indentations, afin de rendre les commandes plus lisibles, tel que ci-dessous.

```js
db.restaurants.find(
    { cuisine : "French" }, 
    { _id: 0, name: 1, borough: 1 }
).sort(
    { borough: -1, name: 1 }
)
```

## Agrégats

En plus des recherches classiques d'informations, le calcul d'agrégat est très utilisé, pour l'analyse, la modélisation ou la visualisation de données. Ce calcul s'effectue avec la fonction `aggregate()`. Celle-ci prend en paramètre un tableau d'opérations (appelé aussi `pipeline`), pouvant contenir les éléments suivants  :

- `$project` : redéfinition des documents (si nécessaire)
- `$match` : restriction sur les documents à utiliser
- `$group` : regroupements et calculs à effectuer
- `$sort` : tri sur les agrégats
- `$unwind` : découpage de tableaux
- ...

### Agrégat simple

Voici un premier exemple permettant un calcul pour toute la base. Ici, nous réalisons un dénombrement (il fait la somme de la valeur 1 pour chaque document).

```js
db.restaurants.aggregate([
    { $group: { _id: null, nb: { $sum: 1 }}}
])
```

Les calculs peuvent être plus complexes, comme nous le verrons plus tard. Bien évidemment, ces calculs d'agrégats peuvent se faire aussi en ajoutant des critères de regroupement. *Attention* au `$` avant le nom de l'item.

```js
db.restaurants.aggregate([
    { $group: { _id: "$borough", nb: { $sum: 1 }}}
])
```

### Tri

Ce résultat peut être trié en ajoutant l'action `$sort` dans le tableau, avec le même mécanismes que précédemment (1 : ascendant, -1 : descendant).

```js
db.restaurants.aggregate([
    { $group: { _id: "$borough", nb: { $sum: 1 }}},
    { $sort: { "nb": -1 }}
])
```

### Redéfinition des documents (et limite)

Il est parfois intéressant (voire nécessaire) de redéfinir les documents, pour ne garder que les items qui nous intéressent. Dans cette projection, il existe différentes fonctions de traitement comme la concaténation (cf ci-dessous).

L'action `$limit` permet de limiter le nombre de sorties renvoyées par le moteur.

```js
db.restaurants.aggregate([
    { $project: { _id: 0, name: 1, info: { $concat: [ "$cuisine", " - ", "$borough" ]} }},
    { $limit: 5 }
]).pretty()
```

### Restriction

On peut aussi faire une restriction avant le calcul, avec l'opération `$match`. 

```js
db.restaurants.aggregate([
    { $match: { cuisine: "French" }},
    { $group: { _id: "$borough", nb: { $sum: 1 }}}
])
```

### Découpage des tableaux

Imaginons maintenant que nous souhaitons calculer le nombre de restaurant par *grade*. La première idée serait de réaliser l'opération suivante.

```js
db.restaurants.aggregate([
    { $group: { _id: "$grades.grade", nb: { $sum: 1 }}}
])
```

Malheureusement, nous voyons que le regroupement se fait par ensemble de grades existant dans la base. Il faut donc faire un découpage des tableaux `grades` dans chaque document. Pour cela, il existe l'opération `$unwind`.

Pour montrer comment fonctionne cette opération, voici les 5 premières lignes renvoyées lorsqu'on l'applique directement sur les données. On s'apercoit que chaque document ne contient plus qu'une seule évaluation.

```js
db.restaurants.aggregate([
    { $unwind: "$grades" },
    { $limit: 5 }
]).pretty()
```

Par ce biais, nous pouvons donc maintenant faire l'opération de regroupement par grade.

```js
db.restaurants.aggregate([
    { $unwind: "$grades" },
    { $group: { _id: "$grades.grade", nb: { $sum: 1 }}} 
])
```

### Calcul statistique

Comme indiqué précédemment, on peut faire tous les calculs d'agrégats classiques, comme ici avec la somme (`$sum`), la moyenne (`$avg`), le minimum (`$min`) et le maximum (`$max`).

```js
db.restaurants.aggregate([
    { $unwind: "$grades" },
    { $group: {
        _id: null,
        nb: { $sum: 1 },
        scoreTot: { $sum: "$grades.score" },
        scoreMoy: { $avg: "$grades.score" },
        scoreMin: { $min: "$grades.score" },
        scoreMax: { $max: "$grades.score" }
    }}
]).pretty()
```

### Regroupement de valeurs

Une fois que les documents sont scindés en plusieurs suite à l'action `$unwind`, il peut être intéressant de regrouper les valeurs dans un tableau. Ici, nous cherchons les différents grades obtenus par chaque restaurant.

```js
db.restaurants.aggregate([
    { $limit: 5 },
    { $unwind: "$grades" },
    { $group: { _id: "$name", nb: { $sum: 1 }, eval: { $addToSet: "$grades.grade" }}} 
])
```


## A faire

Il existe de nombreuses autres opérateurs disponibles dans Mongo. [L'aide en ligne](https://docs.mongodb.com/manual/reference/operator/) est assez bien fournie en exemple et la communauté est grandissante, permettant d'avoir aussi un grand nombre de réponses sur des forums comme [Stack Overflow](https://stackoverflow.com/).

Répondre aux questions suivantes

### Recherche

1. Lister les informations du restaurant "Cafe Henri"
1. Lister les restaurants n'ayant pas de quartier connu ("Missing")
1. Lister les restaurants ayant eu un score de 0
1. Lister les restaurants ayant eu un score entre 0 et 10 (inclus)
1. Lister les restaurants qui ont le terme "Cafe" dans leur nom
1. Lister les restaurants faisant de la cuisine de type "Pizza" dans "Brooklyn"


### Agrégat

1. Quelles sont les 10 plus grandes chaines de restaurants (nom identique) ?
1. Donner le Top 5 et le Flop 5 des types de cuisine, en terme de nombre de restaurants
1. Donner les dates de début et de fin des évaluations
1. Quels sont les 10 restaurants (nom, quartier, addresse et score) avec le plus grand score moyen ?
1. Quels sont les restaurants (nom, quartier et addresse) avec uniquement des grades "A" ?
1. Compter le nombre d'évaluation par jour de la semaine
