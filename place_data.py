import settings as gc
from object_data import items_disponibles
import pygame
import main


def hospital(joueur):
    # Création du fond du menu
    menu_surface = pygame.Surface((400, 200))
    menu_surface.fill(main.BLANC)
    menu_surface.set_alpha(200)  # Transparence du fond

    # Affichage du texte
    texte_surface = main.font.render("Hôpital", True, main.BLANC)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (200, 50)

    # Affichage du coût des soins
    cout_surface = main.font.render(f"Soins (Coût : {gc.settings.hopital_price} pièces)", True, main.BLANC)
    cout_rect = cout_surface.get_rect()
    cout_rect.center = (200, 100)

    # Affichage du bouton "Se soigner"
    bouton_se_soigner = pygame.Rect(150, 150, 200, 40)
    pygame.draw.rect(menu_surface, main.BLANC, bouton_se_soigner)
    bouton_surface = main.font.render("Se soigner", True, main.BLANC)
    bouton_rect = bouton_surface.get_rect()
    bouton_rect.center = bouton_se_soigner.center
    
     # Affichage du bouton "Ne pas se soigner"
    bouton_ne_pas_se_soigner = pygame.Rect(400, 150, 200, 40)
    pygame.draw.rect(menu_surface, main.BLANC, bouton_ne_pas_se_soigner)
    bouton_ne_pas_se_soigner_surface = main.font.render("Ne pas se soigner", True, main.BLANC)
    bouton_ne_pas_se_soigner_rect = bouton_ne_pas_se_soigner_surface.get_rect()
    bouton_ne_pas_se_soigner_rect.center = bouton_ne_pas_se_soigner.center


    # Affichage du menu
    main.fenetre.blit(menu_surface, (200, 200))
    main.fenetre.blit(texte_surface, texte_rect)
    main.fenetre.blit(cout_surface, cout_rect)
    main.fenetre.blit(bouton_surface, bouton_rect)

    # Vérifie si le joueur clique sur le bouton "Se soigner"
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_se_soigner.collidepoint(event.pos):
                # Vérifie si le joueur a suffisamment d'argent pour se soigner
                if joueur.gold >= gc.settings.hopital_price:
                    joueur.pv = gc.settings.pv_player  # Réinitialise la vie du joueur à son maximum
                    joueur.gold -= gc.settings.hopital_price  # Déduit le coût des soins de l'argent du joueur
                    main.fenetre.blit("Vous vous êtes soigné à l'hôpital. Vie restaurée à {settings.pv_player} points.", (200, 250))
                    main.fenetre.blit("Argent restant : {joueur.gold} pièces d'or.", (200, 300))
                    return joueur.pv, joueur.gold
                else:
                    main.fenetre.blit("Désolé, vous n'avez pas assez d'argent pour vous soigner à l'hôpital.", (200, 250))

        
def shop(argent_joueur, inventaire_joueur):
    while True:
        main.fenetre.fill((255, 255, 255))
        # Afficher la liste des objets disponibles avec leurs prix
        y = 50
        for item in items_disponibles:
            texte = main.font.render(f"{item.nom}: {item.prix} pièces d'or", True, (0, 0, 0))
            main.fenetre.blit(texte, (50, y))
            y += 30
        
        # Afficher l'argent du joueur
        texte_argent = main.font.render(f"Argent du joueur: {argent_joueur} pièces d'or", True, (0, 0, 0))
        main.fenetre.blit(texte_argent, (50, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifier si un objet a été cliqué
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 50 <= mouse_x <= 250:
                    for i, item in enumerate(items_disponibles):
                        if 50 <= mouse_y <= 50 + 30 * (i + 1):
                            if argent_joueur >= item.prix:
                                # Le joueur a assez d'argent, il peut acheter l'objet
                                argent_joueur -= item.prix
                                # Ajouter l'objet à l'inventaire du joueur
                                inventaire_joueur.append(item)
                            else:
                                # Le joueur n'a pas assez d'argent pour acheter l'objet
                                main.fenetre.blit("Vous n'avez pas assez d'argent pour acheter cet objet.", (50, 300))
                                pygame.display.flip()
                            
        return argent_joueur, inventaire_joueur
                                

def prison(joueur):
    '''Cette fonction sert à controler le joueur quand il est en prison notamment le bloquer tant que il a pas fait 3 tours'''
    if joueur.prison == True:
        if joueur.prison_timer == 3:
            joueur.prison = False
            joueur.prison_timer = 0
            main.fenetre.blit("Vous êtes sorti de prison.", (200, 250))
        else:
            joueur.prison_timer += 1
            main.fenetre.blit("Vous êtes en prison, vous devez attendre 3 tours.", (200, 250))
    return joueur.prison, joueur.prison_timer
