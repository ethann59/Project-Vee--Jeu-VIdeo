# Importation des modules
import pygame.font
import time, sys, random
# Importation des fichiers
import players, ennemis, objects, settings
import place_data, enemy_data, object_data

# Variables globales

version = "0.0.6"

# Variables de la partie

game_settings = settings.game_settings()
duree_timer = game_settings.time_limit
nb_joueurs = 0


# Variables textuels

pygame.font.init()
font = pygame.font.Font(None, 36)  # Crée une police avec une taille de 36 points (vous pouvez ajuster la taille selon vos besoins)
texte = font.render("Votre texte ici", True, (55, 42, 60))  # Texte blanc avec antialiasing
timer_text = font.render("Temps restant : " + str(duree_timer), True, (55, 42, 60))
inventaire_text = font.render("Inventaire :", True, (55, 42, 60))

# Variables du plateau

Plateau = []
n = 0 # Nombre de cases du plateau - A définir

def inialize_plateau(n):
    for i in range(n):
        Plateau.append([n, ""])
        
# Variables graphiques

plateau_img = pygame.image.load("img/scenes/plateau.jpg")
plateau_img = pygame.transform.scale(plateau_img, (648, 644))

inventaire_img = pygame.image.load("img/scenes/inventaire.png")

# Initialisation de Pygame
pygame.init()

# Configurer la fenêtre
taille_fenetre = (1000,644)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Project Vee - Developement Build " + version)

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
GRIS = (128, 128, 128)
BLEU = (0, 0, 255)

# Fonction graphiques
def dessiner_bouton(x, y, largeur, hauteur, couleur, texte, action=None):
    pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur))
    font = pygame.font.Font(None, 36)
    texte_surface = font.render(texte, True, NOIR)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (x + largeur / 2, y + hauteur / 2)
    fenetre.blit(texte_surface, texte_rect)
    
# Fonctions de la partie

def timer():
    global duree_timer
    duree_timer -= 1
    timer_text = font.render("Temps restant : " + str(duree_timer), True, (55, 42, 60))
    if duree_timer == 0:
        timer_text = font.render("Temps écoulé !", True, (55, 42, 60))
    return timer_text

def dee(): # A finir
    # Il faudrait créer une attente sans pour autant que ce soit instantané ou faire crash le logiciel
    resultat_dee = random.randint(1, 6)
    texte_dee = font.render("Vous avez fait un " + str(resultat_dee), True, (55, 42, 60))
    time.sleep(1)
    return texte_dee
    # Il faut afficher le résultat du dé

def police(player : players.Joueur):
    proba_police = player.proba_police # A modifier plus tard pour les parties personnaliés
    # A finir
    pass


# États du jeu
ETAT_MENU = 0
ETAT_JEU = 1
etat = ETAT_MENU  # Commencez dans l'état du menu


# Fonction pour le menu principal
def menu_principal():
    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Vérifiez si un bouton a été cliqué
                if 250 <= x <= 750 and 200 <= y <= 250:
                    return ETAT_JEU  # Transition vers l'état du jeu
                if 250 <= x <= 750 and 250 <= y <= 300:
                    print("Tu te calmes !")
                elif 250 <= x <= 750 and 300 <= y <= 350:
                    en_cours = False  # Action du bouton "Quitter"

        fenetre.fill(BLANC)  # Efface l'écran

        # Dessinez vos boutons dans l'état du menu
        dessiner_bouton(250, 200, 500, 50, VERT, "Partie rapide (10 minutes)")
        dessiner_bouton(250, 250, 500, 50, GRIS, "Partie personnalisée (non disponible))")
        dessiner_bouton(250, 300, 500, 50, ROUGE, "Quitter")

        pygame.display.flip()

# Fonction pour le jeu

# Définir une fonction qui demande le nombre de joueurs au joueur

def nombre_joueurs():
    fenetre.fill(BLANC)  # Efface l'écran
    
    # Demande le nombre de joueurs
    demande = True
    nb_joueurs = 0
    while demande:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                demande = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Vérifiez si un bouton a été cliqué
                if 250 <= x <= 750 and 200 <= y <= 250:
                    nb_joueurs = 1
                    return nb_joueurs
                elif 250 <= x <= 750 and 300 <= y <= 350:
                    nb_joueurs = 2
                    return nb_joueurs
                elif 250 <= x <= 750 and 400 <= y <= 450:
                    nb_joueurs = 3
                    return nb_joueurs
                elif 250 <= x <= 750 and 500 <= y <= 550:
                    nb_joueurs = 4
                    return nb_joueurs

        fenetre.fill(BLANC)  # Efface l'écran

        # Dessinez vos boutons dans l'état du menu
        dessiner_bouton(250, 200, 500, 50, VERT, "1 joueur")
        dessiner_bouton(250, 300, 500, 50, VERT, "2 joueurs")
        dessiner_bouton(250, 400, 500, 50, VERT, "3 joueurs")
        dessiner_bouton(250, 500, 500, 50, VERT, "4 joueurs")

        pygame.display.flip()
        
