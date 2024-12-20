import random

####### Jeu des bâtonnets #######

def affiche_batonnets(n):
    print("Bâtonnets restants:", "|"*n)

def joueur_retrait(n):
    joueur = 0
    while (joueur != 1 and joueur != 2 and joueur != 3) or joueur > n:
        joueur = int(input("Combien de bâtonnets voulez-vous retirer (1, 2 ou 3) ?  "))
    return joueur

def maitre_retrait(n):
    if n%4 == 0:
        maitre = 3
    elif n%4 == 3:
        maitre = 2
    else:
        maitre = 1
    print("Le maître du jeu retire", maitre,"bâtonnets.")
    return maitre

def jeu_nim():
    n = 20
    tour_joueur = True
    i = 0
    while n != 0:
        affiche_batonnets(n)
        if i%2 == 0:
            tour_joueur = True
        else:
            tour_joueur = False
        if tour_joueur:
            print("Tour du joueur.")
            n -= joueur_retrait(n)
        else:
            n -= maitre_retrait(n)
        i += 1
    if tour_joueur:
        print("Le joueur a retiré le dernier bâtonnet. Le maitre gagne !")
        return False
    else:
        print("Le maître du jeu a retiré le dernier bâtonnet. Le joueur gagne !")
        return True



####### Morpion #######

def affiche_grille(grille):
    print(f" {grille[0][0]} | {grille[0][1]} | {grille[0][2]} ")
    print("___|___|___")
    print(f" {grille[1][0]} | {grille[1][1]} | {grille[1][2]} ")
    print("___|___|___")
    print(f" {grille[2][0]} | {grille[2][1]} | {grille[2][2]} ")
    print("   |   |   ")

def verifier_victoire(grille, symbole):
    victoire = False
    for i in range(len(grille)):
        if grille[i][0] == symbole and grille[i][1] == symbole and grille[i][2] == symbole:
            victoire = True
    for i in range(len(grille)):
        if grille[0][i] == symbole and grille[1][i] == symbole and grille[2][i] == symbole:
            victoire = True
    if grille[0][0] == symbole and grille[1][1] == symbole and grille[2][2] == symbole:
        victoire = True
    if grille[0][2] == symbole and grille[1][1] == symbole and grille[2][0] == symbole:
        victoire = True
    return victoire

def coup_maitre(grille, symbole):
    libre = []
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == " ":
                libre.append((i, j))

    for position in libre:
        test = []
        for ligne in grille:
            test.append(ligne[:])
        a,b = position
        test[a][b] = symbole
        if verifier_victoire(test, symbole):
            return position

    for position in libre:
        test = []
        for ligne in grille:
            test.append(ligne[:])
        a,b = position
        test[a][b] = "X"
        if verifier_victoire(test, "X"):
            return position

    a = random.choice(libre)
    return a

def tour_joueur(grille):
    libre = []
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == " ":
                libre.append((i, j))

    valable = [0, 1, 2]
    position = None
    while position not in libre:
        x = None
        while x not in valable:
            x = int(input("Saisir la ligne où vous voulez jouer (0, 1 ou 2) : "))
        y = None
        while y not in valable:
            y = int(input("Saisir la colonne où vous voulez jouer (0, 1 ou 2) : "))
        position = (x,y)
        if position not in libre:
            print("Position déjà occupée. Choisissez une autre case.")
    a, b = position
    grille[a][b] = 'X'
    return None

def tour_maitre(grille):
    position = coup_maitre(grille, "O")
    a, b = position
    grille[a][b] = 'O'
    return None

def grille_complete(grille):
    libre = []
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == " ":
                libre.append((i, j))
    if libre == []:
        return True
    else:
        return False

def verifier_resultat(grille):
    if verifier_victoire(grille, "O"):
        return True
    if verifier_victoire(grille, "X"):
        return True
    if grille_complete(grille):
        return True
    return False

def jeu_tictactoe():
    grille = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    affiche_grille(grille)
    i = 0
    while not verifier_resultat(grille):
        if i%2 == 0:
            tour_joueur(grille)
            affiche_grille(grille)
        else:
            print("Tour de du maître du jeu (O)...")
            tour_maitre(grille)
            affiche_grille(grille)
        i += 1
    if verifier_victoire(grille, "X"):
        print("Le joueur a gagné !")
        return True
    if verifier_victoire(grille, "O"):
        print("Le maître a gagné !")
        return False
    if grille_complete(grille):
        print("Match nul, égalité !")
        return False

jeu_nim()
jeu_tictactoe()
