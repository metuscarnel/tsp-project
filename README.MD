# Traveling Salesman Problem
## Modélisation des objets 
Individu : Liste de points Point dans l'espace donc : Coordonnées 3D
Choix de la ville de départ aléatoirement
Calcul de la distance : D=∑i=1N−1​distance(ci​,ci+1​)+distance(cN​,c1​)
Population : Ensemble d'individus
Fonction d'évaluation (fitness) : f =  1/D, plus le D est grand plus f est petit

ETL (Extract, Transform, Load) :
Récupération de toutes les communes Françaises :  url = "https://geo.api.gouv.fr/communes?fields=nom,centre&format=json&geometry=centre" soit 34968 communes récupérées.

Je procède par une récupération des villes de france et leur coordonnées pour une étude basée sur des données réelles.
Choix de la taille de la population initiale : variable
Fonction principale crée, fin de la genèse de fonction de base.
Selection par tournoi, type de selection choisi
On choisi aléatoirement k individu et on en choisi 2 (exemple) pour former les parenrs qui vot subir le crossover 
methode de crossover choisi ox_crossover
Récuperer une section d'un des individus et l'insérer dans l'autre.
https://fr.mathworks.com/matlabcentral/fileexchange/93715-ordered-crossover-operator-for-permutations-based-problems?s_tid=answers_rc2-2_p5_MLT

https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_mutation.htm

Swap Mutation : selectionner deux chromosome au hasard et interchangé leur valeur avec une proba de 2% de mutation

Stratégie de remplacement : Les bons parents et leurs enfants.