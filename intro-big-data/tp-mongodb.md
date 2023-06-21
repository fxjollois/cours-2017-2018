---
title: TP MongoDB
---

Vous devez rendre ce TP pour mardi 12 juin, à 18h, en l'envoyant par mail à 

    francois - xavier . jollois [@] parisdescartes . fr

Merci de mettre vos réponses dans le mail, avec le formalisme suivant :

```js
## Question à laquelle vous répondez
db.collection.fonction()
```

## Horodateurs parisien

Nous allons découvrir dans ce TP les [données utilisées](https://opendata.paris.fr/explore/dataset/horodateurs-transactions-de-paiement/) dans le projet à rendre, qui sont l'ensemble des **transactions sur les horodateurs** dans la ville de **Paris** sur l'année **2014**. Celles-ci proviennent du site [Open Data Paris](https://opendata.paris.fr/), répertoire des données ouvertes de la ville de Paris. Elles sont stockées sur le serveur MongoDB déjà utilisé, dans la base horodateurs.

Elle contient trois collections importantes :

- `transactions` : ensemble des paiements
- `transactions_small` : 1% des paiements
- `mobiliers` : liste de tous les horodateurs

## A faire

### Mobiliers

1. Donner le nombre de mobiliers
1. Donners les informations du mobilier `1234` (cf `objectid`)
1. Lister l'ensemble des tarifs horaires existants (`modele`)
1. Lister l'ensemble des modèles existants (`modele`)
1. Donner le nombre de mobiliers pour chaque arrondissement (`arrondt`)
1. Croiser le régime (`regime`) et les arrondissements pour voir s'il y a des différences notables
1. Donner par arrondissements la liste des  régimes des mobiliers

### Transactions

1. Donner la distribution des montants payés (montant carte) et des durées payées (durée payée (h))
1. Lister les différents moyens de paiements utilisés (moyen de paiement) et le type d'usager (usager), en ordonnant chaque table résultat par ordre décroissant du nombre de paiements
1. Déterminer s'il existe un lien entre le moyen de paiement, et le montant d'une part et la durée d'autre part

## Jointure

Il est possible de réaliser une jointure entre deux collections, dans un aggrégat, avec l'opérateur `$lookup`.

Ci-dessous, nous nous restreignons aux transactions de l'horodateur `57080603`, pour simplifier le travail. Ensuite, nous récupérons les informations de celui-ci dans l'autre collection (indiquée dans le `from`), via la jointure avec `$lookup`. L'attribut `localField` indique l'attribut à prendre dans la collection en cours et `foreignField` l'attribut à prendre dans la collection indiquée dans le `from`. La liste des mobiliers correspondants (1 seul normalement ici) est retournée dans un `array` nommé via le `as`. Ensuite, nous nous limitons aux 5 premiers résultats pour ne pas alourdir l'affichage.

```js
db.transactions_small.aggregate([
    { $match: { "horodateur": 57080603}},
    { $lookup: {
        from: "mobiliers",
        localField: "horodateur",
        foreignField: "fields.numhoro",
        as: "mobilier"
    }},
    { $limit: 5}
])
```

1. Calculer le nombre de transactions par arrondissement
1. Calculer la répartition du type d'alimentation par arrondissement