# Importation des modules
import pygame.font
import sys, random
# Importation des fichiers
import players
from settings import *
from enemy_data import *
from object_data import *
from players import Joueur
from ennemis import Ennemi, EnnemiImportant
from plateau import *

# Variables globales

version = "0.1.0"

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
GRIS = (128, 128, 128)
BLEU = (0, 0, 255)

# Variables de la partie
global settings
settings = game_settings()
duree_timer = settings.time_limit
nb_joueurs = 0 # Penser à utiliser la classe game_settings pour changer le nombre de joueurs

grosses_cases_speciales = {
    0: "Départ",
    7: "Prison",
    13: "Marché",
    20: "Hopital"
}


# Variables textuels

pygame.font.init()
font = pygame.font.Font(None, 36)  # Crée une police avec une taille de 36 points (vous pouvez ajuster la taille selon vos besoins)
inventaire_text = font.render("Inventaire :", True, BLANC)
    
# Variables graphiques

plateau_img = pygame.image.load("img/scenes/plateau.jpg")
plateau_img = pygame.transform.scale(plateau_img, (648, 644))
background_img = pygame.image.load("img/scenes/fantasy_london_flou.jpg")
# Voir pour appliquer un effet de flou
inventaire_img = pygame.image.load("img/scenes/inventaire.png")

# Initialisation de Pygame
pygame.init()

# Configurer la fenêtre
taille_fenetre = (1000,644)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Aexo - Le Plan de James - Developement Build " + version)

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

def dee():
    # Il faudrait créer une attente sans pour autant que ce soit instantané ou faire crash le logiciel
    resultat_dee = random.randint(1, 6)
    texte_dee = font.render("Vous avez fait un " + str(resultat_dee), True, BLANC)
    #time.sleep(1)
    return texte_dee, resultat_dee

def save():
    """
    Gére la sauvegarde de la partie (parce que apparament il faudrait en faire une)
    """
    pass

def hospital(joueur):
    # Création du fond du menu
    menu_surface = pygame.Surface((400, 200))
    menu_surface.fill(BLANC)
    menu_surface.set_alpha(200)  # Transparence du fond

    # Affichage du texte
    texte_surface = font.render("Hôpital", True, BLANC)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (200, 50)

    # Affichage du coût des soins
    cout_surface = font.render(f"Soins (Coût : {settings.hospital_price} pièces d'or)", True, BLANC)
    cout_rect = cout_surface.get_rect()
    cout_rect.center = (200, 100)

    # Affichage du bouton "Se soigner"
    bouton_se_soigner = pygame.Rect(150, 150, 200, 40)
    pygame.draw.rect(menu_surface, BLANC, bouton_se_soigner)
    bouton_surface = font.render("Se soigner", True, BLANC)
    bouton_rect = bouton_surface.get_rect()
    bouton_rect.center = bouton_se_soigner.center
    
     # Affichage du bouton "Ne pas se soigner"
    bouton_ne_pas_se_soigner = pygame.Rect(400, 150, 200, 40)
    pygame.draw.rect(menu_surface, BLANC, bouton_ne_pas_se_soigner)
    bouton_ne_pas_se_soigner_surface = font.render("Ne pas se soigner", True, BLANC)
    bouton_ne_pas_se_soigner_rect = bouton_ne_pas_se_soigner_surface.get_rect()
    bouton_ne_pas_se_soigner_rect.center = bouton_ne_pas_se_soigner.center


    # Affichage du menu
    fenetre.blit(menu_surface, (200, 200))
    fenetre.blit(texte_surface, texte_rect)
    fenetre.blit(cout_surface, cout_rect)
    fenetre.blit(bouton_surface, bouton_rect)
    
    # Variables textuelles
    texte_soin = font.render("Vous vous êtes soigné à l'hôpital. Vie restaurée à {settings.pv_player} points.", True, BLANC)
    texte_argent = font.render("Argent restant : {joueur.gold} pièces d'or.", True, BLANC)
    texte_pas_soin = font.render("Désolé, vous n'avez pas assez d'argent pour vous soigner à l'hôpital.", True, BLANC)

    # Vérifie si le joueur clique sur le bouton "Se soigner"
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_se_soigner.collidepoint(event.pos):
                # Vérifie si le joueur a suffisamment d'argent pour se soigner
                if joueur.gold >= gc.settings.hopital_price:
                    joueur.pv = gc.settings.pv_player  # Réinitialise la vie du joueur à son maximum
                    joueur.gold -= gc.settings.hopital_price  # Déduit le coût des soins de l'argent du joueur
                    fenetre.blit(texte_soin, (200, 250))
                    fenetre.blit(texte_argent, (200, 300))
                    return joueur.pv, joueur.gold
                else:
                    fenetre.blit(texte_pas_soin, (200, 250))

        
