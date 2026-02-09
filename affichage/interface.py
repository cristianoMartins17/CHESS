import pygame
import os

TAILLE_CASE = 95      # 760 / 8
LARGEUR = HAUTEUR = TAILLE_CASE * 8

def preparation_plateau():
    image = pygame.image.load(os.path.join("images", "plateau.png"))
    return pygame.transform.scale(image, (LARGEUR, HAUTEUR))

def preparation_pieces():
    images = {}     # Dictionnaire pour stocker les images des pièces de la forme {(type, couleur): image}

    pieces = ["Pion", "Tour", "Cavalier", "Fou", "Dame", "Roi"]
    couleurs = ["blanc", "noir"]

    for couleur in couleurs:
        for piece in pieces:
            nom_fichier = f"{piece}_{couleur}.png"      # j'utilise un f-string pour créer synamiquement le nom du fichier
            chemin = os.path.join("images", nom_fichier)    # Crée le chemin complet vers le fichier dans le dossier images

            image = pygame.image.load(chemin)       #charge l'image
            image = pygame.transform.scale(image, (TAILLE_CASE, TAILLE_CASE))   # redimensionne l'image pour qu'elle corresponde à la taille des cases

            images[(piece, couleur)] = image    # Stocke l'image dans le dictionnaire images avec la clé (type, couleur)

    return images

def dessiner_plateau(ecran, image_plateau):
    ecran.blit(image_plateau, (0, 0))

def dessiner_pieces(ecran, plateau, images):
    for ligne in range(8):
        for colonne in range(8):
            piece = plateau.get_pieces((ligne, colonne))  # Récupère la pièce à la position (ligne, colonne)
            if piece is not None:
                image_piece = images[(piece.nom, piece.couleur)]  # Récupère l'image correspondante à la pièce
                ecran.blit(image_piece, (colonne * TAILLE_CASE, ligne * TAILLE_CASE))  # Dessine l'image de la pièce à la position correcte sur le plateau

