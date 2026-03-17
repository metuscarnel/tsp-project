import tkinter as tk
from tkinter import messagebox
import plotly.graph_objects as go
import salesman_metus as tsp  # ton module logique

# --- Config Couleurs & Police ---
BG_COLOR = "#FFFFFF"
ACCENT_BLUE = "#87CEEB"
TEXT_COLOR = "#2C3E50"
FONT_MAIN = ("Verdana", 10)
FONT_TITLE = ("Verdana", 12, "bold")

# --- Fonctions ---
def lancer_ia():
    try:
        n = int(entree_n.get())
        # --- Calcul TSP ---
        villes_init, chemin, distance = tsp.tsp_algorithm(n_villes=n)
        
        label_resultat.config(text=f"Distance : {distance:.2f} km | Générations : {tsp.nb_gens}")
        
        # --- Mise à jour Text Area ---
        zone_texte.delete("1.0", tk.END)
        zone_texte.tag_configure("header", foreground=ACCENT_BLUE, font=FONT_MAIN + ("bold",))
        zone_texte.tag_configure("ville", foreground=TEXT_COLOR)

        # Ordre initial
        zone_texte.insert(tk.END, "🎲 ORDRE INITIAL GÉNÉRÉ :\n", "header")
        for v in villes_init:
            zone_texte.insert(tk.END, f"  • {v.nom}\n", "ville")
        zone_texte.insert(tk.END, "\n" + "="*30 + "\n\n")

        # Chemin optimisé
        zone_texte.insert(tk.END, f"🚀 CHEMIN OPTIMISÉ (Départ : {chemin[0].nom})\n", "header")
        for i, v in enumerate(chemin, start=1):
            zone_texte.insert(tk.END, f"  {i}. {v.nom}\n", "ville")
        zone_texte.insert(tk.END, f"  {len(chemin)+1}. {chemin[0].nom} (Retour)\n", "header")

        # Carte
        afficher_carte(chemin, distance)

    except Exception as e:
        messagebox.showerror("Erreur", str(e))


def afficher_carte(chemin, distance):
    trace = chemin + [chemin[0]]
    mode_affichage = 'lines+markers+text' if len(chemin) < 25 else 'lines+markers'
    
    fig = go.Figure(go.Scattermapbox(
        lat=[v.latitude for v in trace],
        lon=[v.longitude for v in trace],
        mode=mode_affichage,
        text=[f"{i+1}. {v.nom}" for i, v in enumerate(chemin)] + ["Arrivée"],
        textposition="top right",
        marker=dict(size=8, color=ACCENT_BLUE),
        line=dict(width=2, color=ACCENT_BLUE),
        hoverinfo="text"
    ))

    fig.update_layout(
        title=f"Circuit IA - {distance:.2f} km",
        mapbox_style="open-street-map",
        mapbox=dict(center=dict(lat=46.6, lon=2.2), zoom=5),
        margin={"r":0,"t":50,"l":0,"b":0}
    )
    fig.show()


# --- Interface ---
root = tk.Tk()
root.title("TSP IA - Interface de Contrôle")
root.geometry("900x650")
root.configure(bg=BG_COLOR)

# Header
header = tk.Frame(root, bg=ACCENT_BLUE, height=60)
header.pack(fill=tk.X)
tk.Label(header, text="Optimisation de Trajet (Algorithme Génétique)", bg=ACCENT_BLUE, fg="white", font=FONT_TITLE).pack(pady=15)

# Contenu principal
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(expand=True, fill=tk.BOTH, padx=30, pady=20)

# Section Contrôle
frame_ctrl = tk.Frame(main_frame, bg=BG_COLOR)
frame_ctrl.pack(side=tk.LEFT, anchor="n", padx=10)

tk.Label(frame_ctrl, text="Nombre de villes", bg=BG_COLOR, font=FONT_MAIN).pack(pady=(0,5))
entree_n = tk.Entry(frame_ctrl, font=FONT_MAIN, justify="center", width=8, relief="flat", highlightbackground=ACCENT_BLUE, highlightthickness=1)
entree_n.insert(0, "20")
entree_n.pack(pady=5)

btn_calcul = tk.Button(frame_ctrl, text="CALCULER", command=lancer_ia, bg=ACCENT_BLUE, fg="white", font=FONT_TITLE, relief="flat", cursor="hand2", padx=20)
btn_calcul.pack(pady=20)

label_resultat = tk.Label(frame_ctrl, text="Prêt pour le calcul", bg=BG_COLOR, font=FONT_MAIN, fg=TEXT_COLOR)
label_resultat.pack(pady=10)

# Section Texte + Scroll
frame_liste = tk.Frame(main_frame, bg=BG_COLOR)
frame_liste.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

tk.Label(frame_liste, text="Feuille de route & Séquences :", bg=BG_COLOR, font=FONT_TITLE, fg=TEXT_COLOR).pack(anchor="w")

scrollbar = tk.Scrollbar(frame_liste)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

zone_texte = tk.Text(frame_liste, font=FONT_MAIN, bg="#F8FBFF", fg=TEXT_COLOR, relief="flat", padx=10, pady=10, highlightthickness=1, highlightbackground="lightblue", yscrollcommand=scrollbar.set)
zone_texte.pack(expand=True, fill=tk.BOTH, pady=5)
scrollbar.config(command=zone_texte.yview)

root.mainloop()