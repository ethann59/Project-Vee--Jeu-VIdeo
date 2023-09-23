#On stockera les ennemis ce fichier
import ennemis as en
import pygame


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
en.Ennemi.voleur.image = pygame.image.load("img/sprites/voleur.png")
en.Ennemi.voleur.image = pygame.transform.scale(en.Ennemi.voleur.image, (36, 36))

voleur = en.Ennemi.voleur # Pour l'appeler plus facilement

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
en.Ennemi.delinquant.image = pygame.image.load("img/sprites/delinquant.png")
en.Ennemi.delinquant.image = pygame.transform.scale(en.Ennemi.delinquant.image, (36, 36))

delinquant = en.Ennemi.delinquant


en.Ennemi.ap_James1 = en.Ennemi()
en.Ennemi.ap_James1.nom = "Sandrine la sorcière"
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
en.Ennemi.ap_James1.image = pygame.image.load("img/sprites/sandrine-apjames1.png")
en.Ennemi.ap_James1.image = pygame.transform.scale(en.Ennemi.ap_James1.image, (36, 36))

ap_James1 = en.Ennemi.ap_James1


en.Ennemi.ap_James2 = en.Ennemi()
en.Ennemi.ap_James2.nom = "Luc le sorcier"
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
en.Ennemi.ap_James2.image = pygame.image.load("img/sprites/luc-apjames2.png")
en.Ennemi.ap_James2.image = pygame.transform.scale(en.Ennemi.ap_James2.image, (36, 36))


ap_James2 = en.Ennemi.ap_James2

en.Ennemi.ap_James3 = en.Ennemi()
en.Ennemi.ap_James3.nom = "Augustin-Pierre le sorcier"
en.Ennemi.ap_James3.pv = 50
en.Ennemi.ap_James3.pam = 0
en.Ennemi.ap_James3.patt = 20
en.Ennemi.ap_James3.gold = 250
en.Ennemi.ap_James3.inventaire = []
en.Ennemi.ap_James3.quest_object = ["Item de quête 3"]
en.Ennemi.ap_James3.final_boss = False
en.Ennemi.ap_James3.arme = ["Livre de magie"] # Peut etre les faire varier
en.Ennemi.ap_James3.spawn_taux = 0
en.Ennemi.ap_James3.coords = [0,0] # A définir
en.Ennemi.ap_James3.killed = False
en.Ennemi.ap_James3.image = pygame.image.load("img/sprites/augustin-apjames3.png")
en.Ennemi.ap_James3.image = pygame.transform.scale(en.Ennemi.ap_James3.image, (36, 36))

ap_James3 = en.Ennemi.ap_James3

en.Ennemi.ap_James4 = en.Ennemi()
en.Ennemi.ap_James4.nom = "Tolkien le sorcier"
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
en.Ennemi.ap_James4.image = pygame.image.load("img/sprites/tolkien-apjames4.png")
en.Ennemi.ap_James4.image = pygame.transform.scale(en.Ennemi.ap_James4.image, (36, 36))

ap_James4 = en.Ennemi.ap_James4


en.Ennemi.james = en.Ennemi()
en.Ennemi.james.nom = "James"
# Valeur à changer selon le PDF
en.Ennemi.james.pv = 150
en.Ennemi.james.pam = 25
en.Ennemi.james.patt = 30
en.Ennemi.james.gold = 200
en.Ennemi.james.inventaire = []
en.Ennemi.james.quest_object = []
en.Ennemi.james.final_boss = True
en.Ennemi.james.arme = ["Livre de magie"]
en.Ennemi.james.spawn_taux = 0
en.Ennemi.james.coords = [0,0] # A définir
en.Ennemi.james.killed = False
en.Ennemi.james.image = pygame.image.load("img/sprites/james.png")
en.Ennemi.james.image = pygame.transform.scale(en.Ennemi.james.image, (36, 36))

james = en.Ennemi.james

random_enemy_dict = {"Voleur" : en.Ennemi.voleur, "Delinquant" : en.Ennemi.delinquant}