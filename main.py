import pygame
import sys


pygame.init()


largeur, hauteur = 960, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Anti-Virus")

fond = pygame.image.load("assets/bgLevelSelect.jpg").convert()

class Molecule:
    
    def __init__(self, nom, image_path, x, y):
        self.nom = nom                 
        self.image = pygame.image.load(image_path).convert_alpha()  
        self.rect = self.image.get_rect(topleft=(x, y))             

    
    def afficher(self, fenetre):
        fenetre.blit(self.image, self.rect)    
fond_menu = pygame.image.load("assets/bgLevelSelect.jpg").convert()
fond_jeu = pygame.image.load("assets/backgroundPlayBoard.png").convert()
ecran = "menu"  # Peut valoir "menu" ou "jeu"

class UI : 
     def __init__(self, nom, image_path, x, y):
            self.nom = nom                 
            self.image = pygame.image.load(image_path).convert_alpha()  
            self.rect = self.image.get_rect(topleft=(x, y))             
     def afficher(self, fenetre):
        fenetre.blit(self.image, self.rect)    

# liste des molécules, position diff pour eviter superposition 
molecules = [
    Molecule("virus", "assets/Virus.png", 40, 40),
    Molecule("bleue 2", "assets/Blue_2.png", 220, 80),
    Molecule("bleue 3", "assets/Blue_3.png", 470, 70),
    Molecule("verte 2", "assets/Green_2.png", 220, 270),
    Molecule("verte 3", "assets/Green_3.png", 40, 220),
    Molecule("orange 3", "assets/Orange_3.png", 700, 60),
    Molecule("rose 2", "assets/Pink_2.png", 470, 250),
    Molecule("violette 3", "assets/Purple_3.png", 700, 300),
    Molecule("jaune 3", "assets/Yellow_3.png", 40, 400),
]

UI = [ 
     UI("start_button", "assets/StartButton.png", 400, 300),]

en_cours = True
while en_cours:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ecran == "menu":
                ecran = "jeu"  # On bascule vers le plateau de jeu

    fenetre.blit(fond, (0, 0))
    if ecran == "menu":
        fenetre.blit(fond_menu, (0, 0))
    # Ici tu afficheras les boutons de sélection de niveau
    elif ecran == "jeu":
        fenetre.blit(fond_jeu, (0, 0))
    # Ici tu affiches les pièces du niveau (virus, molécules...)




        


if ecran == 'menu' : 
    for UI in UI:
        UI.afficher(fenetre)



    if ecran == "jeu":
        for molecule in molecules:
            molecule.afficher(fenetre)

    pygame.display.flip()

pygame.quit()
sys.exit()
