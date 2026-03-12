from math import radians, cos, sin, sqrt, atan2
import plotly.graph_objects as go
import pandas as pd
import json, haversine, random
def haversine_distance(ville1, ville2):
  return haversine.haversine((ville1.latitude, ville1.longitude), (ville2.latitude, ville2.longitude))

class Ville:
    def __init__(self, nom, latitude, longitude):
        self.nom = nom
        self.latitude = latitude
        self.longitude = longitude

def generate_random_villes(n):
    villes = []
    donnees_json = json.load(open("villes_france.json", "r", encoding="utf-8"))
    
    selection_aleatoire = random.sample(donnees_json, n)

    for item in selection_aleatoire:
        nouvelle_ville = Ville(
            nom=item["nom"],
            latitude=item["latitude"],
            longitude=item["longitude"]
        )
        villes.append(nouvelle_ville)

    return villes
def generate_individu(villes):
    individu = random.sample(villes, len(villes)) # Crée une nouvelle liste mélangée sans modifier l'originale
    return individu
def generate_genese(villes, taille_population):
    population = []
    for _ in range(taille_population):
        individu = generate_individu(villes)
        population.append(individu)
    return population


def fitness(individu):
    distance_totale = 0
    for i in range(len(individu) - 1):
        distance_totale += haversine_distance(
            individu[i],
            individu[i+1]
        )
    # On ajoute le retour à la ville de départ ici, pas dans l'individu
    distance_totale += haversine_distance(
        individu[-1],
        individu[0]
    )
    return 1 / distance_totale

i=1
for individu in generate_genese(generate_random_villes(10), 10):
    print(f"Individu :{i}")
    for v in individu:
        print(f"- {v.nom} (Lat:{v.latitude:.2f}, Lon:{v.longitude:.2f})" + f"")
    print(f"Distance totale : {fitness(individu):.2f} km\n")
    i += 1
def selection_tournoi(population):
    population_tournoi = random.sample(population, 3) # Sélectionne 3 individus au hasard
    deux_parents = sorted(population_tournoi, key=fitness, reverse=True)[:2] # Garde les 2 meilleurs
    return deux_parents

def ox_crossover(parent1, parent2):
    taille = len(parent1)
    enfant = [None] * taille

    # Sélectionne deux points de crossover
    point1, point2 = sorted(random.sample(range(taille), 2))

    # Copie la section entre les deux points du parent1
    enfant[point1:point2] = parent1[point1:point2]

    # Remplit les positions restantes avec les villes du parent2 dans l'ordre
    index_parent2 = 0
    for i in range(taille):
        if enfant[i] is None:
            while parent2[index_parent2] in enfant:
                index_parent2 += 1
            enfant[i] = parent2[index_parent2]
            index_parent2 += 1

    return enfant