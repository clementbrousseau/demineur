from etat_case import EtatCase

class Case:
    def __init__(self):
        self.etat = EtatCase.MASQUEE
        self.ligne = None
        self.colonne = None

    def marquer(self):
        self.etat = EtatCase.MARQUEE

    def decouvrir(self):
        self.etat = EtatCase.DECOUVERTE

    def changer_etat(self, nouvel_etat):
        self.etat = nouvel_etat