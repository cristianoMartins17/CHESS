from plateau import *

def afficher_plateau_console(plateau):
    y = 8  # Numéro de ligne initial (commence à 8 pour correspondre à l'affichage traditionnel du plateau d'échecs)
    for ligne in plateau.echequier:
        print(y, end=" ") 
        for piece in ligne: # numéros de lignes
            if piece is None:
                print(".", end=" ")  # Affiche un point pour les cases vides
            else:
                print(piece.symbole, end=" ")  # Affiche le symbole de la pièce
        y -= 1  # Décrémente le numéro de ligne pour la prochaine itération
        print()  # Nouvelle ligne après chaque rangée du plateau
