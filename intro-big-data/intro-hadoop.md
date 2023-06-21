---
title: Introduction à Hadoop
---

## Informations

Nous allons nous baser sur un ensemble de tutoriels proposés par [Hortonworks](https://fr.hortonworks.com/tutorial/), permettant d'appréhender l'éco-système d'[Hadoop](http://hadoop.apache.org/) via leur machine virtuelle téléchargeable gratuitement ([ici](https://fr.hortonworks.com/products/sandbox/)).

Pour accéder à votre machine virtuelle, vous devez prendre l'IP celle qui vous est dédié ci-dessous. Celles-ci ne sont accessibles que depuis l'IUT.

| Etudiants              | Nom machine | IP            |
|------------------------|:-----------:|--------------:|
| ANTCHOUET	Jean-Marc    | hadoop01    | 172.19.35.201 |
| BERNARDI	Gérôme       | hadoop02    | 172.19.35.203 |
| BONINO	Mélanie      | hadoop03    | 172.19.35.208 |
| BOURAHLA	Walid        | hadoop04    | 172.19.35.205 |
| DEFFERRARD	Martin   | hadoop05    | 172.19.35.202 |
| DEMARE	Guillaume    | hadoop06    | 172.19.35.206 |
| DESCHAMPS	Antoine      | hadoop07    | 172.19.35.207 |
| DRUMARE	Flora        | hadoop08    | 172.19.35.209 |
| FAROOQ	Hamza        | hadoop09    | 172.19.35.204 |
| GEAY	Maxime           | hadoop10    | 172.19.35.212 |
| KAUR	Parminder        | hadoop11    | 172.19.35.214 |
| LACHUER	Adrien       | hadoop12    | 172.19.35.211 |
| LE FLOCH	Antoine      | hadoop13    | 172.19.35.213 |
| MAKOUMBOU	Stevy        | hadoop14    | 172.19.35.215 |
| MURUGADASAN Ushanthini | hadoop15    | 172.19.35.221 |
| PALALI	Anil         | hadoop16    | 172.19.35.227 |
| PINAL	Romain           | hadoop17    | 172.19.35.226 |
| SALHI	Fariza           | hadoop18    | 172.19.35.216 |
| SERHAL	Elsa         | hadoop19    | 172.19.35.210 |
| SIRAT	Kenza            | hadoop20    | 172.19.35.218 |
| THIRY	Maxence          | hadoop21    | 172.19.35.225 |
| WANG	Anhui            | hadoop22    | 172.19.35.224 |


## Tutoriels

### Premiers pas

Cet ensemble de tutoriels permet de commencer à appréhender l'environnement Hadoop. Vous trouverez sur [cette page](https://fr.hortonworks.com/tutorial/learning-the-ropes-of-the-hortonworks-sandbox/) les informations des différents comptes disponibles pour se connecter à Hadoop.

1. [Chargement des données](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/2/) dans **HDFS**
1. [Intégration des données](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/3/) dans **Hive**
1. [Calcul de facteur de risque](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/4/) avec **Pig**
1. [Calcul de facteur de risque](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/5/) avec **Spark**
1. [Reporting](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/6/) avec **Zeppelin**

### Pour aller plus loin

1. [Traiter les données avec Hive](https://fr.hortonworks.com/tutorial/how-to-process-data-with-apache-hive/)
1. [Traiter des données avec Pig](https://fr.hortonworks.com/tutorial/how-to-process-data-with-apache-pig/)
1. [Chargement et requêtage avec Hadoop](https://fr.hortonworks.com/tutorial/loading-and-querying-data-with-hadoop/)
1. [Visualisation de flux d'un site web](https://fr.hortonworks.com/tutorial/visualize-website-clickstream-data/section/1/)
1. [Retards aériens avec SparkR](https://fr.hortonworks.com/tutorial/predicting-airline-delays-using-sparkr/)
    Pour installer RStudio sur la machine, vous devez procéder aux étapes suivantes
    1. Aller sur le **shell-in-a-box** (cf ci-dessous) 
    1. Se connecter avec le compte : **raj_ops** (cf lien ci-dessus)
    1. Télécharger la version de **RStudio Server** :
    ```
    wget https://download2.rstudio.org/rstudio-server-rhel-1.1.453-x86_64.rpm
    ```
    1. Puis l'installer :
    ```
    sudo yum install rstudio-server-rhel-1.1.453-x86_64.rpm
    ```
    1. Puisque la machine virtuelle ne laisse pas accessible certains ports, il faut reconfigure le serveur. Pour cela, éditer le fichier de configuration 
    ```
    sudo vi /etc/rstudio/rserver.conf
    ```
    1. Appuyer sur la touche **`i`** (pour insérer du texte), puis sur la dernière ligne, écrire :
    ```
    www-port = 8090
    ```
    1. Faire `Esc`, puis taper `:wq` puis `Entrée`
    1. Pour vérifier, taper la commande suivante (première ligne après le `$`). Le résultat devrait être le même que ci-dessous (2ème et 3ème lignes)
    ```
    [raj_ops@sandbox-hdp ~]$cat /etc/rstudio/rserver.conf
    # Server Configuration File
    www-port = 8090
    ```
    1. Vérifier l'installation :
    ```
    sudo rstudio-server verify-installation
    ```
    1. Arrêter puir démarrer le serveur :
    ```
    sudo rstudio-server stop
    sudo rstudio-server start
    ```
    1. Se connecter sur le port dédié (cf ci-dessous) 
1. [Introduction au Machine Leanring avec Spark et Zeppelin](https://fr.hortonworks.com/tutorial/intro-to-machine-learning-with-apache-spark-and-apache-zeppelin/)

### A noter

Il est possible d'accéder aux différentes applications en modifiant le port d'accès (sous la forme `http://ip:port`). Voici les différentes applications et les ports correspondant :

| Application             | Port |
|-------------------------|-----:|
| Accueil                 | 8888 |
| Ambari                  | 8080 |
| shell-in-a-box          | 4200 |
| Zeppelin                | 9995 |
| Resource manager Hadoop | 8088 |
| RStudio                 | 8090 |

