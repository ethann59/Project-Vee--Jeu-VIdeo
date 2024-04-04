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

Dave = Joueur()
Dave.setNom("Dave")
Dave.setImage("img/sprites/dave-human.png")

EnnemiTest = Ennemi()
EnnemiTest.setNom("EnnemiTest")
EnnemiTest.setImage("img/sprites/plagiat-murder-drones-lol.png")

joueur = Dave
ennemi = EnnemiTest
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



fenetre.blit(Dave.image, (50, 300))
fenetre.blit(EnnemiTest.image, (200, 300))


# Affichez les PV du joueur et de l'ennemi

fenetre.blit(text_pv_player, (50, 100))

fenetre.blit(text_pv_enemy, (50, 150))
    
        
pygame.display.flip()

# Stocker le texte dans une variable pour le changer sur l'affichage
# Penser à afficher les images des ennemis et du joueur
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
                            
                
    




pygame.quit()

