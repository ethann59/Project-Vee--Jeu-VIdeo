# Importation des modules
import pygame.font
import time, sys, random
# Importation des fichiers
import players, ennemis, objects
from settings import *
from place_data import *
from enemy_data import *
from object_data import *

# Variables globales

version = "0.0.8"

# Variables de la partie
global settings
settings = game_settings()
duree_timer = settings.time_limit
nb_joueurs = 0

grosses_cases_speciales = {
    0: "Départ",
    7: "Prison",
    13: "Marché",
    20: "Parc"
}


# Variables textuels

pygame.font.init()
font = pygame.font.Font(None, 36)  # Crée une police avec une taille de 36 points (vous pouvez ajuster la taille selon vos besoins)
texte = font.render("Votre texte ici", True, (55, 42, 60))  # Texte blanc avec antialiasing
timer_text = font.render("Temps restant : " + str(duree_timer), True, (55, 42, 60))
inventaire_text = font.render("Inventaire :", True, (55, 42, 60))
    
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
    """
    Dessine un bouton rectangulaire à l'écran avec un texte au centre.

    Args:
        x (int): La position x du coin supérieur gauche du bouton.
        y (int): La position y du coin supérieur gauche du bouton.
        largeur (int): La largeur du bouton.
        hauteur (int): La hauteur du bouton.
        couleur (tuple): La couleur du bouton au format RGB.
        texte (str): Le texte à afficher au centre du bouton.
        action (function, optional): La fonction à exécuter lorsque le bouton est cliqué. Defaults to None.
    """
    pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur))
    font = pygame.font.Font(None, 36)
    texte_surface = font.render(texte, True, NOIR)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (x + largeur / 2, y + hauteur / 2)
    fenetre.blit(texte_surface, texte_rect)
    
# Fonctions de la partie

def timer():
    """
    Gére le timer du jeu
    """
    global duree_timer
    duree_timer -= 1
    timer_text = font.render("Temps restant : " + str(duree_timer), True, (55, 42, 60))
    if duree_timer == 0:
        timer_text = font.render("Temps écoulé !", True, (55, 42, 60))
    return timer_text

def dee():
    # Il faudrait créer une attente sans pour autant que ce soit instantané ou faire crash le logiciel
    resultat_dee = random.randint(1, 6)
    texte_dee = font.render("Vous avez fait un " + str(resultat_dee), True, (55, 42, 60))
    #time.sleep(1)
    return texte_dee, resultat_dee

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
    """Gére le menu principal du jeu

    Returns:
        None
    """
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
                    print("Tu te calmes, Denis !")
                elif 250 <= x <= 750 and 300 <= y <= 350:
                    en_cours = False  # Action du bouton "Quitter"

        fenetre.fill(BLANC)  # Efface l'écran

        # Dessinez vos boutons dans l'état du menu
        titre = font.render("Project Vee", True, (55, 42, 60))
        sous_titre = font.render("Version " + version, True, (55, 42, 60))
        fenetre.blit(titre, (100, 100))
        fenetre.blit(sous_titre, (100, 150))
        # Changer les positions des boutons pour les espacer
        dessiner_bouton(250, 200, 500, 50, VERT, "Partie rapide (10 minutes)")
        dessiner_bouton(250, 250, 500, 50, GRIS, "Partie personnalisée (non disponible))")
        dessiner_bouton(250, 300, 500, 50, ROUGE, "Quitter")

        pygame.display.flip()

# Fonction pour le jeu

# Définir une fonction qui demande le nombre de joueurs au joueur

