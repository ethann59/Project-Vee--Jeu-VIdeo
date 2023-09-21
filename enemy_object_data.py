#On stockera les ennemis et les objets dans ce fichier
#Le nom du fichier peut changer

import game_settings as gc

enemy_list = []

gc.Ennemi.test = gc.Ennemi()


# A corriger
gc.Ennemi.voleur = gc.Ennemi(
    nom = "Voleur",
    pv = 15,
    pam = 0,
    patt = 10,
    gold = 25,
    inventaire = [],
    quest_object = [],
    final_boss = False,
    arme = ["Couteau"],
    spawn_taux = 0.5
)

gc.Ennemi.delinquant = gc.Ennemi(
    nom = "Delinquant",
    pv = 25,
    pam = 0,
    patt = 15,
    gold = 50,
    inventaire = [],
    quest_object = [],
    final_boss = False,
    arme = ["Simple pistolet"],
    spawn_taux = 0.3
)

gc.Ennemi.ap_james = gc.Ennemi( # Il faudra varier les noms en fonction des items mais ça fait un model
    nom = "Protégé de James",
    pv = 50,
    pam = 10,
    patt = 20,
    gold = 100,
    inventaire = [],
    quest_object = ["Item de quête"], #Il faudra inventer des items de quetes
    final_boss = False,
    arme = ["Livre de magie"],
    spawn_taux = 0.1 # Il faudrait les placer sur la carte non ?
)
    