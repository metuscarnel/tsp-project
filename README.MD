# Traveling Salesman Problem
## Modélisation des objets 
Individu : Liste de points Point dans l'espace donc : Coordonnées 3D
Choix de la ville de départ aléatoirement
Calcul de la distance : D=∑i=1N−1​distance(ci​,ci+1​)+distance(cN​,c1​)
Population : Ensemble d'individus
Fonction d'évaluation (fitness) : f =  1/D, plus le D est grand plus f est petit

ETL (Extract, Transform, Load) :
Récupération de toutes les communes Françaises :  url = "https://geo.api.gouv.fr/communes?fields=nom,centre&format=json&geometry=centre"

Je procède par une récupération des villes de france et leur coordonnées pour une étude basée sur des données réelles.
Choix de la taille de la population initiale : variable
Fonction principale crée, fin de la genèse de fonction de base.
Selection par tournoi, type de selection choisi
On choisi aléatoirement k individu et on en choisi 2 (exemple) pour former les parenrs qui vot subir le crossover