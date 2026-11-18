import pygame
import sys
# Path permet de construire des chemins de fichiers qui fonctionnent
# correctement, même si le programme est lancé depuis un autre dossier.
from pathlib import Path


pygame.init()


largeur, hauteur = 960, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Anti-Virus")

# __file__ contient le chemin de ce fichier main.py.
# resolve() transforme ce chemin en chemin absolu et élimine les raccourcis.
# parent récupère uniquement le dossier qui contient main.py.
# Exemple : .../jeux-/main.py devient .../jeux-/
DOSSIER_PROJET = Path(__file__).resolve().parent

# Construit le chemin complet d'un asset situé dans le dossier assets.
# Le paramètre nom correspond uniquement au nom du fichier, par exemple
# "Virus.png". La fonction renvoie une chaîne utilisable par pygame.
def chemin_asset(nom):
    return str(DOSSIER_PROJET / "assets" / nom)

# On utilise la fonction au lieu d'écrire directement "assets/...".
# Cela évite les erreurs lorsque VS Code lance le programme depuis un autre
# dossier que celui du projet.
fond = pygame.image.load(chemin_asset("bgLevelSelect.jpg")).convert()

class Molecule:
    
    def __init__(self, nom, image_path, x, y):
        self.nom = nom                 
        # image_path est déjà le chemin complet créé par chemin_asset().
        # convert_alpha() conserve la transparence des PNG.
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))             

    
    def afficher(self, fenetre):
        fenetre.blit(self.image, self.rect)    
# Chargement des deux arrière-plans avec des chemins indépendants du dossier
# depuis lequel le programme a été lancé.
fond_menu = pygame.image.load(chemin_asset("bgLevelSelect.jpg")).convert()
fond_jeu = pygame.image.load(chemin_asset("download.jpg")).convert()
ecran = "menu"  # Peut valoir "menu" ou "jeu"

class Bouton:
    def __init__(self, nom, image_path, x, y):
        self.nom = nom
        # Le bouton utilise la même logique de chemin que les molécules.
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def afficher(self, fenetre):
        fenetre.blit(self.image, self.rect)

# liste des molécules, position diff pour eviter superposition 
molecules = [
    Molecule("virus", chemin_asset("Virus.png"), 40, 40),
    Molecule("bleue 2", chemin_asset("Blue_2.png"), 220, 80),
    Molecule("bleue 3", chemin_asset("Blue_3.png"), 470, 70),
    Molecule("verte 2", chemin_asset("Green_2.png"), 220, 270),
    Molecule("verte 3", chemin_asset("Green_3.png"), 40, 220),
    Molecule("orange 3", chemin_asset("Orange_3.png"), 700, 60),
    Molecule("rose 2", chemin_asset("Pink_2.png"), 470, 250),
    Molecule("violette 3", chemin_asset("Purple_3.png"), 700, 300),
    Molecule("jaune 3", chemin_asset("Yellow_3.png"), 40, 400),
]

boutons = [
    Bouton("start_button", chemin_asset("Startbutton.png"), 400, 300),
]
# Bouton pour revenir au menu depuis l'écran de jeu
bouton_retour = Bouton("retour", chemin_asset("Startbutton.png"), 20, 20) 
# (Tu peux adapter les coordonnées 20, 20 et la taille si besoin)
# Variables pour la gestion du déplacement
piece_selectionnee = None
decal_x = 0
decal_y = 0
en_cours = True
while en_cours:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.MOUSEBUTTONDOWN and ecran == "menu":
            for bouton in boutons:
                if bouton.rect.collidepoint(event.pos):
                    ecran = "jeu"
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ecran == "menu":
            for bouton in boutons:
                if bouton.rect.collidepoint(event.pos):
                    ecran = "jeu"
        elif ecran == "jeu":
                # On vérifie d'abord si on clique sur le bouton retour
                if bouton_retour.rect.collidepoint(event.pos):
                    ecran = "menu"
                else:
                    # Sinon, on vérifie si on attrape une molécule
                    for molecule in reversed(molecules):
                        if molecule.rect.collidepoint(event.pos):
                            piece_selectionnee = molecule
                            decal_x = molecule.rect.x - event.pos[0]
                            decal_y = molecule.rect.y - event.pos[1]
                            break

    if event.type == pygame.MOUSEMOTION and ecran == "jeu":
        if piece_selectionnee is not None:
            piece_selectionnee.rect.x = event.pos[0] + decal_x
            piece_selectionnee.rect.y = event.pos[1] + decal_y

    if event.type == pygame.MOUSEBUTTONUP and ecran == "jeu":
            if piece_selectionnee is not None:
                # Définis ici la taille d'une case de ta grille (en pixels) 
                # et l'origine (le coin haut-gauche de la grille sur ton image)
                taille_case = 60  # À ajuster si tes cases sont un peu plus grandes ou plus petites
                origine_x = 150   # Coordonnée X du début de la grille sur l'image (à ajuster)
                origine_y = 100   # Coordonnée Y du début de la grille sur l'image (à ajuster)

                # On calcule la colonne et la ligne la plus proche
                colonne = round((piece_selectionnee.rect.x - origine_x) / taille_case)
                ligne = round((piece_selectionnee.rect.y - origine_y) / taille_case)

                # On replace la pièce exactement sur la case calculée
                piece_selectionnee.rect.x = origine_x + (colonne * taille_case)
                piece_selectionnee.rect.y = origine_y + (ligne * taille_case)

                # On libère la pièce
                piece_selectionnee = None
    if ecran == "menu":
        fenetre.blit(fond_menu, (0, 0))

        for bouton in boutons:
            bouton.afficher(fenetre)

    elif ecran == "jeu":
        fenetre.blit(fond_jeu, (0, 0))
        for molecule in molecules:
            molecule.afficher(fenetre)
        
        # --- C'est ici qu'il faut placer l'étape 3 ---
        bouton_retour.afficher(fenetre)

    pygame.display.flip()
# ntm sale fdp
pygame.quit()
sys.exit()
print("hippolyte est gay")