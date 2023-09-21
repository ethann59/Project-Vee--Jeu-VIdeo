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

# États du jeu
etat = 0  # 0 = Menu principal, 1 = Jeu


class Game:
    # Classe principale du jeu
    def __init__(self):
        # Initialisation du jeu (affichage, titre du jeu, etc...)
            self.ecran = pygame.display.set_mode(taille_fenetre) # Change la taille de la fenêtre
        
            pygame.display.set_caption("Project Vee - Development Version " + version)
            self.jeu_lance = True # Pas toucher, maintient le jeu en marche

            pygame.display.flip()
            
    def jeu(self):
        self.jeu_lance = True
        while self.jeu_lance:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jeu_lance = False
                else:
                    self.ecran.fill((255, 255, 255))
                    self.ecran.blit(plateau_img, (0,0)) 
                    self.ecran.blit(texte, (670, 0)) # A modifier pour faire une vrai interface
         
    def event_manager(self):
        # Gére les événements (clavier, souris, etc...)
    
        while self.jeu_lance: # Boucle principale du jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # Vérifiez si un bouton a été cliqué
                    if 250 <= x <= 750 and 200 <= y <= 250:
                        Game.jeu(self)  # Transition vers le jeu - A régler
                    elif 250 <= x <= 750 and 300 <= y <= 350:
                        self.jeu_lance = False  # Action du bouton "Quitter"
                            
                self.ecran.fill((255, 255, 255))  # Efface l'écran
                
                dessiner_bouton(250, 200, 500, 50, VERT, "Jouer", self.ecran)
                dessiner_bouton(250, 300, 500, 50, ROUGE, "Quitter", self.ecran)

                pygame.display.flip()
        

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.event_manager()
    