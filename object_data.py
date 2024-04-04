#On stockera les ennemis ce fichier

import settings as gc
from objects import *

GenericObject.ItemTest = GenericObject()

# Surement nerf les prix

PotionVie = Potion()
PotionVie.setNom("Potion de vie")
PotionVie.setPrix(30)
PotionVie.setDescription("Une potion qui rend 50 points de vie")
PotionVie.setPV(50)

ChampDeForce = TempShield()
ChampDeForce.setNom("Champ de force")
ChampDeForce.setPrix(50)
ChampDeForce.setDefense(50)
ChampDeForce.setDescription("Un champ de force qui vous protège pendant 3 tours")


GrenadeFlashe = GrenadeFlash()
GrenadeFlashe.setNom("Grenade flash")
GrenadeFlashe.setPrix(80)
GrenadeFlashe.setDescription("Une grenade qui aveugle l'ennemi pendant 2 tours")

PistoletMitrailleur = Arme()
PistoletMitrailleur.setNom("Pistolet mitrailleur")
PistoletMitrailleur.setPrix(100)
PistoletMitrailleur.setDescription("Une arme qui inflige 10 points de dégats")
PistoletMitrailleur.setDegats(30)
PistoletMitrailleur.setPoliceProba(0.3)

GiletParBalle = Armure()
GiletParBalle.setNom("Gilet protecteur")
GiletParBalle.setPrix(100)
GiletParBalle.setDescription("Un gilet qui réduit les dégats de 10 points")
GiletParBalle.setDefense(25)

items_disponibles = [PotionVie, ChampDeForce, GrenadeFlashe, PistoletMitrailleur, GiletParBalle]

# Penser à cacher les objets uniques pour éviter les achats en double


# Items de quete

ItemQuete1 = QuestObject()
ItemQuete1.setNom("Cristal mystérieux")
ItemQuete1.setPrix(0)
ItemQuete1.setDescription("Un cristal mystérieux qui semble avoir une grande valeur")
ItemQuete1.setId(1)

ItemQuete2 = QuestObject()
ItemQuete2.setNom("Parchemin Enchanté")
ItemQuete2.setPrix(0)
ItemQuete2.setDescription("Un vieux parchemin couvert de runes magiques.")
ItemQuete2.setId(2)

ItemQuete3 = QuestObject()
ItemQuete3.setNom("Amulette vide")
ItemQuete3.setPrix(0)
ItemQuete3.setDescription("Une amulette vide qui semble pouvoir contenir quelque chose.")

ItemQuete4 = QuestObject()
ItemQuete4.setNom("La Larme de la Lune")
ItemQuete4.setPrix(0)
ItemQuete4.setDescription("Une larme de la lune qui semble avoir une grande valeur.")
ItemQuete4.setId(4)

