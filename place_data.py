import settings as gc
from object_data import items_disponibles
import pygame
from main import BLANC, font, fenetre


def hospital(joueur):
    # Création du fond du menu
    menu_surface = pygame.Surface((400, 200))
    menu_surface.fill(BLANC)
    menu_surface.set_alpha(200)  # Transparence du fond

    # Affichage du texte
    texte_surface = font.render("Hôpital", True, BLANC)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (200, 50)

    # Affichage du coût des soins
    cout_surface = font.render(f"Soins (Coût : {gc.settings.hopital_price} pièces)", True, BLANC)
    cout_rect = cout_surface.get_rect()
    cout_rect.center = (200, 100)

    # Affichage du bouton "Se soigner"
    bouton_se_soigner = pygame.Rect(150, 150, 200, 40)
    pygame.draw.rect(menu_surface, BLANC, bouton_se_soigner)
    bouton_surface = font.render("Se soigner", True, BLANC)
    bouton_rect = bouton_surface.get_rect()
    bouton_rect.center = bouton_se_soigner.center
    
     # Affichage du bouton "Ne pas se soigner"
    bouton_ne_pas_se_soigner = pygame.Rect(400, 150, 200, 40)
    pygame.draw.rect(menu_surface, BLANC, bouton_ne_pas_se_soigner)
    bouton_ne_pas_se_soigner_surface = font.render("Ne pas se soigner", True, BLANC)
    bouton_ne_pas_se_soigner_rect = bouton_ne_pas_se_soigner_surface.get_rect()
    bouton_ne_pas_se_soigner_rect.center = bouton_ne_pas_se_soigner.center


    # Affichage du menu
    fenetre.blit(menu_surface, (200, 200))
    fenetre.blit(texte_surface, texte_rect)
    fenetre.blit(cout_surface, cout_rect)
    fenetre.blit(bouton_surface, bouton_rect)
    
    # Variables textuelles
    texte_soin = font.render("Vous vous êtes soigné à l'hôpital. Vie restaurée à {settings.pv_player} points.", True, BLANC)
    texte_argent = font.render("Argent restant : {joueur.gold} pièces d'or.", True, BLANC)
    texte_pas_soin = font.render("Désolé, vous n'avez pas assez d'argent pour vous soigner à l'hôpital.", True, BLANC)

    # Vérifie si le joueur clique sur le bouton "Se soigner"
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_se_soigner.collidepoint(event.pos):
                # Vérifie si le joueur a suffisamment d'argent pour se soigner
                if joueur.gold >= gc.settings.hopital_price:
                    joueur.pv = gc.settings.pv_player  # Réinitialise la vie du joueur à son maximum
                    joueur.gold -= gc.settings.hopital_price  # Déduit le coût des soins de l'argent du joueur
                    fenetre.blit(texte_soin, (200, 250))
                    fenetre.blit(texte_argent, (200, 300))
                    return joueur.pv, joueur.gold
                else:
                    fenetre.blit(texte_pas_soin, (200, 250))

        
def shop(argent_joueur, inventaire_joueur):
    while True:
        fenetre.fill((255, 255, 255))
        # Afficher la liste des objets disponibles avec leurs prix
        y = 50
        for item in items_disponibles:
            texte = font.render(f"{item.nom}: {item.prix} pièces d'or", True, (0, 0, 0))
            fenetre.blit(texte, (50, y))
            y += 30
        
        # Afficher l'argent du joueur
        texte_argent = font.render(f"Argent du joueur: {argent_joueur} pièces d'or", True, (0, 0, 0))
        fenetre.blit(texte_argent, (50, 10))
        
        # Variables textuelles
        texte_achat = font.render("Vous avez acheté un objet.", True, (0, 0, 0))
        texte_argent = font.render(f"Argent restant : {argent_joueur} pièces d'or.", True, (0, 0, 0))

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
                                fenetre.blit(texte_achat, (50, 250))
                            else:
                                # Le joueur n'a pas assez d'argent pour acheter l'objet
                                fenetre.blit(texte_argent, (50, 300))
                                pygame.display.flip()
                            
        return argent_joueur, inventaire_joueur
                                

def prison(joueur):
    '''Cette fonction sert à controler le joueur quand il est en prison notamment le bloquer tant que il a pas fait 3 tours'''
    
    # Variables textuelles
    
    text_sortie = font.render("Vous êtes sorti de prison.", True, BLANC)
    text_prison = font.render("Vous êtes en prison, vous devez attendre 3 tours.", True, BLANC)
    text_caution = font.render("Voulez-vous payer 100 pièces d'or pour sortir de prison ? (Y/N)", True, BLANC)
    text_argent = font.render("Vous n'avez pas assez d'argent pour payer la caution.", True, BLANC)
    
    if joueur.prison == True:
        if joueur.prison_timer == 3:
            joueur.prison = False
            joueur.prison_timer = 0
            fenetre.blit(text_sortie, (200, 250))
        else:
            joueur.prison_timer += 1
            fenetre.blit(text_prison, (200, 250))
            # Demande au joueur si il veut payer pour sortir de prison
            fenetre.blit(text_caution, (200, 300))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        if joueur.gold >= 100:
                            joueur.gold -= 100
                            joueur.prison = False
                            joueur.prison_timer = 0
                            fenetre.blit(text_sortie, (200, 250))
                        else:
                            fenetre.blit(text_argent, (200, 300))
                    elif event.key == pygame.K_n:
                        fenetre.blit(text_prison, (200, 250))
    return joueur.prison, joueur.prison_timer
