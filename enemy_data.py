#On stockera les ennemis ce fichier

import settings as gc

random_enemy_dict = {"Voleur" : gc.Ennemi.voleur, "Delinquant" : gc.Ennemi.delinquant}

gc.Ennemi.test = gc.Ennemi()


# A corriger
gc.Ennemi.voleur = gc.Ennemi()
gc.Ennemi.voleur.nom = "Voleur"
gc.Ennemi.voleur.pv = 15
gc.Ennemi.voleur.pam = 0
gc.Ennemi.voleur.patt = 10
gc.Ennemi.voleur.gold = 25
gc.Ennemi.voleur.inventaire = []
gc.Ennemi.voleur.quest_object = []
gc.Ennemi.voleur.final_boss = False
gc.Ennemi.voleur.arme = ["Couteau"]
gc.Ennemi.voleur.spawn_taux = 0.5
gc.Ennemi.voleur.coords = [0,0]
gc.Ennemi.voleur.killed = False

gc.Ennemi.delinquant = gc.Ennemi()
gc.Ennemi.delinquant.nom = "Delinquant"
gc.Ennemi.delinquant.pv = 25
gc.Ennemi.delinquant.pam = 0
gc.Ennemi.delinquant.patt = 15
gc.Ennemi.delinquant.gold = 50
gc.Ennemi.delinquant.inventaire = []
gc.Ennemi.delinquant.quest_object = []
gc.Ennemi.delinquant.final_boss = False
gc.Ennemi.delinquant.arme = ["Simple pistolet"]
gc.Ennemi.delinquant.spawn_taux = 0.3
gc.Ennemi.delinquant.coords = [0,0]
gc.Ennemi.delinquant.killed = False


gc.Ennemi.ap_James1 = gc.Ennemi()
gc.Ennemi.ap_James1.nom = "Protégé de James 1"
gc.Ennemi.ap_James1.pv = 50
gc.Ennemi.ap_James1.pam = 0
gc.Ennemi.ap_James1.patt = 20
gc.Ennemi.ap_James1.gold = 100
gc.Ennemi.ap_James1.inventaire = []
gc.Ennemi.ap_James1.quest_object = ["Item de quête 1"]
gc.Ennemi.ap_James1.final_boss = False
gc.Ennemi.ap_James1.arme = ["Livre de magie"]
gc.Ennemi.ap_James1.spawn_taux = 0
gc.Ennemi.ap_James1.coords = [0,0] # A définir
gc.Ennemi.ap_James1.killed = False


gc.Ennemi.ap_James2 = gc.Ennemi()
gc.Ennemi.ap_James2.nom = "Protégé de James 2"
gc.Ennemi.ap_James2.pv = 50
gc.Ennemi.ap_James2.pam = 0
gc.Ennemi.ap_James2.patt = 20
gc.Ennemi.ap_James2.gold = 100
gc.Ennemi.ap_James2.inventaire = []
gc.Ennemi.ap_James2.quest_object = ["Item de quête 2"]
gc.Ennemi.ap_James2.final_boss = False
gc.Ennemi.ap_James2.arme = ["Livre de magie"] # Peut etre les faire varier
gc.Ennemi.ap_James2.spawn_taux = 0
gc.Ennemi.ap_James2.coords = [0,0] # A définir
gc.Ennemi.ap_James2.killed = False

gc.Ennemi.ap_James3 = gc.Ennemi()
gc.Ennemi.ap_James3.nom = "Protégé de James 3"
gc.Ennemi.ap_James3.pv = 50
gc.Ennemi.ap_James3.pam = 0
gc.Ennemi.ap_James3.patt = 20
gc.Ennemi.ap_James3.gold = 100
gc.Ennemi.ap_James3.inventaire = []
gc.Ennemi.ap_James3.quest_object = ["Item de quête 3"]
gc.Ennemi.ap_James3.final_boss = False
gc.Ennemi.ap_James3.arme = ["Livre de magie"] # Peut etre les faire varier
gc.Ennemi.ap_James3.spawn_taux = 0
gc.Ennemi.ap_James3.coords = [0,0] # A définir
gc.Ennemi.ap_James3.killed = False

gc.Ennemi.ap_James4 = gc.Ennemi()
gc.Ennemi.ap_James4.nom = "Protégé de James 3"
gc.Ennemi.ap_James4.pv = 50
gc.Ennemi.ap_James4.pam = 0
gc.Ennemi.ap_James4.patt = 20
gc.Ennemi.ap_James4.gold = 100
gc.Ennemi.ap_James4.inventaire = []
gc.Ennemi.ap_James4.quest_object = ["Item de quête 3"]
gc.Ennemi.ap_James4.final_boss = False
gc.Ennemi.ap_James4.arme = ["Livre de magie"] # Peut etre les faire varier
gc.Ennemi.ap_James4.spawn_taux = 0
gc.Ennemi.ap_James4.coords = [0,0] # A définir
gc.Ennemi.ap_James4.killed = False


gc.Ennemi.james = gc.Ennemi()
gc.Ennemi.james.nom = "James"
# Valeur à changer selon le PDF
gc.Ennemi.james.pv = 100
gc.Ennemi.james.pam = 0
gc.Ennemi.james.patt = 30
gc.Ennemi.james.gold = 200
gc.Ennemi.james.inventaire = []
gc.Ennemi.james.quest_object = []
gc.Ennemi.james.final_boss = True
gc.Ennemi.james.arme = ["Livre de magie"]
gc.Ennemi.james.spawn_taux = 0
gc.Ennemi.james.coords = [0,0] # A définir
gc.Ennemi.james.killed = False
