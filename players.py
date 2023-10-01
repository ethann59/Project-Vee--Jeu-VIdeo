from __future__ import annotations

from objects import *
from settings import game_settings
from place_data import plateau_info
import pygame

class Joueur():    
    def __init__(self):
        self.nom = "Joueur"
        self.pv = 100
        self.pam = 0
        self.pam_temp_duree = 0
        self.patt = 10
        self.gold = 0
        self.inventaire = []
        self.arme = ["Simple pistolet"]
        self.Score = 0
        self.Timer = 0
        self.case = 0 # refaire le système pour prendre en compte les chevauchements // Ou juste modifier un peu l’affichage
        self.coords = plateau_info[self.case]["x"], plateau_info[self.case]["y"] # Le but ici est de pouvoir modifier les coordonnées en fonction de la case et des joueurs dessus
        self.proba_police = 0.2
        self.image = None
    
    def setNom(self : Joueur, nom : str) :
        self.nom = nom
        
    def setArme(self : Joueur, arme : str, patt : int, proba : int) :
        self.arme = arme
        self.patt = patt
        self.proba_police = proba
        
    def setPam(self : Joueur, pam : int) :
        self.pam = pam
        
    def addGold(self : Joueur, gold : int) :
        self.gold += gold
        
    def addScore(self : Joueur, score : int) :
        self.Score += score
        
    def setTimer(self : Joueur, timer : int) :
        self.Timer = timer
        
    def addTimer(self : Joueur, timer : int) :
        self.Timer += timer
        
    def addObjet(self : Joueur, objet : GenericObject) :
        self.inventaire.append(objet)
        
    def delObjet(self : Joueur, objet : GenericObject) :
        self.inventaire.remove(objet)
        
    def addPv(self : Joueur, pv : int) :
        self.pv += pv
        
    # Il faudra prendre en charge les gros cases ainsi que si il y a plus de 2 joueurs sur la même case + A corriger
        
    def setCase(self : Joueur, case : int, plateau : dict) :
        if self in plateau[self.case]["joueurs"] :
            plateau[self.case]["joueurs"].remove(self)
        plateau[case]["joueurs"].append(self)
        self.case = case
        if len(plateau_info[self.case]["joueurs"]) > 0 : # Si il y a déjà un joueur sur la case, on décale le joueur de 10 pixels vers le bas
            self.coords = plateau_info[self.case]["x"], plateau_info[self.case]["y"] + 10
    
    def addCase(self : Joueur, case : int, plateau : dict) :
        if self in plateau[self.case]["joueurs"] :
            plateau[self.case]["joueurs"].remove(self)
        plateau[case]["joueurs"].append(self)
        if self.case + case > 26 :
            self.case = self.case + case - 26
            self.addGold(100)
        else :
            self.case += case
        if len(plateau_info[self.case]["joueurs"]) > 0 : # Si il y a déjà un joueur sur la case, on décale le joueur de 10 pixels vers le bas
            self.coords = plateau_info[self.case]["x"], plateau_info[self.case]["y"] + 10

        
    def setProbapolice(self : Joueur, proba : int) :
        self.proba_police = proba
        
    def setImage(self : Joueur, image : str) :
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (36, 36))
        
