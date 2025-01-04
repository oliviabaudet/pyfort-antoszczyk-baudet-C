import random

####### Jeu des bâtonnets #######

def affiche_batonnets(n):
    print("Bâtonnets restants:", "|"*n, f" ({n})")

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
    print(" ")
    print("Jeu des batônnets\n")
    print("Vous ne devez pas récupérer le dernier batônnet pour gagner")
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
        print("Le maître du jeu a retiré le dernier bâtonnet. Vous remportez une clé !")
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
    print(" ")
    print("Jeu de tictactoe\n")
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
        print("Vous avez gagné, vous remportez une clé !")
        return True
    if verifier_victoire(grille, "O"):
        print("Le maître a gagné !")
        return False
    if grille_complete(grille):
        print("Match nul, égalité !")
        return False

####### Bataille navale #######

def suiv(joueur):
    return 1 - joueur


def grille_vide():
    grille = []
    for i in range(3):
        ligne = []
        for j in range(3):
            ligne.append(" ")
        grille.append(ligne)
    return grille

def affiche_grille_bateau(grille, message):
    print(message)
    print(f"| {grille[0][0]} | {grille[0][1]} | {grille[0][2]} |")
    print(f"| {grille[1][0]} | {grille[1][1]} | {grille[1][2]} |")
    print(f"| {grille[2][0]} | {grille[2][1]} | {grille[2][2]} |")
    print("-------------")

def demande_position():
    ligne = -1
    while ligne < 0 or ligne > 2:
        ligne = int(input("Saisir la ligne sur laquelle vous voulez jouer (0, 1 ou 2) : "))
        if ligne < 0 or ligne > 2:
            print("Votre saisie est incorrecte, veuillez saisir un nombre entre 0 et 2")
    colonne = -1
    while colonne < 0 or colonne > 2:
        colonne = int(input("Saisir la colonne sur laquelle vous voulez jouer (0, 1 ou 2) : "))
        if colonne < 0 or colonne > 2:
            print("Votre saisie est incorrecte, veuillez saisir un nombre entre 0 et 2")
    tuple = (ligne, colonne)
    return tuple

def init():
    grille = grille_vide()
    message = "Voici la grille où vous devez placer vos bateaux"
    affiche_grille_bateau(grille, message)
    libre = []
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == " ":
                libre.append((i, j))

    print("Choisissez la poisition de votre premier bateau")
    position = (-1, -1)
    while position not in libre:
        position = demande_position()
        if position not in libre:
            print("La position est déjà occupée")
    grille[position[0]][position[1]] = "B"

    libre = []
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == " ":
                libre.append((i, j))

    print("Choisissez la poisition de votre second bateau")
    while position not in libre:
        position = demande_position()
        if position not in libre:
            print("La position est déjà occupée")
    grille[position[0]][position[1]] = "B"

    return grille

def tour(joueur,grille_tirs_joueur,grille_adversaire):
    if joueur == 0:
        coordonnees = demande_position()
        libre = []
        for i in range(3):
            for j in range(3):
                if grille_tirs_joueur[i][j] == " ":
                    libre.append((i, j))
        while coordonnees not in libre:
            print("Vous avez déjà tiré à cet endroit, choisissez une autre position.")
            coordonnees = demande_position()

    else :
        libre = []
        for i in range(3):
            for j in range(3):
                if grille_tirs_joueur[i][j] == " ":
                    libre.append((i,j))
        coordonnees = libre[random.randint(0,len(libre)-1)]
        print("Le maître du jeu tire en position ", coordonnees)
    if grille_adversaire[coordonnees[0]][coordonnees[1]] == "B":
        print("Touché coulé !")
        grille_tirs_joueur[coordonnees[0]][coordonnees[1]] = "x"
    else:
        print("Dans l'eau...")
        grille_tirs_joueur[coordonnees[0]][coordonnees[1]] = "."

def gagne(grille_tirs_joueur):
    compteur = 0
    for i in range(3):
        for j in range(3):
            if grille_tirs_joueur[i][j] == "x":
                compteur += 1
    return compteur == 2

def jeu_bataille_navale():
    print(" ")
    print("Jeu de la bataille navale.\n")
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. ")
    print("Les bateaux coulés sont marqués par 'x'.")
    grille_bateau_joueur = init()
    grille_bateau_maitre = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    grille_bateau_maitre[random.randint(0, 2)][random.randint(0, 2)] = "B"
    x, y = random.randint(0, 2), random.randint(0, 2)
    while grille_bateau_maitre[x][y] == "B":
        x, y = random.randint(0, 2), random.randint(0, 2)
    grille_bateau_maitre[x][y] = "B"
    affiche_grille_bateau(grille_bateau_joueur, "Découvrez votre grille de jeu avec vos bateaux :")
    grille_tirs_joueur = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    grille_tirs_maitre = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    joueur = 1
    fin = False
    while not fin:
        joueur = suiv(joueur)
        if joueur == 0:
            print("C'est à votre tour de faire feu !: ")
            affiche_grille_bateau(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")
            tour(joueur, grille_tirs_joueur, grille_bateau_maitre)
            fin = gagne(grille_tirs_joueur)
        else:
            print("C'est le tour du maître du jeu : ")
            affiche_grille_bateau(grille_tirs_maitre, "Rappel de l'historique des tirs du maître :")
            tour(joueur, grille_tirs_maitre, grille_bateau_joueur)
            fin = gagne(grille_tirs_maitre)

    if gagne(grille_tirs_joueur):
        print("Vous avez gagné, vous remportez une clé !")
        return True
    else:
        print("Le maître a gagné !")
        return False

####### Epreuve de logique #######

def epreuve_logique():
    epreuves = [jeu_nim, jeu_tictactoe, jeu_bataille_navale]
    epreuve = random.choice(epreuves)
    return epreuve()
