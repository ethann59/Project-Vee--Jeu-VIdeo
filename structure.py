Plateau = [[]]

class Joueur:
    nom = ""
    pv = 0 # Points de vie
    pam = 0 # Points d'armure
    patt = 0 # Points d'attaque
    gold = 0 # Or
    inventaire = [] # Inventaire
    arme = [] # Arme
    
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
    arme = [] # Arme
    
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


class Object: #On va définir les objets (armes, armures, potions, etc...)
    nom = ""
    pam = 0 # Si l'objet est une armure, il aura des points d'armure
    pam_temp = False # Si l'objet est une bulle de protection, il permet d'indiquer au jeu si les points sont temporaires ou non
    patt = 0 # Si l'objet est une arme, il aura des points d'attaque
        

class Market_Stock: #On va définir ce que il aura sur le marché (armes, armures, potions, etc...)
    # A faire
    pass