# Initialise le plateau de jeu (grille + pièces)

import pygame
import os

largeur, hauteur = 760, 760
lignes, colonnes = 8,8
carre = largeur // lignes

Brun = (87, 16, 16)
Blanc = (245, 245, 220)

# Chargement des images des pièces pour qu'elles conviennent à la taille des cases
Pion_Blanc = pygame.transform.scale(pygame.image.load(os.path.join("images", "Pion_Blanc.png")), (carre, carre)) 
Fou_Blanc = pygame.transform.scale(pygame.image.load(os.path.join("images", "Fou_Blanc.png")), (carre, carre)) 
Cavalier_Blanc = pygame.transform.scale(pygame.image.load(os.path.join("images", "Cavalier_Blanc.png")), (carre, carre)) 
Tour_Blanc = pygame.transform.scale(pygame.image.load(os.path.join("images", "Tour_Blanc.png")), (carre, carre)) 
Dame_Blanc = pygame.transform.scale(pygame.image.load(os.path.join("images", "Dame_Blanc.png")), (carre, carre)) 
Roi_Blanc = pygame.transform.scale(pygame.image.load(os.path.join("images", "Roi_Blanc.png")), (carre, carre)) 

Pion_noir = pygame.transform.scale(pygame.image.load(os.path.join("images", "Pion_noir.png")), (carre, carre)) 
Fou_noir = pygame.transform.scale(pygame.image.load(os.path.join("images", "Fou_noir.png")), (carre, carre)) 
Cavalier_noir = pygame.transform.scale(pygame.image.load(os.path.join("images", "Cavalier_noir.png")), (carre, carre)) 
Tour_noir = pygame.transform.scale(pygame.image.load(os.path.join("images", "Tour_noir.png")), (carre, carre)) 
Dame_noir = pygame.transform.scale(pygame.image.load(os.path.join("images", "Dame_noir.png")), (carre, carre)) 
Roi_noir = pygame.transform.scale(pygame.image.load(os.path.join("images", "Roi_noir.png")), (carre, carre)) 

class plateau :
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

        