def nombre_joueurs():
    """
    Demande le nombre de joueurs et renvoie le nombre sélectionné pour le programme "jeu()".

    Returns:
        int: Le nombre de joueurs sélectionné (1, 2, 3 ou 4).
    """
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
        
        player_text = font.render("Combien de joueurs ?", True, (55, 42, 60))
        fenetre.blit(player_text, (250, 100))

        # Dessinez vos boutons dans l'état du menu
        dessiner_bouton(250, 200, 500, 50, VERT, "1 joueur")
        dessiner_bouton(250, 300, 500, 50, VERT, "2 joueurs")
        dessiner_bouton(250, 400, 500, 50, VERT, "3 joueurs")
        dessiner_bouton(250, 500, 500, 50, VERT, "4 joueurs")

        pygame.display.flip()
        
def nom_joueurs(nb_joueurs): # Ça marche mais il attribue pas les noms aux joueurs
    noms = []  # Une liste pour stocker les noms des joueurs
    
    for i in range(1, nb_joueurs + 1):
        nom = ""  # Initialisez le nom du joueur comme une chaîne vide
        
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Appuyez sur Entrée pour valider le nom
                        if nom.strip():  # Vérifiez si le nom n'est pas vide (il doit avoir au moins un caractère)
                            en_cours = False
                    elif event.key == pygame.K_BACKSPACE:
                        nom = nom[:-1]  # Retirez le dernier caractère si la touche Retour arrière est enfoncée
                    else:
                        nom += event.unicode  # Ajoutez le caractère saisi au nom

            fenetre.fill(BLANC)  # Effacez l'écran

            # Affichez un message invitant le joueur à saisir son nom
            texte_surface = font.render(f"Joueur {i}, saisissez votre nom:", True, NOIR)
            fenetre.blit(texte_surface, (100, 100))

            # Affichez le nom saisi jusqu'à présent
            nom_surface = font.render(nom, True, NOIR)
            fenetre.blit(nom_surface, (100, 150))

            pygame.display.flip()
        
        noms.append(nom)  # Ajoutez le nom du joueur à la liste
    
    return noms

def ennemi_random_place():
    '''Cette fonction permet de placer les ennemis important aléatoirement sur le plateau. Ils ont le droit d'aller partout sauf sur les emplacements importants'''
    liste_case_ennemi = []
    for i in range(0, 5):
        random_case = random.randint(1, 26)
        if random_case != 0 and random_case != 7 and random_case != 13 and random_case != 20 and random_case not in liste_case_ennemi:
            liste_case_ennemi.append(random_case)
        else:
            while random_case == 0 or random_case == 7 or random_case == 13 or random_case == 20 or random_case in liste_case_ennemi:
                random_case = random.randint(1, 26)
            liste_case_ennemi.append(random_case)
    # Affectation des ennemis
    ap_James1.case = liste_case_ennemi[0]
    ap_James2.case = liste_case_ennemi[1]
    ap_James3.case = liste_case_ennemi[2]
    ap_James4.case = liste_case_ennemi[3]
    james.case = liste_case_ennemi[4]
    
    return ap_James1.case, ap_James2.case, ap_James3.case, ap_James4.case, james.case
    


