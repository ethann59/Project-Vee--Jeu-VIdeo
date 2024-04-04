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


argent_joueur = Dave.gold

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

# Afficher les articles

fenetre.blit(texte, (50,300))

        
pygame.display.flip()

# Stocker le texte dans une variable pour le changer sur l'affichage
# Penser à afficher les images des ennemis et du joueur
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False


pygame.quit()
