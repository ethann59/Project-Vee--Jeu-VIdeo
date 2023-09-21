from __future__ import annotations
from objects import Object

class Ennemi:
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
        
