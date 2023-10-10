from __future__ import annotations
        
#J'ai pas encore décidé concernant le marché de comment on le gère

# Pour les parties personnalités, je vais commencer à écrire une classe on verra si on a le temps de l'implémenter
# Mais on peut l'utiliser pour les parties normales aussi (enfin il a des choses que on va jamais utiliser mais bon)
class game_settings:
    def __init__(self):
        self.nb_player = 0 # Permet de changer le nombre de joueurs
        self.police_active = True # Si la police est active
        self.police_multiplier = 1 # Permet de changer la puissance de la police (1 = normal, 2 = double, 0.5 = moitié)
        self.fuite_active = True # Si la fuite est active
        self.object_active = True # Si les objets et le marché est actif pour plus de difficultés
        self.hospital_active = True # Si l'hopital est actif
        self.pvp_active = True # Si le pvp est actif
        self.pv_player = 100 # Permet de changer les pv du joueur
        self.pam_player = 0 # Permet de changer les points d'armure du joueur au lancement de la partie
        self.patt_player = 10 # Permet de changer les points d'attaque du joueur au lancement de la partie
        self.gold_player = 0 # Permet de changer l'or du joueur au lancement de la partie
        self.nb_player = 1 # Permet de changer le nombre de joueurs
        self.enemy_power = 1 # Permet de changer la puissance des ennemis (1 = normal, 2 = double, 0.5 = moitié)
        self.hospital_price = 100 # Permet de changer le prix de l'hopital
        self.time_limit = (10 * 60) # Permet de changer le temps limite de la partie (en minutes)
        self.time_limit_active = True # Si le temps limite est actif
    
        # Coder les méthodes pour changer les paramètres

# Partie réservé au calcul des scores. Elle sont basés sur les points de vie restants, l'or mais aussi les ennemis tués, les items de quetes ramassés, etc...

# Je devrais pas faire un dictionnaire ?
score_panel = [["Points de vie restants", 0], # Dépend des points de vie restants
               ["Or", 0], # Dépend de l'or (voire si il faut nerf ce compteur)
               # ["Ennemis tués", 20], # ça sera calculé en fonction de leur vie voilà !
               ["Items de quêtes ramassés", 150], # Dépend du nombre d'items de quêtes ramassés
               ["Boss final vaincu", 250]] 