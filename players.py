from __future__ import annotations

from objects import Object

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
        
