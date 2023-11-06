from partie import Partie

class Grille:
    def __init__(self, partie):
        self.taille = partie.obtenir_taille_grille(partie.difficulte)

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

