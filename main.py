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
fond_jeu = pygame.image.load(chemin_asset("backgroundPlayBoard.png")).convert()
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

en_cours = True
while en_cours:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.MOUSEBUTTONDOWN and ecran == "menu":
            for bouton in boutons:
                if bouton.rect.collidepoint(event.pos):
                    ecran = "jeu"

    if ecran == "menu":
        fenetre.blit(fond_menu, (0, 0))

        for bouton in boutons:
            bouton.afficher(fenetre)

    elif ecran == "jeu":
        fenetre.blit(fond_jeu, (0, 0))
        for molecule in molecules:
            molecule.afficher(fenetre)

    pygame.display.flip()

pygame.quit()
sys.exit()
