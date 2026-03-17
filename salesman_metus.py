from math import radians, cos, sin, sqrt, atan2
import plotly.graph_objects as go
import pandas as pd
import json, haversine, random


def haversine_distance(ville1, ville2):
    return haversine.haversine(
        (ville1.latitude, ville1.longitude), (ville2.latitude, ville2.longitude)
    )


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
            nom=item["nom"], latitude=item["latitude"], longitude=item["longitude"]
        )
        villes.append(nouvelle_ville)

    return villes


def generate_individu(villes):
    individu = random.sample(
        villes, len(villes)
    )  # Crée une nouvelle liste mélangée sans modifier l'originale
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
        distance_totale += haversine_distance(individu[i], individu[i + 1])
    # On ajoute le retour à la ville de départ pour fermer le circuit
    distance_totale += haversine_distance(individu[-1], individu[0])
    return 1 / distance_totale


def selection_tournoi(population, k=3):
    population_tournoi = random.sample(
        population, k
    )  # Sélectionne k individus au hasard
    deux_parents = sorted(population_tournoi, key=fitness, reverse=True)[
        :2
    ]  # Garde les 2 meilleurs
    return deux_parents


def ox_crossover(parent1, parent2):

    taille = len(parent1)
    enfant = [None] * taille

    p1_idx, p2_idx = sorted(random.sample(range(taille), 2))

    enfant[p1_idx:p2_idx] = parent1[p1_idx:p2_idx]

    villes_presentes = set(enfant)

    p2_index = 0
    for i in range(taille):
        if enfant[i] is None:
            while parent2[p2_index] in villes_presentes:
                p2_index += 1
            enfant[i] = parent2[p2_index]
            villes_presentes.add(parent2[p2_index])

    return enfant


def swap_mutation(individu, p_mutation=0.02):
    if random.random() < p_mutation:
        idx1, idx2 = random.sample(range(len(individu)), 2)
        individu[idx1], individu[idx2] = individu[idx2], individu[idx1]
    return individu


def new_population(population, taille_population):
    nouvelle_population = []
    for _ in range(taille_population):
        parent1, parent2 = selection_tournoi(population)
        enfant = ox_crossover(parent1, parent2)
        enfant_muté = swap_mutation(enfant)
        nouvelle_population.append(enfant_muté)
    return nouvelle_population


global nb_gens

def tsp_algorithm(n_villes=5, taille_pop=100, gens=500):
    global nb_gens
    nb_gens = 0
    villes = generate_random_villes(n_villes)
    pop = generate_genese(villes, taille_pop)
    optimum_global = pop[0]
    for _ in range(gens):
        nouvelle_pop = new_population(pop, taille_pop)
        optimum_local = max(nouvelle_pop, key=fitness)
        if fitness(optimum_local) > fitness(optimum_global):
            optimum_global = optimum_local
        pop = nouvelle_pop
        nb_gens += 1
    return villes, optimum_global, 1 / fitness(optimum_global)


if __name__ == "__main__":
    print("Résultat du TSP avec l'algorithme génétique :")
    villes, optimum, distance = tsp_algorithm()
    print("Distance totale :", distance, "km")
    print("Test obtenu au bout de " + str(nb_gens) + " générations.")
    for ville in optimum:
        print(ville.nom + " -> ", end="")

