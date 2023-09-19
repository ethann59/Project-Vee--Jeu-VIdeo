# Importations des modules
import pygame, sys
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
    