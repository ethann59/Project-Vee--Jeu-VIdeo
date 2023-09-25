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
en.Ennemi.voleur.arme = ["Couteau"]
en.Ennemi.voleur.spawn_taux = 0.5
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
en.Ennemi.delinquant.arme = ["Simple pistolet"]
en.Ennemi.delinquant.spawn_taux = 0.3
en.Ennemi.delinquant.image = pygame.image.load("img/sprites/delinquant.png")
en.Ennemi.delinquant.image = pygame.transform.scale(en.Ennemi.delinquant.image, (36, 36))

delinquant = en.Ennemi.delinquant


en.EnnemiImportant.ap_James1 = en.EnnemiImportant()
en.EnnemiImportant.ap_James1.nom = "Sandrine la sorcière"
en.EnnemiImportant.ap_James1.pv = 50
en.EnnemiImportant.ap_James1.pam = 0
en.EnnemiImportant.ap_James1.patt = 20
en.EnnemiImportant.ap_James1.gold = 100
en.EnnemiImportant.ap_James1.inventaire = []
en.EnnemiImportant.ap_James1.quest_object = ["Item de quête 1"]
en.EnnemiImportant.ap_James1.final_boss = False
en.EnnemiImportant.ap_James1.arme = ["Livre de magie"]
en.EnnemiImportant.ap_James1.spawn_taux = 0
en.EnnemiImportant.ap_James1.coords = [0,0] # A définir
en.EnnemiImportant.ap_James1.killed = False
en.EnnemiImportant.ap_James1.image = pygame.image.load("img/sprites/sandrine-apjames1.png")
en.EnnemiImportant.ap_James1.image = pygame.transform.scale(en.EnnemiImportant.ap_James1.image, (36, 36))

ap_James1 = en.EnnemiImportant.ap_James1


en.EnnemiImportant.ap_James2 = en.Ennemi()
en.EnnemiImportant.ap_James2.nom = "Luc le sorcier"
en.EnnemiImportant.ap_James2.pv = 50
en.EnnemiImportant.ap_James2.pam = 0
en.EnnemiImportant.ap_James2.patt = 20
en.EnnemiImportant.ap_James2.gold = 100
en.EnnemiImportant.ap_James2.inventaire = []
en.EnnemiImportant.ap_James2.quest_object = ["Item de quête 2"]
en.EnnemiImportant.ap_James2.final_boss = False
en.EnnemiImportant.ap_James2.arme = ["Livre de magie"] # Peut etre les faire varier
en.EnnemiImportant.ap_James2.spawn_taux = 0
en.EnnemiImportant.ap_James2.coords = [0,0] # A définir
en.EnnemiImportant.ap_James2.killed = False
en.EnnemiImportant.ap_James2.image = pygame.image.load("img/sprites/luc-apjames2.png")
en.EnnemiImportant.ap_James2.image = pygame.transform.scale(en.EnnemiImportant.ap_James2.image, (36, 36))


ap_James2 = en.EnnemiImportant.ap_James2

en.EnnemiImportant.ap_James3 = en.Ennemi()
en.EnnemiImportant.ap_James3.nom = "Augustin-Pierre le sorcier"
en.EnnemiImportant.ap_James3.pv = 50
en.EnnemiImportant.ap_James3.pam = 0
en.EnnemiImportant.ap_James3.patt = 20
en.EnnemiImportant.ap_James3.gold = 250
en.EnnemiImportant.ap_James3.inventaire = []
en.EnnemiImportant.ap_James3.quest_object = ["Item de quête 3"]
en.EnnemiImportant.ap_James3.final_boss = False
en.EnnemiImportant.ap_James3.arme = ["Livre de magie"] # Peut etre les faire varier
en.EnnemiImportant.ap_James3.spawn_taux = 0
en.EnnemiImportant.ap_James3.coords = [0,0] # A définir
en.EnnemiImportant.ap_James3.killed = False
en.EnnemiImportant.ap_James3.image = pygame.image.load("img/sprites/augustin-apjames3.png")
en.EnnemiImportant.ap_James3.image = pygame.transform.scale(en.EnnemiImportant.ap_James3.image, (36, 36))

ap_James3 = en.EnnemiImportant.ap_James3

en.EnnemiImportant.ap_James4 = en.Ennemi()
en.EnnemiImportant.ap_James4.nom = "Tolkien le sorcier"
en.EnnemiImportant.ap_James4.pv = 50
en.EnnemiImportant.ap_James4.pam = 0
en.EnnemiImportant.ap_James4.patt = 20
en.EnnemiImportant.ap_James4.gold = 100
en.EnnemiImportant.ap_James4.inventaire = []
en.EnnemiImportant.ap_James4.quest_object = ["Item de quête 3"]
en.EnnemiImportant.ap_James4.final_boss = False
en.EnnemiImportant.ap_James4.arme = ["Livre de magie"] # Peut etre les faire varier
en.EnnemiImportant.ap_James4.spawn_taux = 0
en.EnnemiImportant.ap_James4.coords = [0,0] # A définir
en.EnnemiImportant.ap_James4.killed = False
en.EnnemiImportant.ap_James4.image = pygame.image.load("img/sprites/tolkien-apjames4.png")
en.EnnemiImportant.ap_James4.image = pygame.transform.scale(en.EnnemiImportant.ap_James4.image, (36, 36))

ap_James4 = en.EnnemiImportant.ap_James4


en.EnnemiImportant.james = en.EnnemiImportant()
en.EnnemiImportant.james.nom = "James"
# Valeur à changer selon le PDF
en.EnnemiImportant.james.pv = 150
en.EnnemiImportant.james.pam = 25
en.EnnemiImportant.james.patt = 30
en.EnnemiImportant.james.gold = 200
en.EnnemiImportant.james.inventaire = []
en.EnnemiImportant.james.quest_object = []
en.EnnemiImportant.james.final_boss = True
en.EnnemiImportant.james.arme = ["Livre de magie"]
en.EnnemiImportant.james.spawn_taux = 0
en.EnnemiImportant.james.coords = [0,0] # A définir
en.EnnemiImportant.james.killed = False
en.EnnemiImportant.james.image = pygame.image.load("img/sprites/james.png")
en.EnnemiImportant.james.image = pygame.transform.scale(en.EnnemiImportant.james.image, (36, 36))

james = en.EnnemiImportant.james

random_enemy_dict = {"Voleur" : en.Ennemi.voleur, "Delinquant" : en.Ennemi.delinquant}