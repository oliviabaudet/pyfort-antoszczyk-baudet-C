import random

####### Bonneteau #######

def bonneteau():
    bonneteaux = ['A','B', 'C']
    print(" ")
    print("Bonjour, bienvenue dans le jeu des bonneteaux.\n")
    print("Vous devez deviner sous quel bonneteau (A, B ou C) se cache la clé ")
    print("Vous avez deux essais.")
    print("Après chaques essais, la clé sera remélangée aléatoirement sous un des bonneteaux")
    print("Bon courage !")
    print("Bonneteaux disponibles : {}".format(','.join(bonneteaux)))

    essais = 2
    while essais > 0:
        solution = random.choice(bonneteaux)
        print("Tentative {}/2 :".format(2 - essais + 1))
        choix = 'D'
        while choix not in bonneteaux:
            choix = input("Choisissez un bonneteau({}): ".format(','.join(bonneteaux))).upper()
            if choix not in bonneteaux:
                print("Votre choix n'est pas valide, Veuillez réessayer.")
        if choix == solution:
            print("Bravo! vous avez touvé la clé sous le bonneteau {}." .format(solution))
            return True
        else:
            print("Vous n'avez pas trouvé le bon bonneteau.")
        essais -= 1
    print("Vous avez perdu, la clé se trouvait sous le bonneteau {}.".format(solution))
    return False


####### Lancé de dé #######

def jeu_lance_des():
    print(" ")
    print("Bonjour, bienvenue dans le jeu des dés.\n")
    print("Le premier joueur a obtenir un 6 gagne la partie.")
    essais = 3
    while essais != 0:
        print(f"Il vous reste {essais} essais.")
        input("Appuyez sur la touche 'Entrée' pour lancer vos dés.")
        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print("Voici les valeurs que vous avez obtenues:", des_joueur[0], "et" ,des_joueur[1])
        if des_joueur[0] == 6 or des_joueur[1] == 6:
            print("Vous avez remporté la partie et la clé.")
            return True
        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print("Voici les valeurs obtenues par le maître du jeu:", des_maitre[0], "et", des_maitre[1])
        if des_maitre[0] == 6 or des_maitre[1] == 6:
            print("Le maître du jeu a gagné")
            return False
        essais -= 1
        if essais != 0:
            print("Passons au prochain essai.")
    print("Aucun joueur n'a obtenu un 6 après trois essais, c'est un match nul.")
    return False


####### Epreuve de hasard #######

def epreuve_hasard():
    epreuves = [jeu_lance_des, bonneteau]
    epreuve = random.choice(epreuves)
    return epreuve()
