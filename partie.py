import random

class Partie:
    def __init__(self):
        self.grille = []
        self.difficulte = None
        self.nb_mines_restantes = 0
        self.marquees = {}  # Cases marquées

    def choisir_difficulte(self, difficulte):
        if difficulte == "facile":
            self.difficulte = "facile"
        elif difficulte == "moyen":
            self.difficulte = "moyen"
        elif difficulte == "difficile":
            self.difficulte = "difficile"
        else:
            print("Difficulté non valide. Choisissez entre 'facile', 'moyen' ou 'difficile'.")

    def obtenir_taille_grille(self, difficulte):
        if difficulte == "facile":
            return 8, 8
        elif difficulte == "moyen":
            return 10, 10
        elif difficulte == "difficile":
            return 12, 12
        else:
            return None  # Gérer le cas d'une difficulté non valide

    def generer_grille(self):
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

        # Placez les mines aléatoirement sur la grille
        for _ in range(mines):
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
            while self.grille[row][col] == -1:
                row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
            self.grille[row][col] = -1

        # Calculez les nombres autour des mines
        for row in range(rows):
            for col in range(cols):
                if self.grille[row][col] == -1:
                    continue
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= row + dr < rows and 0 <= col + dc < cols and self.grille[row + dr][col + dc] == -1:
                            self.grille[row][col] += 1

    def afficher_grille(self):
        for row in self.grille:
            #print(' '.join(map(lambda x: str(x) if x >= 0 else 'X', row)))
            print(' '.join(map(lambda x: str(x) if (isinstance(x, int) and x >= 0) else 'X', row)))


    def marquer_case(self, row, col):
        if self.grille[row][col] != 'M':
            self.marquees[(row, col)] = self.grille[row][col]
            self.grille[row][col] = 'M'
            if self.grille[row][col] == -1:
                self.nb_mines_restantes -= 1
    
    def demarquer_case(self, row, col):
        if (row, col) in self.marquees:
            self.grille[row][col] = self.marquees[(row, col)]
            if self.grille[row][col] == -1:
                self.nb_mines_restantes += 1
            del self.marquees[(row, col)]
    
    def decouvrir_case(self, row, col):
        rows = len(self.grille)
        cols = len(self.grille[0])
    
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
    
        if self.grille[row][col] == -1:
            print("BOOM! Vous avez découvert une mine.")
        elif self.grille[row][col] == 'M':
            print("Vous avez marqué cette case.")
        elif self.grille[row][col] == 0:
            self.grille[row][col] = 'D'  # 'D' pour découvert
    
            # Explorer les cases adjacentes récursivement
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    new_row, new_col = row + dr, col + dc
                    self.decouvrir_case(new_row, new_col)
        else:
            self.grille[row][col] = 'D'  # 'D' pour découvert


    def jouer(self):
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
                    self.afficher_grille()
                    print("BOOM! Vous avez découvert une mine. La partie est terminée.")
                    break
            else:
                print("Action non valide. Veuillez saisir M, D ou Q.")
                

    

            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

