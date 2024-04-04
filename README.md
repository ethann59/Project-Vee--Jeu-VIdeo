# Aexo - Le plan de James (Project Vee - Sae Jeu Video)

## Description

Jeu vidéo réalisé dans le cadre de la SAE Jeu Vidéo. Le principe du jeu fusionne RPG et Monopoly en un seul jeu. Le joueur doit se déplacer sur un plateau de jeu et doit combattre les sbires de James le magician. Le joueur peut acheter des items et des armes pour se préparer au combat final contre James. Il peut aussi combattre les autres joueurs pour les affaiblir mais aussi leur voler l'un des 4 items qu'il faut pour localiser et donc vaincre James.

Dans le cadre de ce projet, les parties rapides sont limités à 15 minutes. Le joueur qui a le plus de points à la fin de la partie gagne dans ce cas.

## Note de version

Malgré le fait que le jeu soit jouable notamment le déplacement qui marche, le jeu n'est clairement pas fini. Il manque le système d'inventaire notamment et il y a pas mal de bugs. Il est jouable mais il n'est pas fini.

Il y a deux fichiers preview que j'ai utilisé pour le trailer mais ça donne que un visuel (visuel qui ne représente pas le jeu final).

## Installation

### Prérequis

Pour pouvoir lancer le jeu, il faut avoir installé Python 3.11 ou plus. Il faut aussi avoir installé la librairie Pygame.
Vous pouvez tenter une version antérieur de Python mais je ne garantis pas que le jeu fonctionne.

L'installation de Python varie en fonction de votre plateforme. Pour Windows, il suffit de télécharger le fichier d'installation sur le site officiel de Python et de l'installer. Pour Debian et Ubuntu, il suffit de taper la commande suivante dans un terminal :

```bash
sudo apt install python3
```

Pour l'installation de Pygame, il suffit de taper la commande suivante dans un terminal :

```bash
pip3 install pygame
```

### Installation du jeu

Pour installer le jeu, il suffit de télécharger le fichier .zip et de l'extraire dans un dossier. Ensuite, il faut lancer le fichier "main.py" pour lancer le jeu.

## Utilisation

### Régles du jeu

Les joueurs commencent tous à la case départ. Les joueurs lancent le dée et font le tour du plateau. Le but est de battre les sbires de James afin de récupérer les 4 items qui permettent de localiser James. Le premier joueur qui bat James gagne la partie. Si le temps est écoulé, le joueur qui a le plus de points gagne la partie.

Le score est calculé en fonction de l'or, des points de vie, les ennemis tués et des items de quete en possession du joueur.

#### Combat

Le mode Combat se déclenche si un ennemi apparait aléatoirement, si il tombe sur la case avec un sbire de James ou un autre joueur. Le mode est simple. Le joueur a le choix entre 4 actions : Attaquer, Défendre, Fuir et Inventaire. Attaquer inflige des dégats à l'ennemi selon vos points de dégats. Défendre réduit les dégats reçus en fonction de votre oublier. Fuir vous fait perdre le combat et vous fait perdre 1 point de vie. Si vous perdez tous vos points de vie, vous perdez le combat et vous retournez à la case départ. Si l'ennemi perd tous ses points de vie, vous gagnez le combat et vous gagnez de l'or. Si l'ennemi est un sbires de James, vous gagnez son item. Si l'ennemi est un joueur, vous lui volez un item aléatoire.

#### Inventaire

L'inventaire est simple. Il permet de voir les items que vous avez en votre possession. Le joueur ne peut utiliser les items que en combat.

#### Case spéciaux

##### Marché

La case "Marché" permet au joueur d'acheter des items et des armes.

Liste des objets disponibles à l'achat :

Potion de vie : Rend de la vie au joueur. Le joueur ne peut pas dépasser ses points de vie maximum.
Champ de force : Augmente la défense du joueur temporairment.
Grenade flash : Aveugle l'ennemi et lui inflige des dégats.
Pistolet-mitrailleur : Augmente les dégats du joueur. Automatiquement équipé.
Gillet pare-balles : Augmente la défense du joueur. Automatiquement équipé.

##### Hôpital

La case "Hôpital" permet au joueur de récupérer la totalité de ses points de vie si il en a les capacités. Le joueur tombe aussi sur cette case si il perd un combat. Il n'obtient pas les 200 d'or en passant par la case départ dans ce cas.

##### Police et Prison

En mode "Combat", le joueur a une infime chance de se faire attraper par la police. Si il se fait attraper, il est envoyé en prison. Il doit payer 100 d'or pour sortir de prison. Si il n'a pas assez d'or, il doit attendre 3 tours pour sortir de prison. Si il n'a pas assez d'or après 3 tours, il est libéré quand même.


## Credits & Licence

Merci ELUECQUE Anthony et DUVET Alexandre pour l'aide au codage
Merci à The Skindex pour l'outil qui a servi à réalisé des personnages
Merci à Freepik, Khoon Lay Gan et Pngtree pour les pictogrammes utilisés dans le jeu
Le background a été réalisé avec DALL-E 3 via Bing

## Patch notes

### Patch 0.0.7 R2

Finalisation du référencement des cases, mise en place d'un placement aléatoire des ennemis importants.
Début de codage d'un système de déplacement.
Nettoyage du code.

### Patch 0.0.7 R3

Système de déplacement fini. Il reste plus que réparer le bug avec les gros cases et l'affichage des dés.

### Patch 0.0.8

Système de déplacement optimisé. Collistion entre joueurs réalité. Début de codage du système de combat et de case.
Mise à jour visuelle des cases.

### Patch 0.1.0

Système de combat fini.
Système de case spéciaux (magasin, hopital, etc) fini.
Nouveau système de timer.
Il reste plus que le système d'inventaire.
