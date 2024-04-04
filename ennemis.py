from __future__ import annotations
from objects import *
import pygame

class Ennemi:
    def __init__(self):
        self.nom = "Ennemi"
        self.pv = 100
        self.pam = 0
        self.patt = 10
        self.gold = 0
        self.inventaire = []
        self.arme = ["Simple pistolet"]
        self.image = None
        
    def setNom(self : Ennemi, nom : str) :
        self.nom = nom
        
    def setArme(self : Ennemi, arme : str, patt : int) :
        self.arme = arme
        self.patt = patt
        
    def setPam(self : Ennemi, pam : int) :
        self.pam = pam
        
    def addGold(self : Ennemi, gold : int) :
        self.gold += gold
        
    def addObjet(self : Ennemi, objet : GenericObject) :
        self.inventaire.append(objet)
        
    def delObjet(self : Ennemi, objet : GenericObject) :
        self.inventaire.remove(objet)
        
    def addPv(self : Ennemi, pv : int) :
        self.pv += pv
        
    def setPv(self : Ennemi, pv : int) :
        self.pv = pv
        
    def setImage(self : Ennemi, image : str) :
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (36, 36))
    
class EnnemiImportant(Ennemi): # Uniquement pour James et ses protégés
    def __init__(self):
        super().__init__()
        self.quest_object = None
        self.final_boss = False
        self.case = 0
        self.killed = False # Si c'est True, il n'apparait plus
                
    def setObjetQuete(self : EnnemiImportant, objet : GenericObject) :
        self.quest_object.append(objet)
    
    def setFinalBoss(self : EnnemiImportant, final_boss : bool) :
        self.final_boss = final_boss
    
    def setCase(self : EnnemiImportant, case : int) :
        self.case = case

    def setKilled(self : EnnemiImportant, killed : bool) :
        self.killed = killed