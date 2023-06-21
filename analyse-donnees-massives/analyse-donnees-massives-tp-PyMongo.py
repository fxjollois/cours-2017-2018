# MongoDB from Python

import pymongo
import pprint

# Création du client pour connection à Mongo
from pymongo import MongoClient
client = MongoClient()

# Liste des bases de données existantes
client.database_names()

# Choix d'une base dans une variable
db = client.gym

# Liste des collections
db.collection_names()

# Création de variables pointant vers chaque collection
sportifs = db.Sportifs
gymnases = db.Gymnases

# Dénombrement simple
sportifs.count()
gymnases.count()

# Affichage du premier document
sportifs.find_one()
gymnases.find_one()

# Valeurs distinctes
gymnases.distinct("Ville")
gymnases.distinct("Surface")
gymnases.distinct("Seances.Libelle")
gymnases.distinct("Seances.Jour")
sportifs.distinct("Sexe")
sportifs.distinct("Sports.Jouer")

# Recherche
for res in sportifs.find({ "Nom": "KERVADEC" }):
    pprint.pprint(res)

for res in sportifs.find({ "Nom": "KERVADEC" }, { "_id": 0, "Nom": 1 }):
    pprint.pprint(res)

for res in sportifs.find({ "Age": { "$gte": 32} }, { "_id": 0, "Nom": 1, "Age": 1 }):
    pprint.pprint(res)

sportifs.find({ "Sexe" : "F" }).count()

for res in sportifs.find({ "Sexe" : "F" }, { "_id": 0, "Nom": 1, "Sexe": 1 }).limit(5):
    pprint.pprint(res)

for res in sportifs.find({ "Age": { "$gte": 32} }, { "_id": 0, "Nom": 1, "Age": 1 }).sort("Age"):
    pprint.pprint(res)

# Agrégats
for res in gymnases.aggregate([ 
    { "$group": { "_id": "", "nb": { "$sum": 1 }}}
]):
    pprint.pprint(res)

for res in gymnases.aggregate([ 
    { "$group": { 
        "_id": "$Ville", 
        "nb": { "$sum": 1 }, 
        "surfaceTotale": { "$sum": "$Surface" },
        "surfaceMoyenne": { "$avg": "$Surface" },
        "surfaceMinimum": { "$min": "$Surface" },
        "surfaceMaximum": { "$max": "$Surface" }
    }}
]):
    pprint.pprint(res)
    
for res in gymnases.aggregate([
    { "$unwind": "$Seances" }, 
    { "$project": { "Jour": { "$toLower": "$Seances.Jour" } }},
    { "$group": { "_id": "$Jour", "nb": { "$sum": 1 }} }
]):
    pprint.pprint(res)



