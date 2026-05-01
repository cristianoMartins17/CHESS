from Pieces.Piece import Piece

class Cavalier(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = 'C' if couleur == 'blanc' else 'c'
    
    def mouvements_valides(self, position, plateau):
        mouvements = []
        # Les mouvements possibles pour un cavalier (en forme de "L")
        possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for move in possible_moves:
            new_x = position[0] + move[0]
            new_y = position[1] + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:  # Vérifie que la nouvelle position est sur le plateau
                if plateau[new_x][new_y] is None:  # La case est vide
                    mouvements.append((new_x, new_y))
                elif plateau[new_x][new_y].couleur != self.couleur:  # La case est occupée par une pièce adverse
                    mouvements.append((new_x, new_y))
            # Le cavalier peut sauter par-dessus les pièces, donc pas besoin de vérifier les cases intermédiaires
        return mouvements