def shop(argent_joueur, inventaire_joueur):
    while True:
        fenetre.fill((255, 255, 255))
        # Afficher la liste des objets disponibles avec leurs prix
        y = 50
        for item in items_disponibles:
            texte = font.render(f"{item.nom}: {item.prix} pièces d'or", True, (0, 0, 0))
            fenetre.blit(texte, (50, y))
            y += 30
        
        # Afficher l'argent du joueur
        texte_argent = font.render(f"Argent du joueur: {argent_joueur} pièces d'or", True, (0, 0, 0))
        fenetre.blit(texte_argent, (50, 10))
        
        # Variables textuelles
        texte_achat = font.render("Vous avez acheté un objet.", True, (0, 0, 0))
        texte_argent = font.render(f"Argent restant : {argent_joueur} pièces d'or.", True, (0, 0, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifier si un objet a été cliqué
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 50 <= mouse_x <= 250:
                    for i, item in enumerate(items_disponibles):
                        if 50 <= mouse_y <= 50 + 30 * (i + 1):
                            if argent_joueur >= item.prix:
                                # Le joueur a assez d'argent, il peut acheter l'objet
                                argent_joueur -= item.prix
                                # Ajouter l'objet à l'inventaire du joueur
                                inventaire_joueur.append(item)
                                fenetre.blit(texte_achat, (50, 250))
                            else:
                                # Le joueur n'a pas assez d'argent pour acheter l'objet
                                fenetre.blit(texte_argent, (50, 300))
                                pygame.display.flip()
                            
        return argent_joueur, inventaire_joueur
                                

def prison(joueur):
    '''Cette fonction sert à controler le joueur quand il est en prison notamment le bloquer tant que il a pas fait 3 tours'''
    
    # Variables textuelles
    
    text_sortie = font.render("Vous êtes sorti de prison.", True, BLANC)
    text_prison = font.render("Vous êtes en prison, vous devez attendre 3 tours.", True, BLANC)
    text_caution = font.render("Voulez-vous payer 100 pièces d'or pour sortir de prison ? (Y/N)", True, BLANC)
    text_argent = font.render("Vous n'avez pas assez d'argent pour payer la caution.", True, BLANC)
    
    if joueur.prison == True:
        if joueur.prison_timer == 3:
            joueur.prison = False
            joueur.prison_timer = 0
            fenetre.blit(text_sortie, (200, 250))
        else:
            joueur.prison_timer += 1
            fenetre.blit(text_prison, (200, 250))
            # Demande au joueur si il veut payer pour sortir de prison
            fenetre.blit(text_caution, (200, 300))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        if joueur.gold >= 100:
                            joueur.gold -= 100
                            joueur.prison = False
                            joueur.prison_timer = 0
                            fenetre.blit(text_sortie, (200, 250))
                        else:
                            fenetre.blit(text_argent, (200, 300))
                    elif event.key == pygame.K_n:
                        fenetre.blit(text_prison, (200, 250))
    return joueur.prison, joueur.prison_timer



def combat_pve(joueur : Joueur, ennemi : Ennemi): # Voir pour coder un inventaire au passage
    fenetre.fill(BLANC)
    # Variables de combat - Pour vérifier si les boucliers sont actifs
    enemyshield_on = 0
    playershield_on = 0
    show_inventory = False  # Au départ, l'inventaire est masqué
    grenade_flash_active = False
    enemy_pv_de_base = ennemi.pv
    
    # Variables textuels
    
    text_block_attack = font.render(("Il a bloqué l'attaque ! Il lui reste " + str(ennemi.pv) + " PV"), True, BLANC)
    text_normal_attack = font.render(("Il lui reste " + str(ennemi.pv) + " PV"), True, BLANC)
    text_prepare_shield = font.render(("Vous vous préparez votre bouclier."), True, BLANC)
    text_no_run = font.render(("Vous ne pouvez pas fuir, vous devez le tuer !"), True, BLANC)
    text_run = font.render(("Vous avez fui le combat."), True, BLANC)
    attack_text= font.render("Attaquer", True, BLANC)
    defend_text = font.render("Défendre", True, BLANC)
    flee_text = font.render("Fuir", True, BLANC)
    inventory_text = font.render("Inventaire", True, BLANC)
    text_pv_player = font.render(("Vous avez " + str(joueur.pv) + " PV"), True, BLANC)
    text_pv_enemy = font.render(("L'ennemi a " + str(ennemi.pv) + " PV"), True, BLANC)
    text_shield_player = font.render(("Vous avez votre bouclier activé"), True, BLANC)
    text_no_shield_player = font.render(("Vous avez votre bouclier désactivé"), True, BLANC)
    text_grenade_flash = font.render(("L'ennemi est aveuglé"), True, BLANC)
    text_attack_enemy = font.render(("L'ennemi attaque"), True, BLANC)
    text_block_attack_enemy = font.render(("Vous avez bloqué l'attaque ! Il vous reste " + str(joueur.pv) + " PV"), True, BLANC)
    text_defend_enemy = font.render(("L'ennemi se défend"), True, BLANC)
    text_police = font.render(("Wuwu ! Ceci est une descente de la police !"), True, BLANC)
    text_lose = font.render(("Vous avez perdu !"), True, BLANC)
    text_win = font.render(("Vous avez gagné ! Vous avez obtenu " + str(ennemi.gold)), True, BLANC)
    if isinstance(ennemi, EnnemiImportant):
        text_quest_object = font.render(("Vous avez obtenu un objet de quête !" + str(ennemi.quest_object.nom)), True, BLANC)
    
    
    # Créez des boutons "Attaquer", "Défendre" et "Fuir"
    defend_button = pygame.Rect(200, 200, 100, 50)
    flee_button = pygame.Rect(350, 200, 100, 50)
    attack_button = pygame.Rect(50, 200, 100, 50)  # Zone cliquable du bouton d'attaque
    inventory_button = pygame.Rect(500, 200, 100, 50)
    
    # Stocker le texte dans une variable pour le changer sur l'affichage
    # Penser à afficher les images des ennemis et du joueur
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if attack_button.collidepoint(event.pos):
                    # Logique d'attaque
                    # Réduisez les PV de l'ennemi ou augmentez les dégâts du joueur
                    if enemyshield_on == 1:
                        ennemi.pv -= (joueur.patt - ennemi.pam)
                        fenetre.blit(text_block_attack, (50, 50))                    
                    if enemyshield_on == 0:
                        ennemi.pv -= joueur.patt
                        fenetre.blit(text_normal_attack, (50, 50))
                elif defend_button.collidepoint(event.pos):
                    # Logique de défense
                    # Réduisez les dégâts subis par le joueur ou augmentez sa défense
                    playershield_on = 1
                    fenetre.blit(text_prepare_shield, (50, 50))
                elif flee_button.collidepoint(event.pos):
                    # Logique de fuite
                    # Terminez la partie ou retournez à un écran précédent
                    if isinstance(ennemi, EnnemiImportant):
                        fenetre.blit(text_no_run, (50, 50))
                    else:
                        fenetre.blit(text_run, (50, 50))
                        return joueur.pv, joueur.gold
            
    # Affichez les boutons
    pygame.draw.rect(fenetre, BLEU, defend_button)
    pygame.draw.rect(fenetre, VERT, flee_button)
    pygame.draw.rect(fenetre, ROUGE, attack_button)
    pygame.draw.rect(fenetre, BLEU, inventory_button)  # Bouton vert pour l'inventaire

    # Affichez les textes des boutons
    
    fenetre.blit(attack_text, (attack_button.x + 10, attack_button.y + 10))
    fenetre.blit(defend_text, (defend_button.x + 10, defend_button.y + 10))
    fenetre.blit(flee_text, (flee_button.x + 10, flee_button.y + 10))
    fenetre.blit(inventory_text, (inventory_button.x + 10, inventory_button.y + 10))
    
    
    # Afficher l'inventaire si le bouton est cliqué
    # Si l'inventaire est affiché, dessinez le contenu de l'inventaire ici
    if show_inventory:
    # Dessinez les éléments de l'inventaire
    # Par exemple, affichez une liste d'objets avec des quantités
    # Assurez-vous de positionner et de styliser correctement l'affichage de l'inventaire
    # Vous pouvez utiliser une boucle pour parcourir les éléments de l'inventaire et les afficher
        pass
    # Affichez les PV du joueur et de l'ennemi
    
    fenetre.blit(text_pv_player, (50, 100))
    
    fenetre.blit(text_pv_enemy, (50, 150))
        
    if playershield_on == 1:
        fenetre.blit(text_shield_player, (50, 150))
    if playershield_on == 0:
        fenetre.blit(text_no_shield_player, (50, 150))
    
    # Coder le système de bouclier temporaire
    if joueur.pam_temp_duree > 0:
        joueur.pam_temp_duree -= 1
    elif joueur.pam_temp_duree == 0:
        joueur.pam = 0
        joueur.pam_temp_duree = 0
    
    # Choix de l'ennemi
    if grenade_flash_active == True:
        fenetre.blit(text_grenade_flash, (50, 250))
        temp_turn += 1
        if temp_turn == 2:
            grenade_flash_active = False
            temp_turn = 0
    else:
        ennemi_choice = random.randint(1, 2)
        if ennemi_choice == 1:
            fenetre.blit(text_attack_enemy, (50, 250))
            if playershield_on == 1:
                joueur.pv -= (ennemi.patt - joueur.pam)
                fenetre.blit(text_block_attack, (50, 300))
            if playershield_on == 0:
                joueur.pv -= ennemi.patt
                fenetre.blit(text_pv_player, (50, 300))
        if ennemi_choice == 2:
            fenetre.blit(text_defend_enemy, (50, 250))
            enemyshield_on = 1
        
    # Pensez à coder l'event "police"
    if random.randint(0, 100) <= joueur.proba_police:
        fenetre.blit(text_police, (50, 250))
        joueur.setCase(7)
        joueur.setKo(False)
        joueur.activatePrison()
        return joueur.pv, joueur.gold
        
    # Conditions de victoire et de défaite
    if joueur.pv <= 0:
        fenetre.blit(text_lose, (50, 350))
        joueur.setCase(20)
        joueur.setKo(True)
        return joueur.pv, joueur.gold
    if ennemi.pv <= 0:
        fenetre.blit(text_win, (50, 350))
        joueur.gold += ennemi.gold
        joueur.addScore(enemy_pv_de_base)
        if isinstance(ennemi, EnnemiImportant):
            joueur.inventaire.append(ennemi.quest_object)
            fenetre.blit(text_quest_object, (50, 400))
        
    
    return joueur.pv, joueur.gold


def combat_pvp(joueur1: Joueur, joueur2: Joueur):
    fenetre.fill(BLANC)
    # Variables de combat - Pour vérifier si les boucliers sont actifs
    player1shield_on = 0
    player2shield_on = 0
    show_inventory = False  # Au départ, l'inventaire est masqué
    grenade_flash_active = False
    joueur_actif = joueur1
    
    # Créez des boutons "Attaquer", "Défendre" et "Fuir"
    defend_button = pygame.Rect(200, 200, 100, 50)
    flee_button = pygame.Rect(350, 200, 100, 50)
    attack_button = pygame.Rect(50, 200, 100, 50)  # Zone cliquable du bouton d'attaque
    inventory_button = pygame.Rect(500, 200, 100, 50)
    
    # Variables textuels
    text_police = font.render(("Wuwu ! Ceci est une descente de la police !"), True, BLANC)
    
    # Stocker le texte dans une variable pour le changer sur l'affichage
    # Penser à afficher les images des ennemis et du joueur
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if joueur_actif == joueur1:
                    if attack_button.collidepoint(event.pos):
                        # Logique d'attaque
                        # Réduisez les PV de l'ennemi ou augmentez les dégâts du joueur
                        if player2shield_on == 1:
                            joueur2.pv -= (joueur1.patt - joueur2.pam)
                            fenetre.blit(("Il a bloqué l'attaque ! Il lui reste " + str(joueur2.pv) + " PV"), (50, 50))                    
                        if player2shield_on == 0:
                            joueur2.pv -= joueur1.patt
                            fenetre.blit(("Il lui reste " + str(joueur2.pv) + " PV"), (50, 50))
                    elif defend_button.collidepoint(event.pos):
                        # Logique de défense
                        # Réduisez les dégâts subis par le joueur ou augmentez sa défense
                        playershield_on = 1
                        fenetre.blit(("Vous vous préparez votre bouclier."), (50, 50))
                    elif flee_button.collidepoint(event.pos):
                        # Logique de fuite
                        # Terminez la partie ou retournez à un écran précédent
                        fenetre.blit(("Vous avez fui le combat."), (50, 50))
                        return joueur1.pv, joueur2.pv
                if joueur_actif == joueur2:
                    if attack_button.collidepoint(event.pos):
                        # Logique d'attaque
                        # Réduisez les PV de l'ennemi ou augmentez les dégâts du joueur
                        if player1shield_on == 1:
                            joueur1.pv -= (joueur2.patt - joueur1.pam)
                            fenetre.blit(("Il a bloqué l'attaque ! Il lui reste " + str(joueur1.pv) + " PV"), (50, 50))                    
                        if player1shield_on == 0:
                            joueur1.pv -= joueur2.patt
                            fenetre.blit(("Il lui reste " + str(joueur1.pv) + " PV"), (50, 50))
                    elif defend_button.collidepoint(event.pos):
                        # Logique de défense
                        # Réduisez les dégâts subis par le joueur ou augmentez sa défense
                        playershield_on = 1
                        fenetre.blit(("Vous vous préparez votre bouclier."), (50, 50))
                    elif flee_button.collidepoint(event.pos):
                        # Logique de fuite
                        # Terminez la partie ou retournez à un écran précédent
                        fenetre.blit(("Vous avez fui le combat."), (50, 50))
                        return joueur1.pv, joueur2.pv
            
    # Affichez les boutons
    pygame.draw.rect(fenetre, BLEU, defend_button)
    pygame.draw.rect(fenetre, VERT, flee_button)
    pygame.draw.rect(fenetre, ROUGE, attack_button)
    pygame.draw.rect(fenetre, BLEU, inventory_button)  # Bouton vert pour l'inventaire

    # Affichez les textes des boutons
    
    fenetre.blit(("Attaquer"), (attack_button.x + 10, attack_button.y + 10))
    fenetre.blit(("Défendre"), (defend_button.x + 10, defend_button.y + 10))
    fenetre.blit(("Fuir"), (flee_button.x + 10, flee_button.y + 10))
    fenetre.blit(("Inventaire"), (inventory_button.x + 10, inventory_button.y + 10))
    
    
    # Afficher l'inventaire si le bouton est cliqué
    # Si l'inventaire est affiché, dessinez le contenu de l'inventaire ici
    if show_inventory:
    # Dessinez les éléments de l'inventaire
    # Par exemple, affichez une liste d'objets avec des quantités
    # Assurez-vous de positionner et de styliser correctement l'affichage de l'inventaire
    # Vous pouvez utiliser une boucle pour parcourir les éléments de l'inventaire et les afficher
        pass
    # Affichez les PV du joueur et de l'ennemi
    
    fenetre.blit((joueur1.name, " a " + str(joueur1.pv) + " PV"), (50, 100))
    
    fenetre.blit((joueur1.name, " a " + str(joueur2.pv) + " PV"), (50, 150))
        
    if player1shield_on == 1:
        fenetre.blit(("Vous avez votre bouclier activé"), (50, 150))
    if player2shield_on == 0:
        fenetre.blit(("Vous avez votre bouclier désactivé"), (50, 150))
    
       # Coder le système de bouclier temporaire
    if joueur1.pam_temp_duree > 0:
        joueur1.pam_temp_duree -= 1
    elif joueur1.pam_temp_duree == 0:
        joueur1.pam = 0
        joueur1.pam_temp_duree = 0
    
    # Coder le système de bouclier temporaire
    if joueur2.pam_temp_duree > 0:
        joueur2.pam_temp_duree -= 1
    elif joueur2.pam_temp_duree == 0:
        joueur2.pam = 0
        joueur2.pam_temp_duree = 0
    
        
    # Pensez à coder l'event "police"
    if random.randint(0, 100) <= joueur1.proba_police or random.randint(0, 100) <= joueur2.proba_police:
        fenetre.blit(text_police, (50, 250))
        joueur1.setCase(7)
        joueur1.setKo(False)
        joueur1.activatePrison()
        joueur2.setCase(7)
        joueur2.setKo(False)
        joueur2.activatePrison()
        return joueur1.pv, joueur1.gold, joueur2.pv, joueur2.gold
    
    if joueur_actif == joueur1:
        joueur_actif = joueur2
        
    # Conditions de victoire et de défaite
    if joueur1.pv <= 0:
        fenetre.blit(("Vous avez perdu !"), (50, 350))
        joueur1.setCase(20)
        joueur1.setKo(True)
        return joueur1.pv, joueur1.gold
    if joueur2.pv <= 0:
        fenetre.blit(("Vous avez gagné !"), (50, 350))
        joueur1.gold += joueur2.gold
        joueur2.setCase(20)
        joueur2.setKo(True)
        # Vérifier si le joueur 2 a un objet de quête et si il en a un, de piocher parmi ce qu'il a, et de le donner au joueur 1
        if QuestObject in joueur2.inventaire:
            # On liste les objets de quête que le joueur 2 a
            j2_quest_objects = []
            for i in joueur2.inventaire:
                if isinstance(i, QuestObject):
                    j2_quest_objects.append(i)
            # On en choisit un au hasard
            j2_quest_object = random.choice(j2_quest_objects)
            # On le donne au joueur 1
            joueur1.inventaire.append(j2_quest_object)
            # On le retire du joueur 2
            joueur2.inventaire.remove(j2_quest_object)
        return joueur1.pv, joueur1.gold
            
        


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
        fenetre.blit(background_img, (0, 0))
        # Dessinez vos boutons dans l'état du menu
        titre = font.render("Aexo - Le Plan de James", True, BLANC)
        sous_titre = font.render("Version " + version, True, BLANC)
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
        fenetre.blit(background_img, (0, 0))
        
        player_text = font.render("Combien de joueurs ?", True, BLANC)
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
            fenetre.blit(background_img, (0, 0))

            # Affichez un message invitant le joueur à saisir son nom
            texte_surface = font.render(f"Joueur {i}, saisissez votre nom:", True, BLANC)
            fenetre.blit(texte_surface, (100, 100))

            # Affichez le nom saisi jusqu'à présent
            nom_surface = font.render(nom, True, BLANC)
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

def calculate_ranking(players):
    '''Calculates the ranking based on player scores'''
    sorted_players = sorted(players, key=lambda player: player.score, reverse=True)
    ranking = []
    for i, player in enumerate(sorted_players):
        ranking.append(f"{i+1}. {player.nom} ({player.score} points)")
    return ranking

def end_game(motif, list_players):
    '''Cette fonction permet de gérer la fin de la partie'''
    fenetre.fill(BLANC)
    fenetre.blit(background_img, (0, 0))
    
    # Calculer le classement
    classement = calculate_ranking(list_players)
    texte_1er = font.render(f"classment[0]", True, BLANC)
    fenetre.blit(texte_1er, (100, 100))
    texte_2eme = font.render(f"classment[1]", True, BLANC)
    fenetre.blit(texte_2eme, (100, 150))
    texte_3eme = font.render(f"classment[2]", True, BLANC)
    fenetre.blit(texte_3eme, (100, 200))
    texte_4eme = font.render(f"classment[3]", True, BLANC)

            
    
    if motif == "time":
        texte_fin = font.render("Temps écoulé !", True, BLANC)
        fenetre.blit(texte_fin, (100, 100))
        # Afficher le classement
        classement = font.render("Classement :", True, BLANC)
        fenetre.blit(classement, (100, 150))
        fenetre.blit(texte_1er, (100, 200))
        fenetre.blit(texte_2eme, (100, 250))
        fenetre.blit(texte_3eme, (100, 300))
        fenetre.blit(texte_4eme, (100, 350))
        # Afficher le bouton pour quitter
        # A faire
    elif motif == "james":
        texte_fin = font.render("Vous avez battu James !", True, BLANC)
        fenetre.blit(texte_fin, (100, 100))
        # Afficher le classement
        classement = font.render("Classement :", True, BLANC)
        fenetre.blit(classement, (100, 150))
        fenetre.blit(texte_1er, (100, 200))
        fenetre.blit(texte_2eme, (100, 250))
        fenetre.blit(texte_3eme, (100, 300))
        fenetre.blit(texte_4eme, (100, 350))
        # Afficher le bouton pour quitter
        # A faire
    


def jeu(nb_joueurs, list_playername):
    """La fonction qui gère le jeu en lui-même."""
    # Création des joueurs selon la classe et les paramètres du jeu
    # A voir comment raccourcir le code
        
    # Penser à définir les PV des joueurs selon les paramètres du jeu dans la classe game_settings
    
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
    
    # Heure de début du timer
    debut_timer = pygame.time.get_ticks()
    
    # Micro tuto
    tuto = font.render("Lancer le dé : [Espace]", True, BLANC) # Voir comment le faire apparaitre que une fois
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
                    # Vérifier si le joueur n'est pas en prison
                    if joueur_actif.prison == True:
                        prison(joueur_actif)
                    else:
                        # Lancer le dé
                        texte_dee, resultat_dee = dee()
                        fenetre.blit(texte_dee, (700, 400)) # Je sais pas pourquoi mais ça marche pas

                        # Déplacer le personnage
                        joueur_actif.addCase(resultat_dee)
                        fenetre.blit(joueur_actif.image, (plateau_info[joueur_actif.case]["x"], plateau_info[joueur_actif.case]["y"]))
                    
                        ## Les ennemis qui apparaissent de manière aléatoire
                        #dee_ennemi = random.randint(0, 100)
                        #if dee_ennemi < 15:
                        #    combat_pve(joueur_actif, delinquant)
                        #if dee_ennemi < 30:
                        #    combat_pve(joueur_actif, voleur)

                        # PvP
                        # for player in list_players:
                            # if joueur_actif.case == player.case and joueur_actif != player:
                                # combat_pvp(joueur_actif, player)

                        
                        ## Menu par rapport à la case spéciale
                        #if joueur_actif.case == 13:
                        #    shop(joueur_actif.gold, joueur_actif.inventaire)
                        #elif joueur_actif.case == 20:
                        #    hospital(joueur_actif)
                        #elif joueur_actif.case == ap_James1.case:
                        #    combat_pve(joueur_actif, ap_James1)
                        #elif joueur_actif.case == ap_James2.case:
                        #    combat_pve(joueur_actif, ap_James2)
                        #elif joueur_actif.case == ap_James3.case:
                        #    combat_pve(joueur_actif, ap_James3)
                        #elif joueur_actif.case == ap_James4.case:
                        #    combat_pve(joueur_actif, ap_James4)
                        #elif joueur_actif.case == james.case and ItemQuete1 in joueur_actif.inventaire and ItemQuete2 in joueur_actif.inventaire and ItemQuete3 in joueur_actif.inventaire and ItemQuete4 in joueur_actif.inventaire:
                        #    combat_pve(joueur_actif, james)
                        ## Gérer le changement de joueur en fonction du nombre de joueurs  
                        #if nb_joueurs > 0:
                        #    joueur_actif = list_players[(list_players.index(joueur_actif) + 1) % nb_joueurs]

        fenetre.fill(BLANC)  # Efface l'écran
        
        # Obtenir le temps écoulé depuis le début du timer
        temps_ecoule = pygame.time.get_ticks() - debut_timer
        
        # Calculer les minutes et les secondes restantes
        minutes_restantes = (settings.time_limit - temps_ecoule) // 60000
        secondes_restantes = (settings.time_limit - temps_ecoule) // 1000 % 60
        
         # Afficher le minuteur à l'écran
        timer_text = font.render(f"{minutes_restantes:02}:{secondes_restantes:02}", True, (255, 255, 255))

        fenetre.fill((255, 255, 255))
        fenetre.blit(background_img, (0,0))
        fenetre.blit(plateau_img, (0,0))
        fenetre.blit(tuto, (700, 450))
        # Affichage du timer
        temp_timer_text = font.render("Temps restant : X:XX", True, BLANC)
        fenetre.blit(temp_timer_text, (700, 350))
        fenetre.blit(timer_text, (700, 400))
        # Affichage de l'inventaire
        fenetre.blit(inventaire_text, (700, 100))
        fenetre.blit(inventaire_img, (700, 150))
        # Affichage des items de quetes du joueur
        item_quest = font.render("Items de quêtes :", True, BLANC)
        fenetre.blit(item_quest, (700, 500))
        #fenetre.blit("Item 1", (700, 250)) A faire quand on aura les images
        # Affichage du joueur
        quelle_joueur = font.render(joueur_actif.nom, True, BLANC)
        argent_joueur = font.render("Or : " + str(joueur_actif.gold), True, BLANC)
        fenetre.blit(quelle_joueur, (700, 10))
        fenetre.blit(argent_joueur, (700, 50))
        
        # Normalement ça permet de actualiser le plateau
        fenetre.blit(plateau_img, (0,0))
        #fenetre.blit(texte_dee, (700, 450))
        # Affichage des ennemis importants
        fenetre.blit(ap_James1.image, (plateau_info[ap_James1.case]["x"], plateau_info[ap_James1.case]["y"])) # Peut etre les faire bouger un jour
        fenetre.blit(ap_James2.image, (plateau_info[ap_James2.case]["x"], plateau_info[ap_James2.case]["y"]))
        fenetre.blit(ap_James3.image, (plateau_info[ap_James3.case]["x"], plateau_info[ap_James3.case]["y"]))
        fenetre.blit(ap_James4.image, (plateau_info[ap_James4.case]["x"], plateau_info[ap_James4.case]["y"]))
        
        if ItemQuete1 in joueur_actif.inventaire and ItemQuete2 in joueur_actif.inventaire and ItemQuete3 in joueur_actif.inventaire and ItemQuete4 in joueur_actif.inventaire:
            fenetre.blit(james.image, (plateau_info[james.case]["x"], plateau_info[james.case]["y"]))
        
        
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
                
                
        # Affichage du score du joueur
        # Pas oublier de faire le calcul
        
        score_text = font.render("Score :" + str(joueur_actif.Score), True, BLANC)
        fenetre.blit(score_text, (700, 550))
        
        # Conditions de fin de partie
        
        if temps_ecoule >= settings.time_limit and settings.time_limit != 0:
            end_game("time", list_players)
        elif james.killed == True:
            end_game("james", list_players)
                
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
            etat=jeu(settings.nb_player, list_playername)

pygame.quit()
sys.exit()

