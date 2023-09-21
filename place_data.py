<<<<<<< Updated upstream
def hospital(): #Généré par Copilot - A modifier pour le rendre compatible avec le jeu
    print("Vous êtes à l'hôpital")
    print("Vous pouvez vous soigner pour 10 golds")
    print("Vous pouvez aussi vous faire soigner gratuitement mais vous avez 50% de chance de mourir")
    print("1 - Se soigner pour 10 golds")
    print("2 - Se faire soigner gratuitement")
    print("3 - Quitter")
    choix = input("Choix : ")
    if choix == "1":
        if joueur.gold >= 10:
            joueur.gold -= 10
            joueur.pv = 100
            print("Vous avez été soigné")
        else:
            print("Vous n'avez pas assez d'argent")
    elif choix == "2":
        if random.randint(0,1) == 1:
            joueur.pv = 100
            print("Vous avez été soigné")
        else:
            joueur.pv = 0
            print("Vous êtes mort")
    elif choix == "3":
        print("Vous quittez l'hôpital")
    else:
        print("Erreur")
        hospital()
=======
import game_settings as gc

def hospital(): #Généré par Copilot - A modifier pour le rendre compatible avec le jeu
    # print("Vous êtes à l'hôpital")
    # print("Vous pouvez vous soigner pour 10 golds")
    # print("Vous pouvez aussi vous faire soigner gratuitement mais vous avez 50% de chance de mourir")
    # print("1 - Se soigner pour 10 golds")
    # print("2 - Se faire soigner gratuitement")
    # print("3 - Quitter")
    # choix = input("Choix : ")
    # if choix == "1":
    #     if gc.joueur.gold >= 10:
    #         gc.joueur.gold -= 10
    #         gc.joueur.pv = 100
    #         print("Vous avez été soigné")
    #     else:
    #         print("Vous n'avez pas assez d'argent")
    # elif choix == "2":
    #     if gc.random.randint(0,1) == 1:
    #         gc.joueur.pv = 100
    #         print("Vous avez été soigné")
    #     else:
    #         gc.joueur.pv = 0
    #         print("Vous êtes mort")
    # elif choix == "3":
    #     print("Vous quittez l'hôpital")
    # else:
    #     print("Erreur")
    #     hospital()
    
    pass
>>>>>>> Stashed changes
        
def shop():
    pass

def parc():
    pass

def prison():
    pass