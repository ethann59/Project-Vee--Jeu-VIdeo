from __future__ import annotations

class Object: #On va définir les objets (armes, armures, potions, etc...) Voir si il y a pas une autre méthode pour stocker les informations
    def __init__(self):
        self.nom = ""
        self.pam = 0 # Si l'objet est une armure, il aura des points d'armure
        self.pam_temp = False # Si l'objet est un champ de force, il permet d'indiquer au jeu si les points sont temporaires ou non
        self.patt = 0 # Si l'objet est une arme, il aura des points d'attaque
        self.pv = 0 # Si l'objet est une potion, il aura des points de vie (ça sera soit un pourçentage soit un nombre fixe)
        self.police_proba = 0 # Si l'objet est une arme, il aura une probabilité de faire apparaître la police (ça sera un chiffre entre 0 et 1)
        self.fuite_proba = 0 # Si l'objet est une grenade flash, il aura une probabilité de faire fuir l'ennemi (ça sera un chiffre entre 0 et 1)
    
    def setNom(self : Object, nom : str) :
        self.nom = nom
        
    def setPam(self : Object, pam : int) :
        self.pam = pam
        
    def setPatt(self : Object, patt : int) :
        self.patt = patt
        
    def setPv(self : Object, pv : int) :
        self.pv = pv
    
    def setPoliceProba(self : Object, police_proba : float) :
        self.police_proba = police_proba
    
    def setFuiteProba(self : Object, fuite_proba : float) :
        self.fuite_proba = fuite_proba
        