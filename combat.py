from pygame import *
from players import *
from ennemis import *
from enemy_data import *
import random
import main

def combat(joueur : Joueur, ennemi : Ennemi):
    print("combat")
    return

def combat_beta(joueur : Joueur, ennemi : Ennemi): # Voir pour coder un inventaire au passage
    main.fenetre.fill(main.BLANC)
    # Variables de combat - Pour vérifier si les boucliers sont actifs
    enemyshield_on = 0
    playershield_on = 0
    
    # Créez des boutons "Attaquer", "Défendre" et "Fuir"
    defend_button = pygame.Rect(200, 200, 100, 50)
    flee_button = pygame.Rect(350, 200, 100, 50)
    attack_button = pygame.Rect(50, 200, 100, 50)  # Zone cliquable du bouton d'attaque
    
    # Stocker le texte dans une variable pour le changer sur l'affichage
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if attack_button.collidepoint(event.pos):
                    # Logique d'attaque
                    # Réduisez les PV de l'ennemi ou augmentez les dégâts du joueur
                    if enemyshield_on == 1:
                        ennemi.pv -= (joueur.attaque - ennemi.defense)
                        main.fenetre.blit(("Il a bloqué l'attaque ! Il lui reste " + str(ennemi.pv) + " PV"), (50, 50))                    
                    if enemyshield_on == 0:
                        ennemi.pv -= joueur.attaque
                        main.fenetre.blit(("Il lui reste " + str(ennemi.pv) + " PV"), (50, 50))
                elif defend_button.collidepoint(event.pos):
                    # Logique de défense
                    # Réduisez les dégâts subis par le joueur ou augmentez sa défense
                    playershield_on = 1
                    main.fenetre.blit(("Vous vous préparez votre bouclier."), (50, 50))
                elif flee_button.collidepoint(event.pos):
                    # Logique de fuite
                    # Terminez la partie ou retournez à un écran précédent
                    if isinstance(ennemi, EnnemiImportant):
                        main.fenetre.blit(("Vous ne pouvez pas fuir, vous devez le tuer !"), (50, 50))
                    else:
                        main.fenetre.blit(("Vous avez fui le combat."), (50, 50))
                        return joueur.pv, joueur.gold
            
    # Affichez les boutons
    pygame.draw.rect(main.fenetre, main.BLEU, defend_button)
    pygame.draw.rect(main.fenetre, main.VERT, flee_button)
    pygame.draw.rect(main.fenetre, main.ROUGE, attack_button)

    # Affichez les textes des boutons
    
    main.fenetre.blit(("Attaquer"), (attack_button.x + 10, attack_button.y + 10))
    main.fenetre.blit(("Défendre"), (defend_button.x + 10, defend_button.y + 10))
    main.fenetre.blit(("Fuir"), (flee_button.x + 10, flee_button.y + 10))
    
    # Affichez les PV du joueur et de l'ennemi
    
    main.fenetre.blit(("Vous avez " + str(joueur.pv) + " PV"), (50, 100))
        
    if playershield_on == 1:
        main.fenetre.blit(("Vous avez votre bouclier activé"), (50, 150))
    if playershield_on == 0:
        main.fenetre.blit(("Vous avez votre bouclier désactivé"), (50, 150))
        
    # Choix de l'ennemi
    ennemi_choice = random.randint(1, 2)
    if ennemi_choice == 1:
        main.fenetre.blit(("L'ennemi attaque"), (50, 250))
        if playershield_on == 1:
            joueur.pv -= (ennemi.attaque - joueur.defense)
            main.fenetre.blit(("Vous avez bloqué l'attaque ! Il vous reste " + str(joueur.pv) + " PV"), (50, 300))
            
        
    
    return joueur.pv, joueur.gold
