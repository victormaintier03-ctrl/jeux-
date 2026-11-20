import sys
from pathlib import Path
import pygame

pygame.init()

# --- CONFIGURATION DE LA FENÊTRE ---
LARGEUR, HAUTEUR = 960, 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Anti-Virus")
horloge = pygame.time.Clock()

# --- GESTION DES CHEMINS ---
DOSSIER_PROJET = Path(__file__).resolve().parent


def chemin_asset(nom):
    return str(DOSSIER_PROJET / "assets" / nom)


# --- CLASSES ---
class Molecule:
    def __init__(self, nom, image_path, x, y):
        self.nom = nom
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def afficher(self, surface):
        surface.blit(self.image, self.rect)


class Bouton:
    def __init__(self, nom, image_path, x, y, niveau=None):
        self.nom = nom
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.niveau = niveau

    def afficher(self, surface):
        surface.blit(self.image, self.rect)


# --- RESSOURCES ET NIVEAUX ---
fond_menu = pygame.image.load(chemin_asset("bgLevelSelect.jpg")).convert()
fond_jeu = pygame.image.load(chemin_asset("download.jpg")).convert()

niveaux = {
    1: [
        ("virus", chemin_asset("Virus.png"), 40, 40),
        ("bleue 2", chemin_asset("Blue_2.png"), 220, 80),
        ("bleue 3", chemin_asset("Blue_3.png"), 470, 70),
        ("verte 2", chemin_asset("Green_2.png"), 220, 270),
        ("verte 3", chemin_asset("Green_3.png"), 40, 220),
        ("orange 3", chemin_asset("Orange_3.png"), 700, 60),
        ("rose 2", chemin_asset("Pink_2.png"), 470, 250),
        ("violette 3", chemin_asset("Purple_3.png"), 700, 300),
        ("jaune 3", chemin_asset("Yellow_3.png"), 40, 400),
    ],
    2: [
        ("virus", chemin_asset("Virus.png"), 220, 220),
        ("bleue 2", chemin_asset("Blue_2.png"), 100, 100),
        ("verte 3", chemin_asset("Green_3.png"), 350, 150),
        ("rose 2", chemin_asset("Pink_2.png"), 500, 250),
    ],
}

boutons_menu = [
    Bouton("niveau_1", chemin_asset("Startbutton.png"), 300, 250, niveau=1),
    Bouton("niveau_2", chemin_asset("Startbutton.png"), 520, 250, niveau=2),
]

bouton_retour = Bouton("retour", chemin_asset("Startbutton.png"), 20, 20)

# --- PARAMÈTRES DE LA GRILLE ---
TAILLE_CASE = 60
ORIGINE_X = 150
ORIGINE_Y = 100

# --- ÉTAT DU JEU ---
ecran = "menu"  # "menu" ou "jeu"
molecules = []
piece_selectionnee = None
decal_x = 0
decal_y = 0


def charger_niveau(num_niveau):
    global molecules, piece_selectionnee
    piece_selectionnee = None
    molecules = [
        Molecule(nom, image_path, x, y)
        for nom, image_path, x, y in niveaux[num_niveau]
    ]


# --- BOUCLE PRINCIPALE ---
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if ecran == "menu":
                for bouton in boutons_menu:
                    if bouton.rect.collidepoint(event.pos):
                        charger_niveau(bouton.niveau)
                        ecran = "jeu"
                        break

            elif ecran == "jeu":
                if bouton_retour.rect.collidepoint(event.pos):
                    piece_selectionnee = None
                    ecran = "menu"
                else:
                    for molecule in reversed(molecules):
                        if molecule.rect.collidepoint(event.pos):
                            piece_selectionnee = molecule
                            decal_x = molecule.rect.x - event.pos[0]
                            decal_y = molecule.rect.y - event.pos[1]
                            break

        elif event.type == pygame.MOUSEMOTION and ecran == "jeu":
            if piece_selectionnee is not None:
                piece_selectionnee.rect.x = event.pos[0] + decal_x
                piece_selectionnee.rect.y = event.pos[1] + decal_y

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and ecran == "jeu":
            if piece_selectionnee is not None:
                colonne = round((piece_selectionnee.rect.x - ORIGINE_X) / TAILLE_CASE)
                ligne = round((piece_selectionnee.rect.y - ORIGINE_Y) / TAILLE_CASE)

                piece_selectionnee.rect.x = ORIGINE_X + (colonne * TAILLE_CASE)
                piece_selectionnee.rect.y = ORIGINE_Y + (ligne * TAILLE_CASE)
                piece_selectionnee = None

    # --- AFFICHAGE ---
    if ecran == "menu":
        fenetre.blit(fond_menu, (0, 0))
        for bouton in boutons_menu:
            bouton.afficher(fenetre)

    elif ecran == "jeu":
        fenetre.blit(fond_jeu, (0, 0))
        for molecule in molecules:
            molecule.afficher(fenetre)
        bouton_retour.afficher(fenetre)

    pygame.display.flip()
    horloge.tick(60)

pygame.quit()
sys.exit()