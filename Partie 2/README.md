
# 3I025 - Projet 2

Rapport de présentation du second projet de 3I025 du binôme constitué de Benjamin Loglisci et d'André Nasturas.

## Présentation

Ce second projet du cours d'IA 3I025 a pour but la réalisation d'une intelligence artificielle pour les personnages d'un jeu de collecte d'objets sur une carte en deux dimensions. L'enjeu principal est de développer les stratégies de recherche de chemin optimal entre le personnage et les objectifs à atteindre, ainsi que les stratégies d'échange lors des rencontre entre les personnages.

### Organisation du dépôt

Le [dépôt GitHub](http://github.com/3201101/3I025/tree/master) sur lequel nous hébergeons le code de notre projet contient les sources du présent projet (**Projet 2**) ainsi que celles du projet précédent, dont certaines parties seront réutilisées ici. De plus, les sources que nous avons écrites et celles fournies sont séparés dans deux dossiers distincts (**app** et **teaching-iaro**) pour plus de clarté et d'efficacité.

## Recherche de chemin : l'algorithme A*

Premièrement, il est nécessaire d'implémenter l'algorithme de recherche de chemin, ou _pathfinding_, afin de permettre à un personnage d'atteindre le plus rapidement possible un objectif donné. Cette implémentation est faite dans la méthode _doAStar()_ du fichier **AStar.py**

## Répartition des objectifs : le problème du multijoueur

Lorsqu'un puzzle est conçu pour être complété par plusieurs joueurs simultanément, il faut décider des objectifs à attribuer à chacun d'eux pour éviter qu'ils ne se ruent tous ensemble inutilement sur une seul et même cible. Il y a pour celà plusieurs techniques possibles, toutes implémentés dans le fichier **repartiteur.py**.

D'une manière générale, chacune de ces méthodes génère d'abord toutes les routes possibles entre chaque personnage et chaque objectif (en appelant _doAStar()_), puis applique une logique pour décider des routes à retenir en fonction de la longueur des chemins obtenus.

### Les enchères

La méthode _repEnchere()_ implémente la technique des enchères : tant que la répartition n'est pas terminée, un joueur prendra son meilleur choix en fonction de la longueur du chemin pour l'atteindre.

### La dynamique de meilleure réponse

La méthode _repDynamique()_ implémente une technique similaire aux enchères, mais lorsque deux personnages on le même objectif favori, ils le perdent tous les deux et passent à leur second choix.

Cette technique présente en l'état l'inconvénient de ne pas systématiquement pouvoir se terminer. On cherche donc à détecter ce cas de figure pour le traiter, en lancant une exception ou en utilisant une autre méthode de répartition.

### L'algorithme de Gale-Shapley

La méthode _repGaleShapley()_ permet d'utiliser le code d'apparaiement par l'algorithme de Gale-Shapley du Projet 1 afin de répartir les objectifs entre chaque personnage de manière optimisée et stable selon un ordre de préférence basé sur la longueur (et donc la durée) des chemins calculés précédemment par l'algorithme A*.

## Les rencontres entre joueurs : coopération ou aggression

Lorsqu'un joueur en rencontre un autre, il a le choix entre coopérer avec lui ou tenter de le voler.

Dans la boucle principale du programme, on appelle pour chaque voisin du joueur courant (s'il en a) la méthode _meet()_ de l'objet _PotionGame_ défini dans le fichier **GTAPotion.py**. Cet objet, initialisé au début du programme avec éventuellement des paramètres passées en ligne de commande, gère les stratégies des différents joueurs. Ainsi, chaque personnage peut avoir sa propre stratégie d'échange avec les autres parmi celles implémentés dans les différentes méthodes _fooStrat()_.

