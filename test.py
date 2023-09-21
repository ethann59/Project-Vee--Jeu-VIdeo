#Code qui marche - à voir comment le transposer dans le code principal

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Configurer la fenêtre
largeur_fenetre = 1000
hauteur_fenetre = 644
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Menu Principal")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)

# Fonction pour dessiner un bouton
def dessiner_bouton(x, y, largeur, hauteur, couleur, texte, action=None):
    pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur))
    font = pygame.font.Font(None, 36)
    texte_surface = font.render(texte, True, NOIR)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (x + largeur / 2, y + hauteur / 2)
    fenetre.blit(texte_surface, texte_rect)

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
                elif 250 <= x <= 750 and 300 <= y <= 350:
                    en_cours = False  # Action du bouton "Quitter"

        fenetre.fill(BLANC)  # Efface l'écran

        # Dessinez vos boutons dans l'état du menu
        dessiner_bouton(250, 200, 500, 50, VERT, "Jouer")
        dessiner_bouton(250, 300, 500, 50, ROUGE, "Quitter")

        pygame.display.flip()

# Fonction pour le jeu
def jeu():
    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False

        fenetre.fill(NOIR)  # Efface l'écran

        # Ajoutez ici le code de votre jeu

        pygame.display.flip()

# Boucle principale
while etat != None:
    if etat == ETAT_MENU:
        etat = menu_principal()
    elif etat == ETAT_JEU:
        jeu()

pygame.quit()
sys.exit()
