import salesman_metus as tsp
import json
import haversine 
villes = json.load(open("villes_france.json", "r", encoding="utf-8"))
villes_tests = [None] * 10
for i in range(len(villes_tests)):
    villes_tests[i] = villes[i]

print(villes_tests)

def bfs():
    # Implémentation de l'algorithme de recherche en largeur (BFS)
    ville_depart = villes_tests[0]  # Choix de la ville de départ
    file = [ville_depart]  # File pour BFS
    visites = set()  # Ensemble pour suivre les villes visitées
    chemin = []  # Chemin parcouru 
    
    