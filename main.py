# Importations des modules
import pygame, sys
import pygame.font
# Importation des fichiers
import game_class, place_data
#import enemy_object_data // C'est pour après le temps que je répare le progamme

# Variables globales

version = "0.0.4"

# Variables textuels

pygame.font.init()
font = pygame.font.Font(None, 36)  # Crée une police avec une taille de 36 points (vous pouvez ajuster la taille selon vos besoins)
texte = font.render("Votre texte ici", True, (55, 42, 60))  # Texte blanc avec antialiasing


# Variables du plateau
plateau_img = pygame.image.load("plateau.jpg")
plateau_img = pygame.transform.scale(plateau_img, (648, 644)) 

# Variables graphiques

taille_fenetre = (1000,644)

def dessiner_bouton(x, y, largeur, hauteur, couleur, texte, fenetre): #Méthode pour dessiner un bouton
    pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur))
    font = pygame.font.Font(None, 36)
    texte_surface = font.render(texte, True, (0, 0, 0))
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (x + largeur / 2, y + hauteur / 2)
    fenetre.blit(texte_surface, texte_rect)
    
# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)


# Initialisation du jeu (affichage, titre du jeu, etc...)
    ecran = pygame.display.set_mode(taille_fenetre) # Change la taille de la fenêtre

    pygame.display.set_caption("Project Vee - Development Version " + version)
    jeu_lance = True # Pas toucher, maintient le jeu en marche
    pygame.display.flip()
            
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

        ecran.fill(BLANC)  # Efface l'écran

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

        Game.ecran.fill(NOIR)  # Efface l'écran

        # Ajoutez ici le code de votre jeu

        pygame.display.flip()

# Boucle principale
while etat != None:
    if etat == ETAT_MENU:
        etat = menu_principal()
    elif etat == ETAT_JEU:
        jeu()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.event_manager()
    