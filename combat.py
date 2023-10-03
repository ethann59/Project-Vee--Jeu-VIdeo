from pygame import *
from players import *
from ennemis import *
from enemy_data import *

def combat(joueur : Joueur, ennemi : Ennemi):
    print("combat")
    return

# def combat_beta(joueur : Joueur, ennemi : Ennemi): # Voir pour coder un inventaire au passage
    
    
#     # Créez des boutons "Attaquer", "Défendre" et "Fuir"
#     defend_button = pygame.Rect(200, 200, 100, 50)
#     flee_button = pygame.Rect(350, 200, 100, 50)
#     attack_button = pygame.Rect(50, 200, 100, 50)  # Zone cliquable du bouton d'attaque
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:  # Bouton gauche de la souris
#                 if attack_button.collidepoint(event.pos):
#                     # Logique d'attaque
#                     # Calcul des dégâts infligés par le joueur à l'ennemi
#                     ennemi.pv -= joueur.patt

#                     # Vérifier si l'ennemi est mort
#                     if ennemi.pv <= 0:
#                         ennemi.pv = 0
#                     # L'ennemi est vaincu, vous pouvez afficher un message de victoire ici

#                     # Laissez l'ennemi riposter (vous pouvez ajouter une certaine logique d'IA pour cela)
#                     # On ajoutera un random pour faire une pseudo IA
#                     joueur.pv -= ennemi.patt

#                     # Vérifier si le joueur est mort
#                     if joueur.pv <= 0:
#                         joueur.pv = 0
#                     # Le joueur est vaincu, vous pouvez afficher un message de défaite ici
#                 elif defend_button.collidepoint(event.pos):
#                     # Logique de défense
#                     # Réduisez les dégâts subis par le joueur ou augmentez sa défense
#                 elif flee_button.collidepoint(event.pos):
#                     # Logique de fuite
#                     # Terminez la partie ou retournez à un écran précédent


    
#     return joueur.pv, joueur.gold
