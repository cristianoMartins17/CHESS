from Pieces.Piece import Piece

class Pion(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = 'P' if couleur == 'blanc' else 'p'
    
    def mouvements_valides(self, position, plateau):
        mouvements = []
        direction = -1 if self.couleur == 'blanc' else 1  # Les pions blancs sont en haut (direction -1) et les pions noirs sont en bas (direction +1)
        new_x = position[0] + direction
        new_y = position[1]
        
        # Mouvement de base : avancer d'une case
        if 0 <= new_x < 8 and 0 <= new_y < 8 and plateau[new_x][new_y] is None:
            mouvements.append((new_x, new_y))
        
        # Mouvement initial : avancer de deux cases
        if (self.couleur == 'blanc' and position[0] == 6) or (self.couleur == 'noir' and position[0] == 1):
            new_x2 = position[0] + 2 * direction
            if 0 <= new_x2 < 8 and plateau[new_x][new_y] is None and plateau[new_x2][new_y] is None:
                mouvements.append((new_x2, new_y))
        
        # Prise en diagonale
        for dy in [-1, 1]:  # Diagonale gauche et droite
            diag_x = position[0] + direction
            diag_y = position[1] + dy
            if 0 <= diag_x < 8 and 0 <= diag_y < 8:
                if plateau[diag_x][diag_y] is not None and plateau[diag_x][diag_y].couleur != self.couleur:
                    mouvements.append((diag_x, diag_y))
        
        return mouvements