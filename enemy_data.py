#On stockera les ennemis ce fichier
import ennemis as en


en.Ennemi.test = en.Ennemi()

en.Ennemi.voleur = en.Ennemi()
en.Ennemi.voleur.nom = "Voleur"
en.Ennemi.voleur.pv = 15
en.Ennemi.voleur.pam = 0
en.Ennemi.voleur.patt = 10
en.Ennemi.voleur.gold = 25
en.Ennemi.voleur.inventaire = []
en.Ennemi.voleur.quest_object = []
en.Ennemi.voleur.final_boss = False
en.Ennemi.voleur.arme = ["Couteau"]
en.Ennemi.voleur.spawn_taux = 0.5
en.Ennemi.voleur.coords = [0,0]
en.Ennemi.voleur.killed = False

en.Ennemi.delinquant = en.Ennemi()
en.Ennemi.delinquant.nom = "Delinquant"
en.Ennemi.delinquant.pv = 25
en.Ennemi.delinquant.pam = 0
en.Ennemi.delinquant.patt = 15
en.Ennemi.delinquant.gold = 50
en.Ennemi.delinquant.inventaire = []
en.Ennemi.delinquant.quest_object = []
en.Ennemi.delinquant.final_boss = False
en.Ennemi.delinquant.arme = ["Simple pistolet"]
en.Ennemi.delinquant.spawn_taux = 0.3
en.Ennemi.delinquant.coords = [0,0]
en.Ennemi.delinquant.killed = False


en.Ennemi.ap_James1 = en.Ennemi()
en.Ennemi.ap_James1.nom = "Protégé de James 1"
en.Ennemi.ap_James1.pv = 50
en.Ennemi.ap_James1.pam = 0
en.Ennemi.ap_James1.patt = 20
en.Ennemi.ap_James1.gold = 100
en.Ennemi.ap_James1.inventaire = []
en.Ennemi.ap_James1.quest_object = ["Item de quête 1"]
en.Ennemi.ap_James1.final_boss = False
en.Ennemi.ap_James1.arme = ["Livre de magie"]
en.Ennemi.ap_James1.spawn_taux = 0
en.Ennemi.ap_James1.coords = [0,0] # A définir
en.Ennemi.ap_James1.killed = False


en.Ennemi.ap_James2 = en.Ennemi()
en.Ennemi.ap_James2.nom = "Protégé de James 2"
en.Ennemi.ap_James2.pv = 50
en.Ennemi.ap_James2.pam = 0
en.Ennemi.ap_James2.patt = 20
en.Ennemi.ap_James2.gold = 100
en.Ennemi.ap_James2.inventaire = []
en.Ennemi.ap_James2.quest_object = ["Item de quête 2"]
en.Ennemi.ap_James2.final_boss = False
en.Ennemi.ap_James2.arme = ["Livre de magie"] # Peut etre les faire varier
en.Ennemi.ap_James2.spawn_taux = 0
en.Ennemi.ap_James2.coords = [0,0] # A définir
en.Ennemi.ap_James2.killed = False

en.Ennemi.ap_James3 = en.Ennemi()
en.Ennemi.ap_James3.nom = "Protégé de James 3"
en.Ennemi.ap_James3.pv = 50
en.Ennemi.ap_James3.pam = 0
en.Ennemi.ap_James3.patt = 20
en.Ennemi.ap_James3.gold = 100
en.Ennemi.ap_James3.inventaire = []
en.Ennemi.ap_James3.quest_object = ["Item de quête 3"]
en.Ennemi.ap_James3.final_boss = False
en.Ennemi.ap_James3.arme = ["Livre de magie"] # Peut etre les faire varier
en.Ennemi.ap_James3.spawn_taux = 0
en.Ennemi.ap_James3.coords = [0,0] # A définir
en.Ennemi.ap_James3.killed = False

en.Ennemi.ap_James4 = en.Ennemi()
en.Ennemi.ap_James4.nom = "Protégé de James 3"
en.Ennemi.ap_James4.pv = 50
en.Ennemi.ap_James4.pam = 0
en.Ennemi.ap_James4.patt = 20
en.Ennemi.ap_James4.gold = 100
en.Ennemi.ap_James4.inventaire = []
en.Ennemi.ap_James4.quest_object = ["Item de quête 3"]
en.Ennemi.ap_James4.final_boss = False
en.Ennemi.ap_James4.arme = ["Livre de magie"] # Peut etre les faire varier
en.Ennemi.ap_James4.spawn_taux = 0
en.Ennemi.ap_James4.coords = [0,0] # A définir
en.Ennemi.ap_James4.killed = False


en.Ennemi.james = en.Ennemi()
en.Ennemi.james.nom = "James"
# Valeur à changer selon le PDF
en.Ennemi.james.pv = 100
en.Ennemi.james.pam = 0
en.Ennemi.james.patt = 30
en.Ennemi.james.gold = 200
en.Ennemi.james.inventaire = []
en.Ennemi.james.quest_object = []
en.Ennemi.james.final_boss = True
en.Ennemi.james.arme = ["Livre de magie"]
en.Ennemi.james.spawn_taux = 0
en.Ennemi.james.coords = [0,0] # A définir
en.Ennemi.james.killed = False

random_enemy_dict = {"Voleur" : en.Ennemi.voleur, "Delinquant" : en.Ennemi.delinquant}