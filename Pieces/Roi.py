from Pieces import Piece

class Roi(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

    def est_en_echec(self, position, couleur_roi):
        for ligne in self.grille:
            for piece in ligne:
                if piece is not None and piece.couleur != couleur_roi:
                    mouvements = piece.mouvements_valides_sans_verif(self)
                    if position in mouvements:
                        return True
        return False
        
    def mouvements_valides(self, position, plateau):
        mouvements = []
        # Les mouvements possibles pour un roi (une case dans n'importe quelle direction)
        possible_moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Horizontal et vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonales
        ]
        
        for move in possible_moves:
            new_x = position[0] + move[0]
            new_y = position[1] + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:  # Vérifie que la nouvelle position est sur le plateau
                if self.est_en_echec((new_x, new_y), self.couleur) == False :
                    if plateau[new_x][new_y] is None:  # La case est vide
                        mouvements.append((new_x, new_y))
                    elif plateau[new_x][new_y].couleur != self.couleur:  # La case est occupée par une pièce adverse
                        mouvements.append((new_x, new_y))
        return mouvements
    
    