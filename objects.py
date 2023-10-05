from __future__ import annotations
import pygame

class GenericObject: #On va définir les objets (armes, armures, potions, etc...)
    def __init__(self):
        self.nom = ""
        self.prix = 0
        self.description = ""
        self.image = None
        
    def setNom(self : GenericObject, nom : str) :
        self.nom = nom
        
    def setPrix(self : GenericObject, prix : int) :
        self.prix = prix
    
    def setDescription(self : GenericObject, description : str) :
        self.description = description
    
    def setImage(self: GenericObject, image: str) :
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (36, 36)) #On redimensionne l'image en fonction
        
class Arme(GenericObject):
    def __init__(self):
        super().__init__()
        self.patt = 0
        self.Police_Proba = 0 # Probabilité de tomber sur la police à cause de cette arme
        #self.critique = 0 #Une idée de Copilot on pourrait le garder pour le système de combat
        
    def setDegats(self : Arme, degats : int) :
        self.degats = degats
        
    def setPoliceProba(self : Arme, Police_Proba : int) :
        self.Police_Proba = Police_Proba
        
    #def setCritique(self : Arme, critique : int) :
    #    self.critique = critique
    
class GrenadeFlash(Arme):
    def __init__(self):
        super().__init__()
        self.turn_pass = True
    
class Armure(GenericObject):
    def __init__(self):
        super().__init__()
        self.pam = 0
        
    def setDefense(self : Armure, defense : int) :
        self.pam = defense
        
class Potion(GenericObject):
    def __init__(self):
        super().__init__()
        self.pv = 0
        
    def setPV(self : Potion, pv : int) :
        self.pv = pv
        
class TempShield(GenericObject):
    def __init__(self):
        super().__init__()
        self.pdef = 0
        self.duree = 0
        
    def setDefense(self : TempShield, defense : int) :
        self.defense = defense
        
    def setDuree(self : TempShield, duree : int) :
        self.duree = duree
        
# Peut etre faire une classe pour les objets de quête

class QuestObject(GenericObject):
    def __init__(self):
        super().__init__()
        self.id = 0
        
    def setId(self : QuestObject, id : int) :
        self.id = id