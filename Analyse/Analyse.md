**Démineur en orienté objet**

**ANALYSE**

- **Diagramme de cas d’utilisations**

![](Aspose.Words.89bbe37c-06f8-4bf6-9fe0-0977dcb7251e.004.png)

Ce diagramme représente les usages exigés par l’utilisateur à propos du démineur. On y retrouve également des fonctionnalités secondaire qui ne sont pas directement relier à l’utilisateur mais qui étende un cas d’utilisation. Par exemple, la fonctionnalité de marquer les cases n’est pas indispensable pour jouer au démineur mais elle enrichi ce cas d’utilisation.


- **Diagramme de classes**

![](Aspose.Words.89bbe37c-06f8-4bf6-9fe0-0977dcb7251e.003.png)

Ce diagramme représente les classes qui vont être créées pour coder le démineur. La classe « Case » hérite de trois classes qui représentent les trois possibilité de remplissage d’une case : minée, numérotée ou vide. Ensuite, cette classe agrège la classe « Grille » qui agrège elle-même la classe « Partie ». Concernant les fonctions, la fonction *generer\_grille()* permet de créer la grille de démineur en fonction du niveau de difficulté choisi car le niveau de difficulté influe sur la taille de la grille ainsi que le nombre de mine. La difficulté est elle-même définie par la fonction *choisir\_difficulte().* La fonction *test\_fin()* permet de vérifier à chaque fois qu’une case est découverte si la partie est terminée ou non (c’est-à-dire, si une mine est découverte ou si toute les cases vides et numérotées sont découvertes. Enfin, les fonctions *marquer()* et *decouvrir()* de la classe « Case » permettent respectivement de poser une drapeau sur une case on l’on pense qu’il y a une mine et découvrir ce qu’il y a sous une case.


- **Diagramme d’activités**

![](Aspose.Words.89bbe37c-06f8-4bf6-9fe0-0977dcb7251e.002.png)

Ce diagramme représente le fonctionnement du jeu à partir du lancement d’une partie et jusqu’à la fin de cette dernière (victoire ou défaite).


- **Diagramme d’états de transition**

![](Aspose.Words.89bbe37c-06f8-4bf6-9fe0-0977dcb7251e.001.png)

Ce diagramme représente les différents états que peuvent prendre les cases ainsi que les opérations pour y parvenir.
