from pygame import *
from players import *
from ennemis import *
from enemy_data import *
import random
import main

def combat_pve(joueur : Joueur, ennemi : Ennemi): # Voir pour coder un inventaire au passage
    main.fenetre.fill(main.BLANC)
    # Variables de combat - Pour vérifier si les boucliers sont actifs
    enemyshield_on = 0
    playershield_on = 0
    show_inventory = False  # Au départ, l'inventaire est masqué
    grenade_flash_active = False
    enemy_pv_de_base = ennemi.pv
    
    # Créez des boutons "Attaquer", "Défendre" et "Fuir"
    defend_button = pygame.Rect(200, 200, 100, 50)
    flee_button = pygame.Rect(350, 200, 100, 50)
    attack_button = pygame.Rect(50, 200, 100, 50)  # Zone cliquable du bouton d'attaque
    inventory_button = pygame.Rect(500, 200, 100, 50)
    
    # Stocker le texte dans une variable pour le changer sur l'affichage
    # Penser à afficher les images des ennemis et du joueur
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if attack_button.collidepoint(event.pos):
                    # Logique d'attaque
                    # Réduisez les PV de l'ennemi ou augmentez les dégâts du joueur
                    if enemyshield_on == 1:
                        ennemi.pv -= (joueur.patt - ennemi.pam)
                        main.fenetre.blit(("Il a bloqué l'attaque ! Il lui reste " + str(ennemi.pv) + " PV"), (50, 50))                    
                    if enemyshield_on == 0:
                        ennemi.pv -= joueur.patt
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
    pygame.draw.rect(main.fenetre, main.BLEU, inventory_button)  # Bouton vert pour l'inventaire

    # Affichez les textes des boutons
    
    main.fenetre.blit(("Attaquer"), (attack_button.x + 10, attack_button.y + 10))
    main.fenetre.blit(("Défendre"), (defend_button.x + 10, defend_button.y + 10))
    main.fenetre.blit(("Fuir"), (flee_button.x + 10, flee_button.y + 10))
    main.fenetre.blit(("Inventaire"), (inventory_button.x + 10, inventory_button.y + 10))
    
    
    # Afficher l'inventaire si le bouton est cliqué
    # Si l'inventaire est affiché, dessinez le contenu de l'inventaire ici
    if show_inventory:
    # Dessinez les éléments de l'inventaire
    # Par exemple, affichez une liste d'objets avec des quantités
    # Assurez-vous de positionner et de styliser correctement l'affichage de l'inventaire
    # Vous pouvez utiliser une boucle pour parcourir les éléments de l'inventaire et les afficher
        pass
    # Affichez les PV du joueur et de l'ennemi
    
    main.fenetre.blit(("Vous avez " + str(joueur.pv) + " PV"), (50, 100))
    
    main.fenetre.blit(("L'ennemi a " + str(ennemi.pv) + " PV"), (50, 150))
        
    if playershield_on == 1:
        main.fenetre.blit(("Vous avez votre bouclier activé"), (50, 150))
    if playershield_on == 0:
        main.fenetre.blit(("Vous avez votre bouclier désactivé"), (50, 150))
    
    # Coder le système de bouclier temporaire
    
    # Choix de l'ennemi
    if grenade_flash_active == True:
        main.fenetre.blit(("L'ennemi est aveuglé"), (50, 250))
        temp_turn += 1
        if temp_turn == 2:
            grenade_flash_active = False
            temp_turn = 0
    else:
        ennemi_choice = random.randint(1, 2)
        if ennemi_choice == 1:
            main.fenetre.blit(("L'ennemi attaque"), (50, 250))
            if playershield_on == 1:
                joueur.pv -= (ennemi.patt - joueur.pam)
                main.fenetre.blit(("Vous avez bloqué l'attaque ! Il vous reste " + str(joueur.pv) + " PV"), (50, 300))
            if playershield_on == 0:
                joueur.pv -= ennemi.patt
                main.fenetre.blit(("Il vous reste " + str(joueur.pv) + " PV"), (50, 300))
        if ennemi_choice == 2:
            main.fenetre.blit(("L'ennemi se défend"), (50, 250))
            enemyshield_on = 1
        
    # Pensez à coder l'event "police"
        
    # Conditions de victoire et de défaite
    if joueur.pv <= 0:
        main.fenetre.blit(("Vous avez perdu !"), (50, 350))
        joueur.setCase(20)
        joueur.setKo(True)
        return joueur.pv, joueur.gold
    if ennemi.pv <= 0:
        main.fenetre.blit(("Vous avez gagné !"), (50, 350))
        joueur.gold += ennemi.gold
        joueur.addScore(enemy_pv_de_base)
        
    
    return joueur.pv, joueur.gold

