import pygame

class Etat_jeu:
	def __init__(self):
		self.echequier = [
			["Tn", "Cn", "Fn", "Dn", "", "Fn", "Cn", "Tn"],
			["Pn", "Pn", "Pn", "Pn", "Pn", "Pn", "Pn", "Pn"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["Pb", "Pb", "Pb", "Pb", "Pb", "Pb", "Pb", "Pb"],
			["Tb", "Cb", "Fn", "Db", "Rb", "Fn", "Cb", "Tb"]
		]

		self.tourAuBlanc = True
		self.moveLog = []