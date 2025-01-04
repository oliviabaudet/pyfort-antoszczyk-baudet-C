import random

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

def jeu_lance_des():


