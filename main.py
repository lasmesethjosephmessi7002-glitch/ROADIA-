# main.py (version corrigée : virages + continuation après virage)
import tkinter as tk
from vehicle import Vehicle
import math

# ---------- Configuration ----------
INTERSECTION_POS = 100.0
CANVAS_W, CANVAS_H = 600, 600
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2
SCALE = 2.0
TICK_MS = 70   # animation

# Paramètres d'arc
ARC_PROGRESS_FOR_QUARTER = 20.0   # valeur de horiz_progress correspondant à l'arc de 90°
ARC_RADIUS = 40                   # rayon de l'arc en pixels (visuel)

# ---------- Véhicules (directions fixées dès le départ) ----------
v1 = Vehicle("V1", position=40.0, speed=40.0, chosen_direction="Left")
v2 = Vehicle("V2", position=20.0, speed=40.0, chosen_direction="Right")
v3 = Vehicle("V3", position=0.0,  speed=40.0, chosen_direction="Straight")

v2.front_vehicle = v1
v3.front_vehicle = v2
vehicles = [v1, v2, v3]

# ---------- Interface ----------
root = tk.Tk()
root.title("ROADIA Demo - Smart Intersection (corrected)")
canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white")
canvas.pack()

# Routes (forme +)
canvas.create_rectangle(CENTER_X - 50, 0, CENTER_X + 50, CANVAS_H, fill="lightgray", outline="")
canvas.create_rectangle(0, CENTER_Y - 50, CANVAS_W, CENTER_Y + 50, fill="lightgray", outline="")
canvas.create_rectangle(CENTER_X - 50, CENTER_Y - 50, CENTER_X + 50, CENTER_Y + 50,
                        fill="orange", outline="black")

canvas.create_text(CENTER_X, 20,
                   text="ROADIA Demo: V1 -> LEFT | V2 -> RIGHT | V3 -> STRAIGHT",
                   font=("Arial", 14, "bold"))

# Création formes voitures
vehicle_shapes, vehicle_labels = {}, {}
colors = {"V1": "blue", "V2": "green", "V3": "red"}
for v in vehicles:
    rect = canvas.create_rectangle(0, 0, 0, 0, fill=colors[v.id])
    label = canvas.create_text(0, 0, text="", font=("Arial", 9, "bold"))
    vehicle_shapes[v.id] = rect
    vehicle_labels[v.id] = label

# ---------- Mapping coords (corrigée) ----------
def map_coords(v: Vehicle):
    """
    Retourne (x, y) pour afficher la voiture v.
    - Avant le carrefour (not turned): approche verticale depuis le bas vers le centre.
    - Pendant le virage: arc (quart de cercle).
    - Après l'arc: continuation linéaire horizontale (pour Left/Right).
    - Straight: continue verticalement au dessus du centre.
    """
    if not v.turned:
        # approche verticale (venant du bas)
        x = CENTER_X
        y = CENTER_Y + int((INTERSECTION_POS - v.position) * SCALE)
    else:
        # on calcule angle proportionnel à horiz_progress (0 -> 0 ; ARC_PROGRESS_FOR_QUARTER -> pi/2)
        angle = (v.horiz_progress / ARC_PROGRESS_FOR_QUARTER) * (math.pi / 2)
        if angle > math.pi / 2:
            angle = math.pi / 2

        # portion d'arc (visuelle)
        arc_x = ARC_RADIUS * math.sin(angle)
        arc_y = ARC_RADIUS * (1 - math.cos(angle))

        # portion linéaire après arc (en "unités" de horiz_progress, converties en pixels)
        extra_progress = max(0.0, v.horiz_progress - ARC_PROGRESS_FOR_QUARTER)
        extra_pixels = int(extra_progress * SCALE)  # conversion simple unité -> pixels

        if v.chosen_direction == "Left":
            # arc à gauche puis continuation vers la gauche
            x = CENTER_X - int(arc_x) - extra_pixels
            y = CENTER_Y - int(arc_y)
        elif v.chosen_direction == "Right":
            # arc à droite puis continuation vers la droite
            x = CENTER_X + int(arc_x) + extra_pixels
            y = CENTER_Y + int(arc_y)
        else:
            # Straight (sécurisé) : continue vertical vers le haut
            x = CENTER_X
            y = CENTER_Y - int((v.position - INTERSECTION_POS) * SCALE)
    return x, y

# ---------- Update loop ----------
def update():
    # 1) Ajustements de distance
    for v in vehicles:
        v.maintain_distance()

    # 2) Déplacement des véhicules (met à jour position/horiz_progress/turned)
    for v in vehicles:
        v.move(dt=TICK_MS/1000.0, intersection_pos=INTERSECTION_POS)

    # 3) Rendu
    for v in vehicles:
        x, y = map_coords(v)
        canvas.coords(vehicle_shapes[v.id], x-12, y-6, x+12, y+6)
        canvas.coords(vehicle_labels[v.id], x, y-15)
        canvas.itemconfig(vehicle_labels[v.id],
                          text=f"{v.id} | {int(v.speed)} km/h | {v.current_direction}")

    # 4) Planification prochain tick
    root.after(TICK_MS, update)

root.after(500, update)
root.mainloop()