# vehicle.py
class Vehicle:
    """
    Vehicle gère :
    - position (distance le long de l'approche verticale)
    - speed (km/h)
    - chosen_direction: "Left", "Right" ou "Straight" (défini dès le départ pour la démo)
    - turned: bool (true quand la voiture a quitté l'approche verticale pour emprunter la trajectoire choisie)
    - horiz_progress: distance parcourue horizontalement après le virage (pour gauche/droite)
    """
    def __init__(self, id, position=0.0, speed=40.0, chosen_direction=None):
        self.id = id
        self.position = float(position)      # distance le long de l'approche (0 -> intersection_pos -> plus loin)
        self.speed = float(speed)            # km/h (utilisé pour la simulation)
        self.max_speed = None
        self.front_vehicle = None
        self.chosen_direction = chosen_direction
        self.turned = False
        self.horiz_progress = 0.0            # utilisé après le virage (pixels / unités)
        self.current_direction = chosen_direction  # pour affichage

    def set_road_speed(self, speed_limit):
        self.max_speed = speed_limit
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def maintain_distance(self):
        if self.front_vehicle and not self.turned:
            # distance en unités de position entre la voiture et celle de devant
            distance = self.front_vehicle.position - self.position
            if distance < 8:  # distance minimale en unités (à ajuster)
                # on ralentit progressivement
                self.speed = min(self.speed, max(5.0, self.front_vehicle.speed - 5.0))

    def move(self, dt=0.2, intersection_pos=100.0):
        """
        dt : facteur temps (sec) pour la simulation de déplacement (contrôle la vitesse d'animation)
        intersection_pos : position où se situe le carrefour
        Retour : tuple (screen_x, screen_y, status) où status peut aider au rendu
        """
        # conversion vitesse -> unité de position par tick (vitesse/10 est empirique)
        step = (self.speed / 10.0) * (dt / 0.2)

        if not self.turned:
            # Approche verticale : avancer vers l'intersection
            self.position += step
            # Si on a atteint ou dépassé l'intersection, on déclenche le virage / continuité
            if self.position >= intersection_pos:
                if self.chosen_direction in ("Left", "Right"):
                    self.turned = True
                    self.horiz_progress = 0.0
                    self.current_direction = self.chosen_direction
                else:
                    # Straight : on continue verticalement, reste current_direction = Straight
                    self.current_direction = "Straight"
        else:
            # Après avoir tourné : on se déplace horizontalement (horiz_progress augmente)
            self.horiz_progress += step
            # on peut éventuellement réduire la vitesse après le virage
            # (ici on garde la même speed, c'est une démo)
        # Retour d'état utile pour le rendu (les coordonnées seront calculées dans main)
        return (self.position, self.horiz_progress, self.turned)