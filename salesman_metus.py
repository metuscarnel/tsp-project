from math import radians, cos, sin, sqrt, atan2
import plotly.graph_objects as go
import pandas as pd
import json, haversine, random
def haversine_distance(ville1, ville2):
    lat1, lon1 = ville1['latitude'], ville1['longitude']
    lat2, lon2 = ville2['latitude'], ville2['longitude']
    return haversine.haversine((lat1, lon1), (lat2, lon2))

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
    individu = villes[:]
    random.shuffle(individu)
    individu.append(individu[0]) 
    return individu
def generate_genese(villes, taille_population):
    population = []
    for _ in range(taille_population):
        individu = generate_individu(villes)
        population.append(individu)
    return population

for ville in generate_genese(generate_random_villes(3), 5):
    i=1
    print(f"Individu :{i}")
    for v in ville:
        print(f"- {v.nom} (Lat:{v.latitude:.2f}, Lon:{v.longitude:.2f})")
    i += 1