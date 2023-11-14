import random

class Partie:
    """Classe définissant la partie de démineur

    Attributes
    ----------
    grille : list
        grille de la partie
    difficulte : str
        niveau de difficulté
    nb_mines_restantes : int
        nombre de mines restantes à marquer
    marquees : dict
        cases marquées
    visible : liste
        cases visibles
    """
    def __init__(self):
        """Constructeur de la classe Partie
        """
        self.grille = []
        self.difficulte = None
        self.nb_mines_restantes = 0
        self.marquees = {}
        self.visible = []

    def initialiser_visibilite(self):
        """Cache la grille de départ
        """
        rows, cols = len(self.grille), len(self.grille[0])
        self.visible = [['C' for _ in range(cols)] for _ in range(rows)]

    def obtenir_taille_grille(self, difficulte):
        """Récupère la taille de la grille pour la classe Grille
        """
        if difficulte == "facile":
            return 8, 8
        elif difficulte == "moyen":
            return 10, 10
        elif difficulte == "difficile":
            return 12, 12
        else:
            return None  # Gére le cas d'une difficulté non valide

    def choisir_difficulte(self, difficulte):
        """Définie la difficulté de la partie
        """
        if difficulte == "facile":
            self.difficulte = "facile"
        elif difficulte == "moyen":
            self.difficulte = "moyen"
        elif difficulte == "difficile":
            self.difficulte = "difficile"
        else:
            print("Difficulté non valide. Choisissez entre 'facile', 'moyen' ou 'difficile'.")

            
    def generer_grille(self):
        """Retourne la grille de la partie
        """
        if self.difficulte is None:
            print("Veuillez choisir une difficulté avant de générer la grille.")
            return
        if self.difficulte == "facile":
            rows, cols, mines = 8, 8, 10
        elif self.difficulte == "moyen":
            rows, cols, mines = 10, 10, 20
        elif self.difficulte == "difficile":
            rows, cols, mines = 12, 12, 30
        self.nb_mines_restantes = mines
        self.grille = [[0 for _ in range(cols)] for _ in range(rows)]
        # Place les mines aléatoirement sur la grille
        for _ in range(mines):
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
            while self.grille[row][col] == -1:
                row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
            self.grille[row][col] = -1
        # Calcule les nombres autour des mines
        for row in range(rows):
            for col in range(cols):
                if self.grille[row][col] == -1:
                    continue
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= row + dr < rows and 0 <= col + dc < cols and self.grille[row + dr][col + dc] == -1:
                            self.grille[row][col] += 1
        
        # Initialiser la visibilité après la génération de la grille
        self.initialiser_visibilite()




    def afficher_grille(self, afficher_mines=False):
        """Affiche la grille de la partie
        """
        for row_idx, row in enumerate(self.grille):
            visible_row = self.visible[row_idx]
            display_row = []
            for col_idx, cell in enumerate(row):
                if visible_row[col_idx] == 'C':
                    display_row.append('X')  # Afficher 'X' pour les cases masquées
                elif cell == -1 and afficher_mines:
                    display_row.append('B')  # Afficher 'B' pour les mines
                else:
                    display_row.append(str(cell))
            print(' '.join(display_row))
                
    def marquer_case(self, row, col):
        """Permet de marquer ou démarquer une case"""
        if (row, col) in self.marquees:
            # Démarquer la case
            self.grille[row][col] = self.marquees[(row, col)]
            if self.grille[row][col] == -1:
                self.nb_mines_restantes += 1
            del self.marquees[(row, col)]
        else:
            # Marquer la case
            if self.visible[row][col] == 'C':
                self.marquees[(row, col)] = self.grille[row][col]
                self.grille[row][col] = 'M'
                if self.grille[row][col] == -1:
                    self.nb_mines_restantes -= 1
            

    def demarquer_case(self, row, col):
        """Permet de démarquer une case
        """
        if (row, col) in self.marquees:
            self.grille[row][col] = self.marquees[(row, col)]
            if self.grille[row][col] == -1:
                self.nb_mines_restantes += 1
            del self.marquees[(row, col)]
    
    def decouvrir_case(self, row, col):
        """Permet de découvrir une case
        """
        rows, cols = len(self.grille), len(self.grille[0])
        if row < 0 or row >= rows or col < 0 or col >= cols or self.visible[row][col] != 'C':
            return
        if self.grille[row][col] == -1:
            print("BOOM! Vous avez découvert une mine.")
        elif self.grille[row][col] == 'M':
            print("Vous avez marqué cette case.")
        else:
            self.visible[row][col] = self.grille[row][col]
            if self.grille[row][col] == 0:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        new_row, new_col = row + dr, col + dc
                        self.decouvrir_case(new_row, new_col)

    def jouer(self):
        """Permet de jouer au démineur
        """
        self.initialiser_visibilite()
        while True:
            self.afficher_grille()
            action = input("Saisissez votre action (M pour marquer, D pour découvrir, Q pour quitter) : ").upper()
            if action == "Q":
                print("Partie terminée.")
                break
            elif action == "M":
                row = int(input("Saisissez la ligne de la case à marquer : "))
                col = int(input("Saisissez la colonne de la case à marquer : "))
                self.marquer_case(row, col)
            elif action == "D":
                row = int(input("Saisissez la ligne de la case à découvrir : "))
                col = int(input("Saisissez la colonne de la case à découvrir : "))
                self.decouvrir_case(row, col)
                if self.grille[row][col] == -1:
                    self.afficher_grille(afficher_mines=True)
                    print("La partie est terminée.")
                    break
            else:
                print("Action non valide. Veuillez saisir M, D ou Q.")

       
                
                
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
                

class Demineur(QWidget):
    """Classe définissant l'interface de la partie
    """
    def __init__(self):
        super().__init__()

        self.partie = Partie()
        self.partie.choisir_difficulte("facile")
        self.partie.generer_grille()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Démineur')
        self.setGeometry(100, 100, 600, 600)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.boutons = []

        for i in range(len(self.partie.grille)):
            ligne_boutons = []
            for j in range(len(self.partie.grille[i])):
                bouton = QPushButton('')
                bouton.clicked.connect(lambda _, row=i, col=j: self.clic_bouton(row, col))
                ligne_boutons.append(bouton)
                self.layout.addWidget(bouton, i, j)
            self.boutons.append(ligne_boutons)

        self.bouton_recommencer = QPushButton('Recommencer')
        self.bouton_recommencer.clicked.connect(self.recommencer)
        self.layout.addWidget(self.bouton_recommencer, len(self.partie.grille) + 1, 0, 1, len(self.partie.grille[0]))

        self.maj_affichage()

    def clic_bouton(self, row, col):
        self.partie.decouvrir_case(row, col)
        self.maj_affichage()

    def recommencer(self):
        self.partie.generer_grille()
        self.partie.initialiser_visibilite()
        self.maj_affichage()

    def maj_affichage(self):
        for i in range(len(self.partie.grille)):
            for j in range(len(self.partie.grille[i])):
                cell_value = self.partie.visible[i][j]
                if cell_value == 'C':
                    self.boutons[i][j].setText('')
                elif cell_value == 'M':
                    self.boutons[i][j].setText('M')
                else:
                    self.boutons[i][j].setText(str(cell_value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Demineur()
    ex.show()
    sys.exit(app.exec())
    
                
                
                
                
                
                
                
                
                
                
                
                