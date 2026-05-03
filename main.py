import pygame
from plateau import *
from Pieces import *
from jeu import *
from affichage.interface import *
from affichage.console import *

pygame.init()

temps = pygame.time.Clock()
pygame.display.set_caption('CHESS') # Titre de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))


def main():
    plateau = Plateau()

    print("\nPlateau avant déplacement :")
    afficher_plateau_console(plateau)

    # Déplacement du pion blanc
    plateau.deplacer_piece((6, 0), (5, 0))

    print("\nPlateau après déplacement :")
    afficher_plateau_console(plateau)

    # Vérifications
    depart = plateau.get_piece((6, 0))
    arrivee = plateau.get_piece((5, 0))

    if depart is None and arrivee is not None:
        print("✅ Déplacement fonctionnel")
    else:
        print("❌ Erreur déplacement")

    

    # run = True
    # FPS = 60
    # while run :
    #     temps.tick(FPS) # Combien de fois par seconde on raffraichit la fenêtre
        
    #     pygame.display.update() # Met à jour la fenêtre à chaque itération de la boucle
        
    #     for event in pygame.event.get() : # Si un event QUIT est détecté, on ferme la fenêtre
    #         if event.type == pygame.QUIT :
    #             run = False
    #             quit()
                
    #         # Gestion des clics de la souris pour : sélectionner et déplacer les pièces
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             pos = pygame.mouse.get_pos()
    #             square = mouse_to_square(pos)

    #             if not selected_square:
    #                 selected_square = square
    #                 valid_moves = jeu.get_valid_moves(square)
    #             else:
    #                 jeu.play_move(selected_square, square)
    #                 selected_square = None
    #                 valid_moves = []
                    
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_RETURN and game_over:
    #                     jeu = Etat_jeu()
    #                     selected_square = None
    #                     valid_moves = []
    #                     game_over = False
        
    #         dessiner_plateau(ecran, image_plateau)
    #         dessiner_pieces(ecran, jeu.plateau, images_pieces)

    #         pygame.display.flip()

if __name__ == "__main__":
    main()