
class Piece:
    def __init__(self, couleur):
        self.couleur = couleur
        self.position = None
        self.vivante = True

    def mouvements_valides(self, position, plateau):
        return []  # Cette méthode est implémentée dans les classes hérité pour chaque type de pièce