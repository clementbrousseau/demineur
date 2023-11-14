from partie2 import Partie

if __name__ == "__main__":
    partie = Partie()
    partie.choisir_difficulte("facile")
    partie.generer_grille()
    partie.jouer()
