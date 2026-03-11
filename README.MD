# Traveling Salesman Problem
## Modélisation des objets 
Individu : Liste de points Point dans l'espace donc : Coordonnées 3D
Choix de la ville de départ aléatoirement
Calcul de la distance : D=∑i=1N−1​distance(ci​,ci+1​)+distance(cN​,c1​)
Population : Ensemble d'individus
Fonction d'évaluation (fitness) : f =  1/D, plus le D est grand plus f est petit
Paramètres : 
La fonction de sélection : Basé sur le fitness
Croisement : Récupérer une section (ensemble de ville) chez des parents pour créer des enfant
Fonction de mutation : Choix de deux villes au hasard et permutation 
Fonction de génération de la nouvelle population : 
Et récursivitié
API de récupération des coordonnées et villes de france ( plusn fun à faire)

ETL (Extract, Transform, Load) :
Récupération de toutes les communes Françaises :     url = "https://geo.api.gouv.fr/communes?fields=nom,centre&format=json&geometry=centre"

Je procède par une récupération des villes de france et leur coordonnées pour rendre le code un peu plmus réaliste.
Choix de la taille de la population initiale