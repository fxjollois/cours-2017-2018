# intro à Python

# quelques types de base

1
type(1)
1.234
type(1.234)
"chaîne"
type("chaîne")
(1, 2)
type((1, 2))
[1, 2]
type([1, 2])
{"a": 1, "b": "deux"}
type({"a": 1, "b": "deux"})

(1, (2, 3), [4, 5], {"a": 1, "b": "deux"})
[1, [2, 3], (4, 5), {"a": 1, "b": "deux"}]
{"a": 1, "b": "deux", "c": (5, 6), "d": [7, 8]}


# Valeurs particulières
False
True
None

# suppression d'une variable
a = 1
print(a)
print(b)
del(a)


# typage dynamique
a = 1
print(a)
type(a)
a = "deux"
print(a)
type(a)

# Affichage
print("Bonjour")
print("a =", a)
print("a", a, sep = "=")
print("a=", end = "")
print(a)


# opérateurs arithmétiques
5 + 2
5 - 2
5 * 2
5 / 2
5 // 2
5 % 2
5 ** 2

# opérateurs de comparaisons
5 > 2
5 >= 2
5 < 2
5 <= 2
5 == 2
5 != 2

# Opérateurs booléens
True | False
True & True
not(True)


# IF et autre

a = 3
if (a > 2):
    print("sup")

if (a > 2):
    print("dans le IF")
    print("sup")

a = 1
if (a > 2):
    print("sup")
else:
    print("inf")

if (a > 2):
    print("sup")
elif (a > 0):
    print("mid")
else:
    print("inf")

    
# Pour le switch/case, rien dans python mais on peut passer par un dictionnaire 
# pour des tests d'égalité

jour = {
    0: "lundi",
    1: "mardi",
    2: "mercredi",
    3: "jeudi",
    4: "vendredi",
    5: "samedi",
    6: "dimanche"
}
jour.get(2)


# Iteratif

for i in range(5):
    print(i)
print(i)

for i in range(5, 10):
    print(i)

for i in range(10, 5, -1):
    print(i)

for i in [4, 1, 10]:
    print(i)

for l in "Bonjour":
    print(l)

for l in ("jour", "soir"):
    print("Bon", l, sep = "")

a = [3, 1, 9, 4]
for i, x in enumerate(a):
    print("i =", i, "\tx =", x)

b = ["trois", "un", "neuf"]
for i, j in zip(a, b):
    print(" i =", i, "\tj =", j)

a = {"a": 1, "b": "deux"}
for cle in a:
    print(cle, "->", a[cle], sep = "\t")

i = 0
while i < 10:
    print(i)
    i += 1
print("Valeur de i :", i)


# sur les chaînes
a = "bonjour"
len(a)
a[1:5]
a[0:3]
a[:3]
a[3:len(a)]
a[3:]
a[::]
a[::-1]
a[::2]
a[1:5:2]
a[5:1:-2]
a.upper()
a.capitalize()
a.find('j')
a.replace('jour', 'soir')
a.count('o')
a.split('j')

# Création de tuples
a = (3, 1, 9, 7)
print(a)
a[0]
a[0] = 5 # Pas possible : tuple == constante
tuple([3, 1])

# Création de listes
a = [3, 1, 9, 7]
print(a)
len(a)
a[0]
a[1:3]

a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.pop()
print(a)
a.append(5)
print(a)
a.insert(0, 6)
print(a)
a.remove(7)
print(a)

a * 2
a + 1
a + [1, 2]

a = [3, 1, 9, 7]
[x**2 for x in a]
[x**2 for x in a if x >= 4]


# Attention aux passages de référence
a = [1, 2, 3, 4]
print(a)
b = a
print(b)
a[0] = 5
print(a)
print(b)
b[1] = 9
print(b)
print(a)
b = a.copy()
a[0] = -1
print(a)
print(b)