def nom_joueurs(nb_joueurs):
    # Demande à chaque joueur d'écrire son nom
    if nb_joueurs == 1:
        #Demander à ChatGPT de faire le truc
        pass
    elif nb_joueurs == 2:
        #Demander à ChatGPT de faire le truc
        pass
    elif nb_joueurs == 3:
        #Demander à ChatGPT de faire le truc
        pass
    elif nb_joueurs == 4:
        #Demander à ChatGPT de faire le truc
        pass

def jeu(nb_joueurs):
    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False

        fenetre.fill(BLANC)  # Efface l'écran
        
        # Récupération des paramètres de la partie
        
        game_settings = settings.game_settings()
        
        # Demande le nombre de joueurs
        
        # nb_joueurs = nombre_joueurs()
        # Création des joueurs selon la classe et les paramètres du jeu - Vous pouvez passer à la suite
        # A voir comment raccourcir le code
        if nb_joueurs == 1:
            Joueur1 = players.Joueur()
            Joueur1.setNom("Dave")
            Joueur1.setImage("img/sprites/human.png")
        if nb_joueurs == 2:
            Joueur1 = players.Joueur()
            Joueur1.setNom("Dave")
            Joueur1.setImage("img/sprites/dave-human.png")
            Joueur2 = players.Joueur()
            Joueur2.setNom("Wendy")
            Joueur2.setImage("img/sprites/wendy-squirrel.png")
        if nb_joueurs == 3:
            Joueur1 = players.Joueur()
            Joueur1.setNom("Dave")
            Joueur1.setImage("img/sprites/dave-human.png")
            Joueur2 = players.Joueur()
            Joueur2.setNom("Wendy")
            Joueur2.setImage("img/sprites/wendy-squirrel.png")
            Joueur3 = players.Joueur()
            Joueur3.setNom("Bob")
            Joueur3.setImage("img/sprites/bob-aquaman.png")
        if nb_joueurs == 4:
            Joueur1 = players.Joueur()
            Joueur1.setNom("Dave")
            Joueur1.setImage("img/sprites/dave-human.png")
            Joueur2 = players.Joueur()
            Joueur2.setNom("Wendy")
            Joueur2.setImage("img/sprites/wendy-squirrel.png")
            Joueur3 = players.Joueur()
            Joueur3.setNom("Bob")
            Joueur3.setImage("img/sprites/bob-aquaman.png")
            Joueur4 = players.Joueur()
            Joueur4.setNom("Pi")
            Joueur4.setImage("img/sprites/pi-robot.png")
            
        joueur_actif = Joueur1.nom # A changer selon le joueur
        
        # Demande à chaque joueur d'écrire son nom
        
        #nom_joueurs(nb_joueurs)
        

        fenetre.fill((255, 255, 255))
        fenetre.blit(plateau_img, (0,0))
        # Affichage du timer
        temp_timer_text = font.render("Temps restant : X:XX", True, (55, 42, 60))
        fenetre.blit(temp_timer_text, (700, 350))
        #fenetre.blit(timer_txt=timer()), (700, 300)
        # Affichage de l'inventaire
        fenetre.blit(inventaire_text, (700, 100))
        fenetre.blit(inventaire_img, (700, 150))
        # Affichage du joueur
        quelle_joueur = font.render(joueur_actif, True, (55, 42, 60)) # A changer selon le joueur
        fenetre.blit(quelle_joueur, (700, 10))
        # Affichage du dé - A corriger
        #resultat_dee = random.randint(1, 6)
        #texte_dee = dee()
        temp_dee = font.render("Vous avez fait un X", True, (55, 42, 60))
        fenetre.blit(temp_dee, (700, 400))
        #fenetre.blit(texte_dee, (700, 350))
        
    # Affichage des joueurs
        if nb_joueurs == 1:
            fenetre.blit(Joueur1.image, (15, 15))
        if nb_joueurs == 2:
            fenetre.blit(Joueur1.image, (15, 15))
            fenetre.blit(Joueur2.image, (80, 15))
        if nb_joueurs == 3:
            fenetre.blit(Joueur1.image, (15, 15))
            fenetre.blit(Joueur2.image, (80, 15))
            fenetre.blit(Joueur3.image, (15, 80))
        if nb_joueurs == 4:
            fenetre.blit(Joueur1.image, (15, 15))
            fenetre.blit(Joueur2.image, (80, 15))
            fenetre.blit(Joueur3.image, (15, 80))
            fenetre.blit(Joueur4.image, (80, 80))
            
    # Affichage des ennemis
            fenetre.blit(enemy_data.voleur.image, (210, 15))
            fenetre.blit(enemy_data.delinquant.image, (145, 15))
            fenetre.blit(enemy_data.ap_James1.image, (270, 15))
            fenetre.blit(enemy_data.ap_James2.image, (15, 335))
            fenetre.blit(enemy_data.ap_James3.image, (15, 145))
            fenetre.blit(enemy_data.ap_James4.image, (15, 210))
            fenetre.blit(enemy_data.james.image, (15, 400))
    # Deplacement des joueurs
        

        pygame.display.flip()

# Boucle principale
etat = ETAT_MENU  # Commencez dans l'état du menu
       
while etat != None:
    if etat == ETAT_MENU:
        etat=menu_principal()
    elif etat == ETAT_JEU:
        if nb_joueurs == 0:
            nb_joueurs=nombre_joueurs()
        etat=jeu(nb_joueurs)

pygame.quit()
sys.exit()

