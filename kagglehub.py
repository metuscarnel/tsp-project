from haversine import haversine
import json
villes = json.load(open("villes_france.json", "r", encoding="utf-8"))
villes_tests = [None] * 10
for i in range(len(villes_tests)):
    villes_tests[i] = villes[i]
def longueur_tour(tour, villes):
    total = 0
    for i in range(len(tour)):
        a = villes[tour[i]]
        b = villes[tour[(i+1) % len(tour)]]
        total += haversine(a, b)
    return total
import itertools

def brute_force(villes):
    best = float("inf")
    best_tour = None

    # On fixe la première ville pour éviter les doublons
    for perm in itertools.permutations(range(1, len(villes))):
        tour = (0,) + perm

        d = longueur_tour(tour, villes)

        if d < best:
            best = d
            best_tour = tour

    return best, best_tour
opt, _ = brute_force(villes_tests)
ga = sale(villes_tests)  # Remplace par l'appel à ton algorithme génétique

print("Optimal :", opt)
print("GA :", ga)
print("Erreur (%) :", (ga - opt) / opt * 100)