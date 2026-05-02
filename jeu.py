from plateau import Plateau

class jeu:
	def __init__(self):
		self.plateau = Plateau()
		self.tour = "blanc" # blanc ou noir
		self.selection = None # Carré sélectionné (ligne, colonne)
		self.coups_valides = [] # Liste des coups valides pour la pièce sélectionnée
		self.partie_terminee = False
		self.gagnant = None # "blanc", "noir" ou None
  
	def reinitialiser(self):
		self.plateau = Plateau()
		self.tour = "blanc" # blanc ou noir
		self.selection = None # Carré sélectionné (ligne, colonne)
		self.coups_valides = [] # Liste des coups valides pour la pièce sélectionnée
		self.partie_terminee = False
		self.gagnant = None # "blanc", "noir" ou None

	def selectionner_case(self, case):
		piece = self.plateau.get_piece(case)

		if piece is None:
			return False

		if piece.couleur != self.tour:
			return False

		self.selection = case
		self.coups_valides = piece.coups_possibles(case, self.plateau)
		return True

	def jouer_coup(self, depart, arrivee):
		if arrivee not in self.coups_valides:
			return False

		self.plateau.deplacer_piece(depart, arrivee)
		self.selection = None
		self.coups_valides = []

		self.changer_tour()
		self.verifier_fin_partie()
		return True

	def changer_tour(self):
		if self.tour == "blanc":
			self.tour = "noir"
		else:
			self.tour = "blanc"
   
	

