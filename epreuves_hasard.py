import random

####### Bonneteau #######
"""
def bonneteau():
    bonneteaux = ['A','B', 'C']

    print("Bonjour, bienvenue dans le jeu des bonneteaux.")
    print("Vous devez deviner sous quel bonneteau (A, B ou C) se cache la clé ")
    print("Vous avez deux essais. Bon courage !")
    print("Bonneteaux disponibles : {}".format(', '.join(bonneteaux)))

    max = 2
    tentative = 1
    while tentative <= max:
        lettre = random.choice(bonneteaux)
        print("Tentative {}/{} :".format(tentative, max))
        choix = input("Choisissez un bonneteau({}): ".format(','.join(bonneteaux))).strip().lower()
            if choix in lettre:
                if choix == lettre:
                    print("Bravo! vous avez touvé la clé sous le bonneteau {}." .format(choix))
                    return True
                else:
                print("Vous n'avez pas trouvé le bon bonneteau.")
            else:
                print("Votre choix n'est pas valide.")
            tentative += 1
    print("Vous avez perdu, la clé se trouvait sous le bonneteau {}.".format(lettre))
    return False
"""


####### Lancé de dé #######

def jeu_lance_des():
    essais = 3
    while essais != 0:
        print(f"Il vous reste {essais} essais.")
        input("Appuyez sur la touche 'Entrée'.")
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
        print("Passons au prochain essai.")
        essais -= 1
    print("Aucun joueur n'a obtenu un 6 après trois essais, c'est un match nul.")
    return False



####### Lancé de dé #######
"""
def epreuve_hasard():
    epreuves = [jeu_lance_des, bonneteau]
    epreuve = random.choice(epreuves)
    return epreuve()
"""
