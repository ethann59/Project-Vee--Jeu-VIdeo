# Importations des modules
import pygame, sys
<<<<<<< Updated upstream
# Importation des fichiers
import enemy_object_data, game_class, place_data

# Variables globales

version = "0.0.3"

# Variables du plateau
plateau_img = pygame.image.load("plateau.jpg")
plateau_img = pygame.transform.scale(plateau_img, (648, 644))
plateau_img_pos = (0, 0)

class Game:
    # Classe principale du jeu
    def __init__(self):
        # Initialisation du jeu (affichage, titre du jeu, etc...)
            self.ecran = pygame.display.set_mode((1000, 644)) # Change la taille de la fenêtre
        
            pygame.display.set_caption("Project Vee - Development Version " + version)
            self.jeu_lance = True # Pas toucher, maintient le jeu en marche
        
    def event_manager(self):
        # Gére les événements (clavier, souris, etc...)
    
        while self.jeu_lance: # Boucle principale du jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # A separer en une fonction distincte afin de se faire les transitions
            self.ecran.fill((255, 255, 255))
            self.ecran.blit(plateau_img, plateau_img_pos) 
        
            pygame.display.flip()
            
    def menu(self):
        # Menu principal du jeu
        pass
    
    def partie(self):
        # Plateau du jeu
        pass
        

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.event_manager()
    
=======
import pygame.font
import time
# Importation des fichiers
import place_data
import players, ennemis, objects, game_settings
#import enemy_object_data // C'est pour après le temps que je répare le progamme

# Variables globales

version = "0.0.4"

# Variables de la partie

duree_timer = game_settings.game_settings.time_limit


# Variables textuels

pygame.font.init()
font = pygame.font.Font(None, 36)  # Crée une police avec une taille de 36 points (vous pouvez ajuster la taille selon vos besoins)
texte = font.render("Votre texte ici", True, (55, 42, 60))  # Texte blanc avec antialiasing
timer_text = font.render("Temps restant : " + str(duree_timer), True, (55, 42, 60))


# Variables du plateau

Plateau = []

def inialize_plateau(n):
    for i in range(n):
        Plateau.append([n, ""])

plateau_img = pygame.image.load("img/scenes/plateau.jpg")
plateau_img = pygame.transform.scale(plateau_img, (648, 644))

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
        dessiner_bouton(250, 200, 500, 50, VERT, "Partie rapide")
        dessiner_bouton(250, 250, 500, 50, GRIS, "Partie personnalisée (non disponible)")
        dessiner_bouton(250, 300, 500, 50, ROUGE, "Quitter")

        pygame.display.flip()

# Fonction pour le jeu
def jeu(duree_timer):
    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
                pygame.quit()
                sys.exit()

        fenetre.fill(BLANC)  # Efface l'écran

        fenetre.fill((255, 255, 255))
        fenetre.blit(plateau_img, (0,0))
        fenetre.blit(timer_text, (700, 10)) # A changer pour afficher le timer

        pygame.display.flip()
        
        

# Boucle principale
while etat != None:
    if etat == ETAT_MENU:
        etat = menu_principal()
    elif etat == ETAT_JEU:
        jeu(duree_timer)

pygame.quit()
sys.exit()
>>>>>>> Stashed changes