# Listes nommées -> dictionnaires
a = { "nom": "Jollois", "prenom": "FX", "langues": ["R", "Python", "SQL", "SAS"], "labo": { "nom": "LIPADE", "lieu": "CUSP"}}
print(a)
len(a)

a["nom"]
a["langues"]
a["langues"][0]
a["labo"]
a["labo"]["lieu"]

a.get("nom")
a.keys()
a.values()
a.popitem()
print(a)
a.pop("nom")
print(a)

a["type"] = "MCF"
print(a)

b = a
b["prenom"] = "Xavier"
print(b)
print(a)

b = a.copy()
b["prenom"] = "FX"
print(b)
print(a)

fruits = ["pommes", "bananes", "poires", "oranges"]
nombres = [5, 2, 10, 4]
{fruits[i]:nombres[i] for i in range(4)}
dict(zip(fruits, nombres))








# Fonctions

def pi():
    res = 3.141593 ** 2
    return res
pi()

def afficheBonjour():
    print("Bonjour")
afficheBonjour()

def afficheBonjour(nom):
    print("Bonjour", nom)
afficheBonjour("Jollois")
afficheBonjour()

def afficheBonjour(nom, prenom):
    print("Bonjour", prenom, nom)
afficheBonjour("Jollois", "FX")
afficheBonjour(nom = "Jollois", prenom = "FX")
afficheBonjour(prenom = "FX", nom = "Jollois")
afficheBonjour(prenom = "FX", "Jollois")

def afficheBonjour(nom, prenom = "?"):
    print("Bonjour", prenom, nom)
afficheBonjour("Jollois", "FX")
afficheBonjour("Jollois")

# Attention à la "pureté" d'une fonction

def f1(a):
    a = [b**2 for b in a]
    return a
a = list(range(5))
print(a)
print(f1(a))
print(a)

def f2(a):
    for i in a:
        a[i] = a[i] ** 2
    return a
a = list(range(5))
print(a)
print(f2(a))
print(a)

# Gestion des erreurs

def somme(v):
    try:
        res = sum(v)
    except:
        print("Erreur : somme impossible !")
        res = None
    finally:
        return res
a = somme([1, 3, 5])
print(a)
a = somme(["un", 3, 5])
print(a)

# Fonctions sur Listes

a = [13, 7, 2, 9, 1, 10, 6, 3, 8]
print(a)

# map()
def carre(v):
    return v ** 2
carre(5)

b = map(carre, a)
print(list(b))

# filter
def pair(v):
    return v%2 == 0
pair(5)
pair(8)

b = filter(pair, a)
print(list(b))

# reduce
def somme(v1, v2): 
    return v1 + v2
somme(3, 10)

import functools
b = functools.reduce(somme, a)
print(b)

b = functools.reduce(somme, a, 100)
print(b)

# Fonction anonyme : SUR UNE SEULE LIGNE
b = map(lambda v: v ** 2, a)
print(list(b))

b = map(lambda v: v **2 if v > 8 else -(v ** 2), a)
print(list(b))


# Fichier

# répertoire courant
os.getcwd()

# changer
os.chdir("Sites/fxjollois.github.io/")
os.getcwd()

fichier = open("donnees/Iris.txt")
lignesBrutes = fichier.readlines()
fichier.close()




# Exercices

# import csv
# lignes = csv.reader(open("donnees/Iris.txt"), delimiter = ";", quotechar = "'")

lignes = [l.replace("\n", "").replace("'", "").split(";") for l in lignesBrutes]

def enReel(x):
    try:
        res = float(x)
        return res
    except:
        return x

donnees = []
for i, l in enumerate(lignes):
    if i == 0:
        var = l
    else:
        donnees.append({cle:enReel(val) for cle, val in zip(var, l)})
donnees

[{cle:enReel(val) for cle, val in zip(var, l)} for l in lignes[1:]]


# Mapper : superficie ??
# Filtrer : qu'une seule espèce 
# Réduire : moyenne des variables