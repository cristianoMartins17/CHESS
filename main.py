import pygame
from plateau import *
from pieces import *
from jeu import *

pygame.init()

temps = pygame.time.Clock()
pygame.display.set_caption('CHESS') # Titre de la fenêtre
Win = pygame.display.set_mode((largeur, hauteur))


def main():
    
    run = True
    FPS = 60
    while run :
        temps.tick(FPS) # Combien de fois par seconde on raffraichit la fenêtre
        
        pygame.display.update() # Met à jour la fenêtre à chaque itération de la boucle
        
        for event in pygame.event.get() : # Si un event QUIT est détecté, on ferme la fenêtre
            if event.type == pygame.QUIT :
                run = False
                quit()
                
            # Gestion des clics de la souris pour : sélectionner et déplacer les pièces
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                square = mouse_to_square(pos)

                if not selected_square:
                    selected_square = square
                    valid_moves = jeu.get_valid_moves(square)
                else:
                    jeu.play_move(selected_square, square)
                    selected_square = None
                    valid_moves = []
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and game_over:
                        jeu = Etat_jeu()
                        selected_square = None
                        valid_moves = []
                        game_over = False
