# ACP ou AFC ?

Nous allons voir ici l'application de l'**ACP** et de l'**AFC**, sur un même jeu de données, à l'aide du logiciel **SAS**. Comme pour **R**, nous ne pourrons voir ici toutes les options des procédures utilisées.

## Données

Nous allons travailler sur la table `SASHELP.GNP` présente directement dans le logiciel. Celle-ci contient le produit national brut (*Gross National Product* ou **GNP**) de 1960 à 1991. Vous avez ici un aperçu de cette table (8 premières   lignes).

  DATE	  |GNP	  |CONSUMP	|INVEST	|EXPORTS	|GOVT
  --------|------:|--------:|------:|--------:|---:
  1960Q1	|516.1	|325.5	|88.7	|4.3	|97.6
  1960Q2	|514.5	|331.6	|78.1	|5.1	|99.6
  1960Q3	|517.7	|331.7	|77.4	|6.5	|102.1
  1960Q4	|513.0	|333.8	|68.5	|7.7	|103.0
  1961Q1	|517.4	|334.4	|69.5	|8.3	|105.3
  1961Q2	|527.9	|339.1	|74.7	|7.0	|107.1
  1961Q3	|538.5	|341.9	|81.2	|6.6	|108.7
  1961Q4	|551.5	|349.1	|83.0	|6.9	|112.5

### Premier travail à faire

Vous devez modifier la table de départ pour obtenir la suivante :

year	|q1	 |q2	|q3	 |q4
------|---:|---:|---:|---:
y1960	|516.1	|514.5	|517.7	|513.0
y1961	|517.4	|527.9	|538.5	|551.5
y1962	|564.4	|572.2	|579.2	|582.8
y1963	|592.1	|600.3	|613.1	|622.1
y1964	|636.9	|645.6	|656.0	|660.6

## ACP

L'**Analyse en Composantes Principales** est obtenue sous SAS avec la procédure **`PRINCOMP`**. Voici la syntaxe avec les options et paramètres principaux.

```sas
PROC PRINCOMP DATA = <table>
    OUT = <table en sortie>
    OUTSTAT = <table d'informations>
    COV N = <nb composantes> VARDEF = <diviseur de la variance>
    PLOTS = <listes des graphiques à produire>;
  VAR <variables>;
  ID <identifiant>;
RUN;
```

L'option `COV` permet d'indiquer que l'on souhaite travailler sur la matrice de covariance, plutôt que celle de corrélation. `VARDEF` va nous permettre de définir le calcul de la variance *à la française*.

Pour la liste des graphiques, il est possible d'indiquer que nous les voulons tous avec `ALL`.

Vous devez réaliser l'ACP sur la table `GNP` nouvellement créée, en indiquant une table de sortie pour récupérer les coordonnées sur les composantes principales (nous n'en garderons que deux), ainsi que les statistiques disponibles (dans une autre table donc). Il faudra spécifier que le diviseur pour la variance est `N`. Et nous allons produire tous les graphiques pour le moment.

> Analyser les résultats obtenus.

## AFC

L'**Analyse Factorielle des Correspondances** se fait à l'aide de la procédure `CORRESP`. Voici la syntaxe avec les options et paramètres principaux.

```sas
PROC CORRESP DATA = <table>
    OUT|OUTC = <table des coordonnées>
    OUTF = <tables des effectifs>
    DIMENS = <nombre de dimensions>
    ALL|OBSERVED|.. <informations à afficher>
    PLOTS = <listes des graphiques à produire>;
  TABLES <variables à croiser>;
  VAR <variables contenant la table de contingence>;
  ID <identifiant>;
RUN;
```

Il y a donc deux façons d'utiliser cette procédure. Soit les données que vous avez à traiter dans une table de type individus décrits par des variables. Dans ce cas, il faut préciser que c'est le croisement de ces deux variables qu'il faut analyser, à l'aide de la clause `TABLES`. Il est possible de pondérer chaque observation si nécessaire. Soit la table est déjà une table de contingence, et dans ce cas, il faut lister les variables (si besoin) à prendre en considération dans l'AFC, à l'aide de `VAR`. Les deux ne peuvent bien évidemment pas être utilisés en même temps.

Pour la liste des graphiques, il est aussi possible d'indiquer que nous les voulons tous, toujours avec `ALL`.

Vous devez donc réaliser l'AFC sur la table `GNP`, en indiquant une table de sortie pour récupérer les coordonnées sur les dimensions (nous n'en garderons que deux), ainsi que toutes les autres informations possibles. Nous allons produire tous les graphiques pour le moment.

> Analyser les résultats obtenus.

## Conclusion

En regardant les résultats, nous remarquons que l'AFC nous donne beaucoup plus d'informations intéressantes que l'ACP. En effet, celle-ci se concentre sur les volumes. Alors que l'AFC nous permet de repérer des profils différents entre les années.

## A faire

Sur ces [données de consommation électriques](https://www.data.gouv.fr/fr/datasets/consommation-electrique-par-secteur-dactivite/), vous appliquerez ces deux analyses pour voir laquelle est la plus pertinente, et quelles conclusions nous pouvons faire sur le lien entre les régions et les secteurs d'activité sur la consommation totale.
