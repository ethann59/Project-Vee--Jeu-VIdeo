from __future__ import annotations

from objects import *
from settings import game_settings
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
        self.case = 0
        self.proba_police = 0.1
        self.image = None
        self.ko = False # Si elle est sur True, le joueur n'obtient pas le bonus du départ et est envoyé à l'hôpital. Ça évite que un joueur fait exprès de perdre pour obtenir des golds.
    
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
        
    def setPv(self : Joueur, pv : int) :
        self.pv = pv
        
    def setKo(self : Joueur, ko : bool) :
        self.ko = ko
        
    # Il faudra prendre en charge les gros cases ainsi que si il y a plus de 2 joueurs sur la même case + A corriger
        
    def setCase(self : Joueur, case : int) :
        self.case = case
    
    def addCase(self : Joueur, case : int) :
        if self.case + case > 26 :
            self.case = self.case + case - 26
            if self.ko == True : # Vérifie si le joueur n'a pas été KO précdément
                self.ko = False
            else:
                self.addGold(100)
        else :
            self.case += case

        
    def setProbapolice(self : Joueur, proba : int) :
        self.proba_police = proba
        
    def setImage(self : Joueur, image : str) :
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (36, 36))
        