def jeu(nb_joueurs, list_playername):
    """La fonction qui gère le jeu en lui-même."""
    # Création des joueurs selon la classe et les paramètres du jeu
    # A voir comment raccourcir le code
        
    list_players : list[players.Joueur]= []
    if nb_joueurs == 1:
        Joueur1 = players.Joueur()
        Joueur1.setNom("Dave") # voir pour le mettre en nom par défaut
        Joueur1.setNom(list_playername[0])
        Joueur1.setImage("img/sprites/dave-human.png")
        list_players.append(Joueur1)
        fenetre.blit(Joueur1.image, (15, 15))
    if nb_joueurs == 2:
        Joueur1 = players.Joueur()
        Joueur1.setNom("Dave")
        Joueur1.setNom(list_playername[0])
        Joueur1.setImage("img/sprites/dave-human.png")
        Joueur2 = players.Joueur()
        Joueur2.setNom("Wendy")
        Joueur2.setNom(list_playername[1])
        Joueur2.setImage("img/sprites/wendy-squirrel.png")
        list_players.append(Joueur1)
        list_players.append(Joueur2)
        fenetre.blit(Joueur1.image, (15, 15))
        fenetre.blit(Joueur2.image, (80, 15))
    if nb_joueurs == 3:
        Joueur1 = players.Joueur()
        Joueur1.setNom("Dave")
        Joueur1.setNom(list_playername[0])
        Joueur1.setImage("img/sprites/dave-human.png")
        Joueur2 = players.Joueur()
        Joueur2.setNom("Wendy")
        Joueur2.setNom(list_playername[1])
        Joueur2.setImage("img/sprites/wendy-squirrel.png")
        Joueur3 = players.Joueur()
        Joueur3.setNom("Bob")
        Joueur3.setNom(list_playername[2])
        Joueur3.setImage("img/sprites/bob-aquaman.png")
        list_players.append(Joueur1)
        list_players.append(Joueur2)
        list_players.append(Joueur3)
        fenetre.blit(Joueur1.image, (15, 15))
        fenetre.blit(Joueur2.image, (80, 15))
        fenetre.blit(Joueur3.image, (15, 80))
    if nb_joueurs == 4:
        Joueur1 = players.Joueur()
        Joueur1.setNom(list_playername[0])
        Joueur1.setImage("img/sprites/dave-human.png")
        Joueur2 = players.Joueur()
        Joueur2.setNom(list_playername[1])
        Joueur2.setImage("img/sprites/wendy-squirrel.png")
        Joueur3 = players.Joueur()
        Joueur3.setNom(list_playername[2])
        Joueur3.setImage("img/sprites/bob-aquaman.png")
        Joueur4 = players.Joueur()
        Joueur4.setNom(list_playername[3])
        Joueur4.setImage("img/sprites/plagiat-murder-drones-lol.png")
        list_players.append(Joueur1)
        list_players.append(Joueur2)
        list_players.append(Joueur3)
        list_players.append(Joueur4)
        fenetre.blit(Joueur1.image, (15, 15))
        fenetre.blit(Joueur2.image, (80, 15))
        fenetre.blit(Joueur3.image, (15, 80))
        fenetre.blit(Joueur4.image, (80, 80))
    
    joueur_actif = list_players[0] # A changer selon le joueur
    
    # Micro tuto
    tuto = font.render("Lancer le dé : [Espace]", True, (55, 42, 60)) # Voir comment le faire apparaitre que une fois
    #first_tour = True
    
    fenetre.blit(tuto, (700, 450))
    
    # Jeu en lui-même
    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Touche Espace pour lancer le dé
                    texte_dee, resultat_dee = dee()
                    fenetre.blit(texte_dee, (700, 400)) # Je sais pas pourquoi mais ça marche pas

                    # Déplacer le personnage
                    joueur_actif.addCase(resultat_dee, plateau_info)
                    fenetre.blit(joueur_actif.image, (plateau_info[joueur_actif.case]["x"], plateau_info[joueur_actif.case]["y"]))
                    
                    # Les ennemis qui apparaissent de manière aléatoire
                    dee_ennemi = random.rand(0, 1)
                    if dee_ennemi > 0.:

                    # Gérer le changement de joueur en fonction du nombre de joueurs  
                    if nb_joueurs > 0:
                        joueur_actif = list_players[(list_players.index(joueur_actif) + 1) % nb_joueurs]


        fenetre.fill(BLANC)  # Efface l'écran

        fenetre.fill((255, 255, 255))
        fenetre.blit(plateau_img, (0,0))
        fenetre.blit(tuto, (700, 450))
        # Affichage du timer
        temp_timer_text = font.render("Temps restant : X:XX", True, (55, 42, 60))
        fenetre.blit(temp_timer_text, (700, 350))
        #fenetre.blit(timer_txt=timer()), (700, 300)
        # Affichage de l'inventaire
        fenetre.blit(inventaire_text, (700, 100))
        fenetre.blit(inventaire_img, (700, 150))
        # Affichage du joueur
        quelle_joueur = font.render(joueur_actif.nom, True, (55, 42, 60))
        argent_joueur = font.render("Or : " + str(joueur_actif.gold), True, (55, 42, 60))
        fenetre.blit(quelle_joueur, (700, 10))
        fenetre.blit(argent_joueur, (700, 50))
        
    
        # Affichage des ennemis importants
        fenetre.blit(ap_James1.image, (plateau_info[ap_James1.case]["x"], plateau_info[ap_James1.case]["y"]))
        fenetre.blit(ap_James2.image, (plateau_info[ap_James2.case]["x"], plateau_info[ap_James2.case]["y"]))
        fenetre.blit(ap_James3.image, (plateau_info[ap_James3.case]["x"], plateau_info[ap_James3.case]["y"]))
        fenetre.blit(ap_James4.image, (plateau_info[ap_James4.case]["x"], plateau_info[ap_James4.case]["y"]))
        # fenetre.blit(james.image, (15, 400)) -- Il faut le faire apparaitre quand un joueur a tout les items
            
        
        # Normalement ça permet de actualiser le plateau
        fenetre.blit(plateau_img, (0,0))
        #fenetre.blit(texte_dee, (700, 450))
        # Affichage des ennemis importants
        fenetre.blit(ap_James1.image, (plateau_info[ap_James1.case]["x"], plateau_info[ap_James1.case]["y"]))
        fenetre.blit(ap_James2.image, (plateau_info[ap_James2.case]["x"], plateau_info[ap_James2.case]["y"]))
        fenetre.blit(ap_James3.image, (plateau_info[ap_James3.case]["x"], plateau_info[ap_James3.case]["y"]))
        fenetre.blit(ap_James4.image, (plateau_info[ap_James4.case]["x"], plateau_info[ap_James4.case]["y"]))
        
        
        # Affichage des joueurs
        # Il vérifie si le joueur est sur une case spéciale et si oui, il l'affiche à la bonne position ainsi que les autres joueurs sur la même case
        # Avant c'était un gros if mais j'ai changé pour un dictionnaire, j'en suis plutot fier
        
        joueur_case = []
        for player in list_players:
            if player.case in grosses_cases_speciales:
                fenetre.blit(player.image, (plateau_pos_alternatif[grosses_cases_speciales[player.case]][list_players.index(player)]))
                joueur_case.append(player.case)
            elif player.case in joueur_case and joueur_case.count(player.case) == 1:
                fenetre.blit(player.image, (plateau_info[player.case]["x"], plateau_info[player.case]["y"] + 10))
                joueur_case.append(player.case)
            elif player.case in joueur_case and joueur_case.count(player.case) == 2:
                fenetre.blit(player.image, (plateau_info[player.case]["x"], plateau_info[player.case]["y"] - 10))
                joueur_case.append(player.case)
            elif player.case in joueur_case and joueur_case.count(player.case) == 3:
                fenetre.blit(player.image, (plateau_info[player.case]["x"], plateau_info[player.case]["y"] + 20))
                joueur_case.append(player.case)
            else:
                fenetre.blit(player.image, (plateau_info[player.case]["x"], plateau_info[player.case]["y"]))
                joueur_case.append(player.case)
        pygame.display.flip()

# Boucle principale
# C'est gérer le menu le passage au jeu etc
etat = ETAT_MENU  # Commencez dans l'état du menu
       
while etat != None:
    if etat == ETAT_MENU:
        etat=menu_principal()
    elif etat == ETAT_JEU:
        if nb_joueurs == 0:
            nb_joueurs=nombre_joueurs()
            list_playername=nom_joueurs(nb_joueurs)
            ennemi_random_place()
        etat=jeu(nb_joueurs, list_playername)

pygame.quit()
sys.exit()

