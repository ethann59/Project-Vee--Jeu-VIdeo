import settings as gc
from objects import *
from object_data import *
import main


# A finir
plateau_info = {
    0: {"x": 15, "y": 15, "lieu": "Départ"},
    1: {"x": 145, "y": 15, "lieu": ""},
    2: {"x": 210, "y": 15, "lieu": ""},
    3: {"x": 270, "y": 15, "lieu": ""},
    4: {"x": 335, "y": 15, "lieu": ""},
    5: {"x": 400, "y": 15, "lieu": ""},
    6: {"x": 465, "y": 15, "lieu": ""},
    7: {"x": 535, "y": 15, "lieu": "Prison"},
    8: {"x": 597, "y": 143, "lieu": ""},
    9: {"x": 597, "y": 207, "lieu": ""},
    10: {"x": 597, "y": 335, "lieu": ""},
    11: {"x": 597, "y": 399, "lieu": ""},
    12: {"x": 597, "y": 463, "lieu": ""},
    13: {"x": 535, "y": 532, "lieu": "Marché"},
    14: {"x": 467, "y": 593, "lieu": ""},
    15: {"x": 402, "y": 593, "lieu": ""},
    16: {"x": 337, "y": 593, "lieu": ""},
    17: {"x": 273, "y": 593, "lieu": ""},
    18: {"x": 209, "y": 593, "lieu": ""},
    19: {"x": 145, "y": 593, "lieu": ""},
    20: {"x": 15, "y": 527, "lieu": "Hopital"},
    21: {"x": 15, "y": 463, "lieu": ""},
    22: {"x": 15, "y": 400, "lieu": ""},
    23: {"x": 15, "y": 335, "lieu": ""},
    24: {"x": 15, "y": 270, "lieu": ""},
    25: {"x": 15, "y": 210, "lieu": ""},
    26: {"x": 15, "y": 335, "lieu": ""}
}

plateau_pos_alternatif = {
    "Départ": [(15, 15), (80, 15), (15, 80), (80, 80)], #Départ = 0
    "Prison": [(535, 15), (595, 15), (535, 80), (595, 595)], # Prison = 7
    "Marché": [(535, 532), (595, 532), (535, 595), (598, 595)], # Marché = 13
    "Hopital": [(15, 527), (80, 527), (15, 593), (80, 593)] # Hopital = 20
}

def hospital(joueur):
    # Création du fond du menu
    menu_surface = pygame.Surface((400, 200))
    menu_surface.fill(main.NOIR)
    menu_surface.set_alpha(200)  # Transparence du fond

    # Affichage du texte
    texte_surface = main.font.render("Hôpital", True, main.BLANC)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (200, 50)

    # Affichage du coût des soins
    cout_surface = main.font.render(f"Soins (Coût : {main.settings.hopital_price} pièces)", True, main.BLANC)
    cout_rect = cout_surface.get_rect()
    cout_rect.center = (200, 100)

    # Affichage du bouton "Se soigner"
    bouton_se_soigner = pygame.Rect(150, 150, 200, 40)
    pygame.draw.rect(menu_surface, main.BLANC, bouton_se_soigner)
    bouton_surface = main.font.render("Se soigner", True, main.NOIR)
    bouton_rect = bouton_surface.get_rect()
    bouton_rect.center = bouton_se_soigner.center
    
     # Affichage du bouton "Ne pas se soigner"
    bouton_ne_pas_se_soigner = pygame.Rect(400, 150, 200, 40)
    pygame.draw.rect(menu_surface, main.BLANC, bouton_ne_pas_se_soigner)
    bouton_ne_pas_se_soigner_surface = main.font.render("Ne pas se soigner", True, main.NOIR)
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
                if joueur.gold >= main.settings.hopital_price:
                    joueur.pv = main.settings.pv_player  # Réinitialise la vie du joueur à son maximum
                    joueur.gold -= main.settings.hopital_price  # Déduit le coût des soins de l'argent du joueur
                    main.fenetre.blit("Vous vous êtes soigné à l'hôpital. Vie restaurée à {main.settings.pv_player} points.", (200, 250))
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
                                print("Vous n'avez pas assez d'argent pour acheter cet objet.")
