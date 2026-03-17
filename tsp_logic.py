import json, haversine, random


# ── Modèle ────────────────────────────────────────────────────────────────────

class Ville:
    def __init__(self, nom, latitude, longitude):
        self.nom = nom
        self.latitude = latitude
        self.longitude = longitude


# ── Utilitaires ───────────────────────────────────────────────────────────────

def haversine_distance(v1, v2):
    return haversine.haversine((v1.latitude, v1.longitude), (v2.latitude, v2.longitude))

def charger_villes_aleatoires(n):
    data = json.load(open("villes_france.json", encoding="utf-8"))
    return [Ville(d["nom"], d["latitude"], d["longitude"]) for d in random.sample(data, n)]


# ── Algorithme génétique ──────────────────────────────────────────────────────

def fitness(individu):
    # Distance totale du circuit (retour au départ inclus)
    dist = sum(haversine_distance(individu[i], individu[i+1]) for i in range(len(individu)-1))
    dist += haversine_distance(individu[-1], individu[0])
    return 1 / dist  # plus la distance est petite, plus le score est grand

def selection_tournoi(population, k=3):
    # Tire k individus au hasard, garde les 2 meilleurs
    return sorted(random.sample(population, k), key=fitness, reverse=True)[:2]

def ox_crossover(parent1, parent2):
    # Copie un segment du parent1, complète avec le parent2 (ordre préservé)
    taille = len(parent1)
    enfant = [None] * taille
    a, b = sorted(random.sample(range(taille), 2))
    enfant[a:b] = parent1[a:b]
    presents = set(enfant)
    j = 0
    for i in range(taille):
        if enfant[i] is None:
            while parent2[j] in presents:
                j += 1
            enfant[i] = parent2[j]
            presents.add(parent2[j])
    return enfant

def mutation(individu, p=0.02):
    # Échange deux villes avec une probabilité p
    if random.random() < p:
        i, j = random.sample(range(len(individu)), 2)
        individu[i], individu[j] = individu[j], individu[i]
    return individu

def nouvelle_generation(population):
    nouvelle = []
    for _ in range(len(population)):
        p1, p2 = selection_tournoi(population)
        enfant = mutation(ox_crossover(p1, p2))
        nouvelle.append(enfant)
    return nouvelle


# ── Point d'entrée ────────────────────────────────────────────────────────────

nb_gens = 0  # exposé pour que main.py puisse l'afficher

def tsp_algorithm(n_villes=10, taille_pop=100, nb_generations=500):
    global nb_gens
    villes = charger_villes_aleatoires(n_villes)
    pop = [random.sample(villes, len(villes)) for _ in range(taille_pop)]
    meilleur = max(pop, key=fitness)

    for nb_gens in range(1, nb_generations + 1):
        pop = nouvelle_generation(pop)
        champion = max(pop, key=fitness)
        if fitness(champion) > fitness(meilleur):
            meilleur = champion

    return villes, meilleur, 1 / fitness(meilleur)
