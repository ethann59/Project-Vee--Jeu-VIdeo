from pygame import *
from players import *
from ennemis import *
from enemy_data import *
import random
import main
from objects import *

def combat_pve(joueur : Joueur, ennemi : Ennemi): # Voir pour coder un inventaire au passage
    main.fenetre.fill(main.BLANC)
    # Variables de combat - Pour vérifier si les boucliers sont actifs
    enemyshield_on = 0
    playershield_on = 0
    show_inventory = False  # Au départ, l'inventaire est masqué
    grenade_flash_active = False
    enemy_pv_de_base = ennemi.pv
    
    # Variables textuels
    
    text_block_attack = main.font.render(("Il a bloqué l'attaque ! Il lui reste " + str(ennemi.pv) + " PV"), True, main.BLANC)
    text_normal_attack = main.font.render(("Il lui reste " + str(ennemi.pv) + " PV"), True, main.BLANC)
    text_prepare_shield = main.font.render(("Vous vous préparez votre bouclier."), True, main.BLANC)
    text_no_run = main.font.render(("Vous ne pouvez pas fuir, vous devez le tuer !"), True, main.BLANC)
    text_run = main.font.render(("Vous avez fui le combat."), True, main.BLANC)
    attack_text= main.font.render("Attaquer", True, main.BLANC)
    defend_text = main.font.render("Défendre", True, main.BLANC)
    flee_text = main.font.render("Fuir", True, main.BLANC)
    inventory_text = main.font.render("Inventaire", True, main.BLANC)
    text_pv_player = main.font.render(("Vous avez " + str(joueur.pv) + " PV"), True, main.BLANC)
    text_pv_enemy = main.font.render(("L'ennemi a " + str(ennemi.pv) + " PV"), True, main.BLANC)
    text_shield_player = main.font.render(("Vous avez votre bouclier activé"), True, main.BLANC)
    text_no_shield_player = main.font.render(("Vous avez votre bouclier désactivé"), True, main.BLANC)
    text_grenade_flash = main.font.render(("L'ennemi est aveuglé"), True, main.BLANC)
    text_attack_enemy = main.font.render(("L'ennemi attaque"), True, main.BLANC)
    text_block_attack_enemy = main.font.render(("Vous avez bloqué l'attaque ! Il vous reste " + str(joueur.pv) + " PV"), True, main.BLANC)
    text_defend_enemy = main.font.render(("L'ennemi se défend"), True, main.BLANC)
    text_police = main.font.render(("Wuwu ! Ceci est une descente de la police !"), True, main.BLANC)
    text_lose = main.font.render(("Vous avez perdu !"), True, main.BLANC)
    text_win = main.font.render(("Vous avez gagné ! Vous avez obtenu " + str(ennemi.gold)), True, main.BLANC)
    if isinstance(ennemi, EnnemiImportant):
        text_quest_object = main.font.render(("Vous avez obtenu un objet de quête !" + str(ennemi.quest_object.name)), True, main.BLANC)
    
    
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
                        main.fenetre.blit(text_block_attack, (50, 50))                    
                    if enemyshield_on == 0:
                        ennemi.pv -= joueur.patt
                        main.fenetre.blit(text_normal_attack, (50, 50))
                elif defend_button.collidepoint(event.pos):
                    # Logique de défense
                    # Réduisez les dégâts subis par le joueur ou augmentez sa défense
                    playershield_on = 1
                    main.fenetre.blit(text_prepare_shield, (50, 50))
                elif flee_button.collidepoint(event.pos):
                    # Logique de fuite
                    # Terminez la partie ou retournez à un écran précédent
                    if isinstance(ennemi, EnnemiImportant):
                        main.fenetre.blit(text_no_run, (50, 50))
                    else:
                        main.fenetre.blit(text_run, (50, 50))
                        return joueur.pv, joueur.gold
            
    # Affichez les boutons
    pygame.draw.rect(main.fenetre, main.BLEU, defend_button)
    pygame.draw.rect(main.fenetre, main.VERT, flee_button)
    pygame.draw.rect(main.fenetre, main.ROUGE, attack_button)
    pygame.draw.rect(main.fenetre, main.BLEU, inventory_button)  # Bouton vert pour l'inventaire

    # Affichez les textes des boutons
    
    main.fenetre.blit(attack_text, (attack_button.x + 10, attack_button.y + 10))
    main.fenetre.blit(defend_text, (defend_button.x + 10, defend_button.y + 10))
    main.fenetre.blit(flee_text, (flee_button.x + 10, flee_button.y + 10))
    main.fenetre.blit(inventory_text, (inventory_button.x + 10, inventory_button.y + 10))
    
    
    # Afficher l'inventaire si le bouton est cliqué
    # Si l'inventaire est affiché, dessinez le contenu de l'inventaire ici
    if show_inventory:
    # Dessinez les éléments de l'inventaire
    # Par exemple, affichez une liste d'objets avec des quantités
    # Assurez-vous de positionner et de styliser correctement l'affichage de l'inventaire
    # Vous pouvez utiliser une boucle pour parcourir les éléments de l'inventaire et les afficher
        pass
    # Affichez les PV du joueur et de l'ennemi
    
    main.fenetre.blit(text_pv_player, (50, 100))
    
    main.fenetre.blit(text_pv_enemy, (50, 150))
        
    if playershield_on == 1:
        main.fenetre.blit(text_shield_player, (50, 150))
    if playershield_on == 0:
        main.fenetre.blit(text_no_shield_player, (50, 150))
    
    # Coder le système de bouclier temporaire
    if joueur.pam_temp_duree > 0:
        joueur.pam_temp_duree -= 1
    elif joueur.pam_temp_duree == 0:
        joueur.pam = 0
        joueur.pam_temp_duree = 0
    
    # Choix de l'ennemi
    if grenade_flash_active == True:
        main.fenetre.blit(text_grenade_flash, (50, 250))
        temp_turn += 1
        if temp_turn == 2:
            grenade_flash_active = False
            temp_turn = 0
    else:
        ennemi_choice = random.randint(1, 2)
        if ennemi_choice == 1:
            main.fenetre.blit(text_attack_enemy, (50, 250))
            if playershield_on == 1:
                joueur.pv -= (ennemi.patt - joueur.pam)
                main.fenetre.blit(text_block_attack, (50, 300))
            if playershield_on == 0:
                joueur.pv -= ennemi.patt
                main.fenetre.blit(text_pv_player, (50, 300))
        if ennemi_choice == 2:
            main.fenetre.blit(text_defend_enemy, (50, 250))
            enemyshield_on = 1
        
    # Pensez à coder l'event "police"
    if random.randint(0, 100) <= joueur.proba_police:
        main.fenetre.blit(text_police, (50, 250))
        joueur.setCase(7)
        joueur.setKo(False)
        joueur.activatePrison()
        return joueur.pv, joueur.gold
        
    # Conditions de victoire et de défaite
    if joueur.pv <= 0:
        main.fenetre.blit(text_lose, (50, 350))
        joueur.setCase(20)
        joueur.setKo(True)
        return joueur.pv, joueur.gold
    if ennemi.pv <= 0:
        main.fenetre.blit(text_win, (50, 350))
        joueur.gold += ennemi.gold
        joueur.addScore(enemy_pv_de_base)
        if isinstance(ennemi, EnnemiImportant):
            joueur.inventaire.append(ennemi.quest_object)
            main.fenetre.blit(text_quest_object, (50, 400))
        
    
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
    joueur_actif = joueur1
    
    # Créez des boutons "Attaquer", "Défendre" et "Fuir"
    defend_button = pygame.Rect(200, 200, 100, 50)
    flee_button = pygame.Rect(350, 200, 100, 50)
    attack_button = pygame.Rect(50, 200, 100, 50)  # Zone cliquable du bouton d'attaque
    inventory_button = pygame.Rect(500, 200, 100, 50)
    
    # Variables textuels
    text_police = main.font.render(("Wuwu ! Ceci est une descente de la police !"), True, main.BLANC)
    
    # Stocker le texte dans une variable pour le changer sur l'affichage
    # Penser à afficher les images des ennemis et du joueur
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if joueur_actif == joueur1:
                    if attack_button.collidepoint(event.pos):
                        # Logique d'attaque
                        # Réduisez les PV de l'ennemi ou augmentez les dégâts du joueur
                        if player2shield_on == 1:
                            joueur2.pv -= (joueur1.patt - joueur2.pam)
                            main.fenetre.blit(("Il a bloqué l'attaque ! Il lui reste " + str(joueur2.pv) + " PV"), (50, 50))                    
                        if player2shield_on == 0:
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
                if joueur_actif == joueur2:
                    if attack_button.collidepoint(event.pos):
                        # Logique d'attaque
                        # Réduisez les PV de l'ennemi ou augmentez les dégâts du joueur
                        if player1shield_on == 1:
                            joueur1.pv -= (joueur2.patt - joueur1.pam)
                            main.fenetre.blit(("Il a bloqué l'attaque ! Il lui reste " + str(joueur1.pv) + " PV"), (50, 50))                    
                        if player1shield_on == 0:
                            joueur1.pv -= joueur2.patt
                            main.fenetre.blit(("Il lui reste " + str(joueur1.pv) + " PV"), (50, 50))
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
    
    main.fenetre.blit((joueur1.name, " a " + str(joueur1.pv) + " PV"), (50, 100))
    
    main.fenetre.blit((joueur1.name, " a " + str(joueur2.pv) + " PV"), (50, 150))
        
    if player1shield_on == 1:
        main.fenetre.blit(("Vous avez votre bouclier activé"), (50, 150))
    if player2shield_on == 0:
        main.fenetre.blit(("Vous avez votre bouclier désactivé"), (50, 150))
    
       # Coder le système de bouclier temporaire
    if joueur1.pam_temp_duree > 0:
        joueur1.pam_temp_duree -= 1
    elif joueur1.pam_temp_duree == 0:
        joueur1.pam = 0
        joueur1.pam_temp_duree = 0
    
    # Coder le système de bouclier temporaire
    if joueur2.pam_temp_duree > 0:
        joueur2.pam_temp_duree -= 1
    elif joueur2.pam_temp_duree == 0:
        joueur2.pam = 0
        joueur2.pam_temp_duree = 0
    
        
    # Pensez à coder l'event "police"
    if random.randint(0, 100) <= joueur1.proba_police or random.randint(0, 100) <= joueur2.proba_police:
        main.fenetre.blit(text_police, (50, 250))
        joueur1.setCase(7)
        joueur1.setKo(False)
        joueur1.activatePrison()
        joueur2.setCase(7)
        joueur2.setKo(False)
        joueur2.activatePrison()
        return joueur1.pv, joueur1.gold, joueur2.pv, joueur2.gold
    
    if joueur_actif == joueur1:
        joueur_actif = joueur2
        
    # Conditions de victoire et de défaite
    if joueur1.pv <= 0:
        main.fenetre.blit(("Vous avez perdu !"), (50, 350))
        joueur1.setCase(20)
        joueur1.setKo(True)
        return joueur1.pv, joueur1.gold
    if joueur2.pv <= 0:
        main.fenetre.blit(("Vous avez gagné !"), (50, 350))
        joueur1.gold += joueur2.gold
        joueur2.setCase(20)
        joueur2.setKo(True)
        # Vérifier si le joueur 2 a un objet de quête et si il en a un, de piocher parmi ce qu'il a, et de le donner au joueur 1
        if QuestObject in joueur2.inventaire:
            # On liste les objets de quête que le joueur 2 a
            j2_quest_objects = []
            for i in joueur2.inventaire:
                if isinstance(i, QuestObject):
                    j2_quest_objects.append(i)
            # On en choisit un au hasard
            j2_quest_object = random.choice(j2_quest_objects)
            # On le donne au joueur 1
            joueur1.inventaire.append(j2_quest_object)
            # On le retire du joueur 2
            joueur2.inventaire.remove(j2_quest_object)
        return joueur1.pv, joueur1.gold
            
        

