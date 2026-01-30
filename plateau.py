# Initialise le plateau de jeu (grille + pièces)
from pieces import Pion, Tour, Cavalier, Fou, Dame, Roi

largeur, hauteur = 760, 760
lignes, colonnes = 8,8
carre = largeur // lignes

Brun = (87, 16, 16)
Blanc = (245, 245, 220)

class plateau :
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.echequier = [
			[Tour("noir"), Cavalier("noir"), Fou("noir"), Dame("noir"), Roi("noir"), Fou("noir"), Cavalier("noir"), Tour("noir")],
			[Pion("noir"), Pion("noir"), Pion("noir"), Pion("noir"), Pion("noir"), Pion("noir"), Pion("noir"), Pion("noir")],
			[None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None],
			[Pion("blanc"), Pion("blanc"), Pion("blanc"), Pion("blanc"), Pion("blanc"), Pion("blanc"), Pion("blanc"), Pion("blanc")],
			[Tour("blanc"), Cavalier("blanc"), Fou("blanc"), Dame("blanc"), Roi("blanc"), Fou("blanc"), Cavalier("blanc"), Tour("blanc")]
		]
        
    def get_piece(self, position):  
        ligne, colonne = position   # On décompose le tuple position en ligne et colonne
        return self.echequier[ligne][colonne] # On retourne None ou l'objet Piece à cette position

    def case_vide(self, position):
        return self.get_piece(position) is None

    def dans_plateau(self, position):   # Vérifie si une position est dans les limites du plateau
        ligne, colonne = position
        return 0 <= ligne < 8 and 0 <= colonne < 8 # On retourne True si la position est valide, sinon False

    def deplacer_piece(self, depart, arrivee):
        piece = self.get_piece(depart)                  # Récupère la pièce à la position de départ
        self.echequier[arrivee[0]][arrivee[1]] = piece  # Place la pièce à la position d'arrivée
        self.echequier[depart[0]][depart[1]] = None     # Vide la position de départ 

    def supprimer_piece(self, position):                # Supprime la pièce à la position donnée (sers pour les captures spéciales)
        self.echequier[position[0]][position[1]] = None
    

        