def combat_pvp(joueur1: Joueur, joueur2: Joueur):
    print("combat pvp")
    return joueur1.pv, joueur2.pv

def combat_pvp_beta(joueur1: Joueur, joueur2: Joueur):
    main.fenetre.fill(main.BLANC)
    # Variables de combat - Pour vérifier si les boucliers sont actifs
    player1shield_on = 0
    player2shield_on = 0
    show_inventory = False  # Au départ, l'inventaire est masqué
    grenade_flash_active = False
    
    # Créez des boutons "Attaquer", "Défendre" et "Fuir"
    defend_button = pygame.Rect(200, 200, 100, 50)
    flee_button = pygame.Rect(350, 200, 100, 50)
    attack_button = pygame.Rect(50, 200, 100, 50)  # Zone cliquable du bouton d'attaque
    inventory_button = pygame.Rect(500, 200, 100, 50)
    
    # Stocker le texte dans une variable pour le changer sur l'affichage
    # Penser à afficher les images des ennemis et du joueur
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if attack_button.collidepoint(event.pos):
                    # Logique d'attaque
                    # Réduisez les PV de l'ennemi ou augmentez les dégâts du joueur
                    if enemyshield_on == 1:
                        joueur2.pv -= (joueur1.patt - joueur2.pam)
                        main.fenetre.blit(("Il a bloqué l'attaque ! Il lui reste " + str(joueur2.pv) + " PV"), (50, 50))                    
                    if enemyshield_on == 0:
                        joueur2.pv -= joueur1.patt
                        main.fenetre.blit(("Il lui reste " + str(joueur2.pv) + " PV"), (50, 50))
                elif defend_button.collidepoint(event.pos):
                    # Logique de défense
                    # Réduisez les dégâts subis par le joueur ou augmentez sa défense
                    playershield_on = 1
                    main.fenetre.blit(("Vous vous préparez votre bouclier."), (50, 50))
                elif flee_button.collidepoint(event.pos):
                    # Logique de fuite
                    # Terminez la partie ou retournez à un écran précédent
                    main.fenetre.blit(("Vous avez fui le combat."), (50, 50))
                    return joueur1.pv, joueur2.pv
            
    # Affichez les boutons
    pygame.draw.rect(main.fenetre, main.BLEU, defend_button)
    pygame.draw.rect(main.fenetre, main.VERT, flee_button)
    pygame.draw.rect(main.fenetre, main.ROUGE, attack_button)
    pygame.draw.rect(main.fenetre, main.BLEU, inventory_button)  # Bouton vert pour l'inventaire

    # Affichez les textes des boutons
    
    main.fenetre.blit(("Attaquer"), (attack_button.x + 10, attack_button.y + 10))
    main.fenetre.blit(("Défendre"), (defend_button.x + 10, defend_button.y + 10))
    main.fenetre.blit(("Fuir"), (flee_button.x + 10, flee_button.y + 10))
    main.fenetre.blit(("Inventaire"), (inventory_button.x + 10, inventory_button.y + 10))
    
    
    # Afficher l'inventaire si le bouton est cliqué
    # Si l'inventaire est affiché, dessinez le contenu de l'inventaire ici
    if show_inventory:
    # Dessinez les éléments de l'inventaire
    # Par exemple, affichez une liste d'objets avec des quantités
    # Assurez-vous de positionner et de styliser correctement l'affichage de l'inventaire
    # Vous pouvez utiliser une boucle pour parcourir les éléments de l'inventaire et les afficher
        pass
    # Affichez les PV du joueur et de l'ennemi
    
    main.fenetre.blit(("Vous avez " + str(joueur.pv) + " PV"), (50, 100))
    
    main.fenetre.blit(("L'ennemi a " + str(ennemi.pv) + " PV"), (50, 150))
        
    if playershield_on == 1:
        main.fenetre.blit(("Vous avez votre bouclier activé"), (50, 150))
    if playershield_on == 0:
        main.fenetre.blit(("Vous avez votre bouclier désactivé"), (50, 150))
    
    # Coder le système de bouclier temporaire
    
    # Choix du joueur 2
    
        
    # Pensez à coder l'event "police"
        
    # Conditions de victoire et de défaite
    if joueur.pv <= 0:
        main.fenetre.blit(("Vous avez perdu !"), (50, 350))
        joueur.setCase(20)
        joueur.setKo(True)
        return joueur.pv, joueur.gold
    if ennemi.pv <= 0:
        main.fenetre.blit(("Vous avez gagné !"), (50, 350))
        joueur.gold += ennemi.gold
        joueur.addScore(enemy_pv_de_base)
        
    
    return joueur.pv, joueur.gold

