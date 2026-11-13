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
virus = Molecule("virus", "assets/Virus.png", 0, 0)
piece_verte = Molecule("verte", "assets/Green_2.png", 200, 150)
fond_menu = pygame.image.load("assets/bgLevelSelect.jpg").convert()
fond_jeu = pygame.image.load("assets/backgroundPlayBoard.png").convert()
ecran = "menu"  # Peut valoir "menu" ou "jeu"
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




        






    virus.afficher(fenetre)
    piece_verte.afficher(fenetre)
    pygame.display.flip()

pygame.quit()
sys.exit()
