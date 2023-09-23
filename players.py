from __future__ import annotations

from objects import Object
from settings import game_settings
import pygame

class Joueur():    
    def __init__(self):
        self.nom = "Joueur"
        self.pv = 100
        self.pam = 0
        self.patt = 10
        self.gold = 0
        self.inventaire = []
        self.arme = ["Simple pistolet"]
        self.Score = 0
        self.Timer = 0
        self.case = 0
        self.proba_police = 0.2
        self.image = None
    
    def setNom(self : Joueur, nom : str) :
        self.nom = nom
        
    def setArme(self : Joueur, arme : str, patt : int) :
        self.arme = arme
        self.patt = patt
        
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
        
    def addObjet(self : Joueur, objet : Object) :
        self.inventaire.append(objet)
        
    def delObjet(self : Joueur, objet : Object) :
        self.inventaire.remove(objet)
        
    def addPv(self : Joueur, pv : int) :
        self.pv += pv
        
    def setCase(self : Joueur, case : int) :
        self.case = case
        
    def setProbapolice(self : Joueur, proba : int) :
        self.proba_police = proba
        
    def setImage(self : Joueur, image : str) :
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (36, 36))
        
