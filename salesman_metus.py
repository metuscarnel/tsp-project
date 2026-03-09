from math import radians, cos, sin, sqrt, atan2
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
    
    
communes_france = json.load(open("villes_france.json", "r", encoding="utf-8"))
print(haversine_distance(communes_france[0], communes_france[1]))
print("Villes sélectionnées pour le trajet :")
for v in generate_random_villes(10):
    print(f"- {v.nom} (Lat:{v.latitude:.2f}, Lon:{v.longitude:.2f})")