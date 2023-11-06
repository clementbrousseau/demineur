from partie import Partie
from grille import Grille
from case import Case
from etat_case import EtatCase
 
if __name__ == "__main__":
    partie = Partie()
    partie.choisir_difficulte("facile")
    partie.generer_grille()
    partie.jouer()
    