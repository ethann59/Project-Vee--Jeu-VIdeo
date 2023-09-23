from __future__ import annotations
from objects import Object
import pygame

class Ennemi:
    def __init__(self): # Temporaire, à voir pour créer les différents ennemis
        self.nom = "Ennemi"
        self.pv = 100
        self.pam = 0
        self.patt = 10
        self.gold = 0
        self.inventaire = []
        self.quest_object = []
        self.final_boss = False
        self.arme = ["Simple pistolet"]
        self.coords = [0,0] # Uniquement pour James et ses protégés // Si c'est à 0,0, il n'apparait pas
        self.killed = False # Uniquement pour James et ses protégés // Si c'est True, il n'apparait plus
        self.image = None
        self.spawn_taux = 0
        
    def setNom(self : Ennemi, nom : str) :
        self.nom = nom
        
    def setArme(self : Ennemi, arme : str, patt : int) :
        self.arme = arme
        self.patt = patt
        
    def setPam(self : Ennemi, pam : int) :
        self.pam = pam
        
    def addGold(self : Ennemi, gold : int) :
        self.gold += gold
        
    def addObjet(self : Ennemi, objet : Object) :
        self.inventaire.append(objet)
        
    def delObjet(self : Ennemi, objet : Object) :
        self.inventaire.remove(objet)
        
    def addPv(self : Ennemi, pv : int) :
        self.pv += pv
        
    def setObjetQuete(self : Ennemi, objet : Object) :
        self.quest_object.append(objet)
        
    def setFinalBoss(self : Ennemi, final_boss : bool) :
        self.final_boss = final_boss
        
    def setCooords(self : Ennemi, coords : list) :
        self.coords = coords
        
    def setImage(self : Ennemi, image : str) :
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (36, 36))
        
