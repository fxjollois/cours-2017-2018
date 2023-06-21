---
title: TP MongoDB
---

Vous devez rendre ce TP pour lundi 19 juin, à 18h, en l'envoyant par mail à 

    francois - xavier . jollois [@] parisdescartes . fr

Merci de mettre vos réponses dans le mail, avec le formalisme suivant :

```js
## Question à laquelle vous répondez
code R
```

### Trafic parisien

Nous allons utiliser la base de données `trafic`, dans laquelle il y a
trois collections :

- `capteurs` : liste des capteurs permanents ([source](https://opendata.paris.fr/explore/dataset/referentiel-comptages-routiers/information/))
- `capteurs_geo` : idem, mais au format GeoJson (qu'on ne va pas utiliser a priori)
- `trafic` : débit et taux d'occupation par heure sur les différents capteurs ([source](https://opendata.paris.fr/explore/dataset/comptages-routiers-permanents/information/))

Répondre aux questions suivantes :

- Afficher le premier document des collections `capteurs` et `trafic`, ainsi que le nombre de documents existants dans chacune des collections
- Afficher sur des graphiques le débit et le trafic moyen 
    - par année
    - par mois
    - par jour de la semaine
- Récupérer les coordonnées (point) de chaque capteur, puis les afficher sur une carte
- Ajouter l'information sur le nombre de mesures pour chaque capteur à la carte précédente
- Récupérer les débits et les taux d'occupation du capteur 1, et afficher les évolutions
    - depuis le début
    - idem en moyenne journalière
    - en moyenne journalière, par année (une couleur par année et années superposées)
    - moyenne horaire sur une journée
    - moyenne horaire sur une journée, pour chaque mois
    - moyenne horaire sur une journée, comparaison semaine/week-end
- Récupérer les coordonnées du tronçon de chaque capteur, puis les afficher sur une carte
