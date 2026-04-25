from Pieces import Piece

class Dame(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
    
    def mouvements_valides(self, position, plateau):
        mouvements = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Horizontal et vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonales
        ]
        for direction in directions:
            for i in range(1, 8):  # La dame peut se déplacer jusqu'à 7 cases
                new_x = position[0] + direction[0] * i
                new_y = position[1] + direction[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:  # Vérifie que la nouvelle position est sur le plateau
                    if plateau[new_x][new_y] is None:  # La case est vide
                        mouvements.append((new_x, new_y))
                    elif plateau[new_x][new_y].couleur != self.couleur:  # La case est occupée par une pièce adverse
                        mouvements.append((new_x, new_y))
                        break  # La dame ne peut pas sauter par-dessus les pièces
                    else:  # La case est occupée par une pièce alliée
                        break
                else:
                    break  # Sort du plateau
        return mouvements