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

jeu_nim()


