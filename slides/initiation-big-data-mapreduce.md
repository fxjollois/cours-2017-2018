---
title: Map-Reduce
subtitle: Initiation au Big Data
author: FX Jollois
---

## Présentation de MapReduce

- Framework développé par Google
- Permet l'écriture simple de programmes sur des clusters informatiques (possiblement très gros)
- Idée de base de la parallélisation des tâches : diviser pour régner
- 2 étapes donc :
	1. Etape 1 (**Map**) :
		- Diviser le travail à faire en plusieurs tâches 
		- Réaliser les tâches en parallèle 
	2. Etape 2 (**Reduce**) :
		- Récupérer les différents résultats
		- Regrouper ceux-ci pour obtenir le résultat final

## Paradigme de MapReduce

Le framework MapReduce est constitué de :

- un seul *JobTracker*, qui sera le chef d'orchestre :
	- programmation (*scheduling*) des jobs aux musiciens
	- gestion des défaillances de ceux-ci
- un *TaskTracker* par noeud du cluster, qui sera un musicien :
	- exécution des tâches demandés par le chef

Le travail se fait exclusivement sur des paires $<key, value>$

- Entrées : ensemble de paires $<key, value>$
- Sorties d'un job : paires $<key, value>$

## Schéma de MapReduce 

<img src="Mapreduce.png" style="margin: 0 auto;" width="673">

<div class="footnote">Source : <a href="http://commons.wikimedia.org/wiki/File:Mapreduce.png" target="_blank">http://commons.wikimedia.org/wiki/File:Mapreduce.png</a></div>

## Etapes Map et Reduce

Comme indiqué, cela s'articule autour de deux grandes étapes (**Map** et **Reduce**)  :

- Etape **Map** :
	- réalisé dans chaque noeud du cluster
	- souvent un seul des deux paramètres intéressant 
	- calcule une liste de couples $<key, value>$
- Etape **Reduce** :
	- traitement sur les valeurs ($value$) pour chaque $key$
	- travail possible en parallèle
	- tous les couples avec le même $key$ arrivent au même *worker*
	
## Exemple basique : comptage de mots

Deux fonctions à écrire : `map(key, value)` et `reduce(key, value)`

```{js}
map(string key, string value) {
	// key: document name
	// value: document contents
	for each word w in value 
		emit <w, 1>
}

reduce(string key, list value) {
	// key: word
	// value: list of each word appareance
	sum = 0
	for each v in value
		sum = sum + v
	emit <key, sum>
}
```

<div class="footnote">Ceci n'est pas un exemple littéral, mais une adaptation pour illustration</div>

## Exemple basique : comptage de mots

<img src="example-mapreduce-wordcount.png" width=100%>

<div class="footnote">Source : <a href="http://blog.trifork.com/wp-content/uploads/2009/08/" target="_blank">http://blog.trifork.com/wp-content/uploads/2009/08/</a></div>

## Algorithme plus détaillé de MapReduce

- Lecture des entrées dans le système de fichier distribué, découpages en blocs de taille identique, et assignation de chaque bloc à un *worker*
- Application de la fonction `map()` dans chaque *worker*
- Distribution des résultats de `map()` (étape **Shuffle**) en fonction des clés
- Application de la fonction `reduce()` (en parallèle ou non, selon les besoins)
- Ecriture de la sortie dans le système de fichier distribué (généralement)

## Caractéristiques 

- Modèle de programmation simple : 
	- deux fonctions à écrire (`map()` et `reduce()`)
	- indépendant du système de stockage
	- adaptatif à tout type de données
- Ajout possible d'une fonction `combine()` des résultats de `map()` pour les couples avec même clé
- Système gérant seul le découpage, l'allocation et l'exécution
- Tolérance aux défaillances (redémarrage de tâches, réaffectation)
- Parallélisation invisible à l'utilisateur

## Quelques critiques

- Pas de garantie d'être rapide : attention à l'étape *shuffle* qui peut prendre du temps, et qui n'est pas adaptable par l'utilisateur
- Coût de communication pouvant être important
- Pas adapté à des problèmes où les données peuvent tenir en mémoire ou à un petit cluster
- Pas de support de langage haut niveau, tel que SQL
- Est une réelle nouveauté ?
	- Proche d'autres implémentations, tel que *Clusterpoint* ou *MongoDB* 
	- Facilement applicable avec PL/SQL sous *Oracle*
- Pas optimisé au niveau des entres/sorties, et donc pas forcément adapté à un problème de *Machine Learning* dans lequel on doit régulièrement lire le même jeu de données plusieurs fois

## Implémentations

Toutes *open source* et *forkable* sur GitHub

- **Hadoop** [site web](http://hadoop.apache.org/)
	- Framework basé sur le système de fichiers distribués *HDFS*
- **CouchDB** [site web](http://couchdb.apache.org/)
	- BD *NoSQL*, basée sur JSON et JavaScript
- **InfiniSpan** [site web](http://infinispan.org/)
	- BD *NoSQL* 
- **MongoDB** [site web](http://www.mongodb.org/)
	- BD *NoSQL*, basée sur JSON et JavaScript
- **Riak** [site web](http://basho.com/riak/)
	- BD *NoSQL* 
	
## D'autres voies encore 

- **Spark** [lien](http://spark.apache.org)
	- projet Apache
	- Framework pour le calcul sur cluster informatique
- **Distributed R** [lien](https://github.com/vertica/DistributedR)
	- projet GitHub, mais développé par HP Vertica
	- extension permettant de réaliser des programmes bénéficiant de la parallélisation
- **BID Data Project** [lien](http://bid2.berkeley.edu/bid-data-project/)
	- projet issu de Berkely, et sur GitHub
	- dédié Machine Learning
- sous **Python** [lien](https://wiki.python.org/moin/ParallelProcessing)
	- existence de plusieurs librairies permettant le travail sur plusieurs processeurs
- **Flink** [lien](http://flink.incubator.apache.org/)
	- projet Apache en incubation
- **H2O** [lien](http://0xdata.com/h2o/)
	- disponible sous GitHub, développé par 0xdata
	- dédié Machine Learning, et interfaçable avec R
