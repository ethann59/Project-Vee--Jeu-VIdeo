Plateau = []

def inialize_plateau(n):
    for i in range(n):
        Plateau.append([n, ""])


class Joueur:
    nom = ""
    pv = 0 # Points de vie
    pam = 0 # Points d'armure
    patt = 0 # Points d'attaque
    gold = 0 # Or
    inventaire = [] # Inventaire
    arme = [] # Arme
    Score = 0 # Score
    Timer = 0 # Timer (dans le cas de la partie démo la partie est limité à 15 minutes donc on va mettre un timer par tour de 1 minute max)
    
    def __init__(self):
        self.nom = "Joueur"
        self.pv = 100
        self.pam = 0
        self.patt = 10
        self.gold = 0
        self.inventaire = []
        self.arme = ["Simple pistolet"]
        

class Ennemi:
    nom = ""
    pv = 0 # Points de vie
    pam = 0 # Points d'armure
    patt = 0 # Points d'attaque
    gold = 0 # Or qui sera donné au joueur si meurt
    inventaire = [] # Je sais pas si ça sera utilisé mais ça peut être utile si on veut qu'il se soigne par exemple
    quest_object = [] # Objet de quête qui sera donné au joueur si meurt (si il en a un)
    final_boss = False # Si c'est le boss final (ça permet de désactiver l'evenement "Police" ou la fuite)
    arme = [] # Arme (pour le jeu)
    spawn_taux = 0 # Taux de spawn (pour le jeu) (ça sera un chiffre entre 0 et 1)
    
    def __init__(self): #Temporaire, à voir pour créer les différents ennemis
        self.nom = "Ennemi"
        self.pv = 100
        self.pam = 0
        self.patt = 10
        self.gold = 0
        self.inventaire = []
        self.quest_object = []
        self.final_boss = False
        self.arme = ["Simple pistolet"]
        


class Object: #On va définir les objets (armes, armures, potions, etc...) Voir si il y a pas une autre méthode pour stocker les informations
    nom = ""
    pam = 0 # Si l'objet est une armure, il aura des points d'armure
    pam_temp = False # Si l'objet est un champ de force, il permet d'indiquer au jeu si les points sont temporaires ou non
    patt = 0 # Si l'objet est une arme, il aura des points d'attaque
    pv = 0 # Si l'objet est une potion, il aura des points de vie (ça sera soit un pourçentage soit un nombre fixe)
    police_proba = 0 # Si l'objet est une arme, il aura une probabilité de faire apparaître la police (ça sera un chiffre entre 0 et 1)
    fuite_proba = 0 # Si l'objet est une grenade flash, il aura une probabilité de faire fuir l'ennemi (ça sera un chiffre entre 0 et 1)
    
    
    
        

#J'ai pas encore décidé concernant le marché de comment on le gère

# Pour les parties personnalités, je vais commencer à écrire une classe on verra si on a le temps de l'implémenter
# Mais on peut l'utiliser pour les parties normales aussi (enfin il a des choses que on va jamais utiliser mais bon)
class game_settings:
    nb_player = 1 # Permet de changer le nombre de joueurs
    police_active = True # Si la police est active
    fuite_active = True # Si la fuite est active
    object_active = True # Si les objets et le marché est actif pour plus de difficultés
    hospital_active = True # Si l'hopital est actif
    parc_active = True # Si le parc est actif
    pvp_active = True # Si le pvp est actif
    pv_player = 100 # Permet de changer les pv du joueur
    pam_player = 0 # Permet de changer les points d'armure du joueur au lancement de la partie
    patt_player = 10 # Permet de changer les points d'attaque du joueur au lancement de la partie
    gold_player = 0 # Permet de changer l'or du joueur au lancement de la partie
    nb_player = 1 # Permet de changer le nombre de joueurs
    enemy_power = 1 # Permet de changer la puissance des ennemis (1 = normal, 2 = double, 0.5 = moitié)
    hospital_price = 10 # Permet de changer le prix de l'hopital
    time_limit = 15 # Permet de changer le temps limite de la partie (en minutes), si elle est à 0, la partie n'est pas limité dans le temps
    
    
# Partie réservé au calcul des scores. Elle sont basés sur les points de vie restants, l'or mais aussi les ennemis tués, les items de quetes ramassés, etc...

# Je devrais pas faire un dictionnaire ?
score_panel = [["Points de vie restants", 0], # Dépend des points de vie restants
               ["Or", 0], # Dépend de l'or (voire si il faut nerf ce compteur)
               # ["Ennemis tués", 20], # ça sera calculé en fonction de leur vie voilà !
               ["Items de quêtes ramassés", 150], # Dépend du nombre d'items de quêtes ramassés
               ["Boss final vaincu", 250]] 