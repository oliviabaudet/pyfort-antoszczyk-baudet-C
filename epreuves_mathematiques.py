import random

####### factorielle #######

def factorielle(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def epreuve_math_factorielle():
    n = random.randint(1,10)
    fact = factorielle(n)
    print(f"Épreuve de Mathématiques: Calculer la factorielle de {n}.")
    rep = int(input("Votre réponse: "))
    if fact == rep:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect, vous avez perdu.")
        print("La bonne réponse était", fact)
        return False


####### equation linaire #######

def resoudre_equation_lineaire():
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = -b/a
    liste = [a,b,x]
    return liste

def epreuve_math_equation():
    liste =  resoudre_equation_lineaire()
    a,b,x = liste
    print(f"Épreuve de Mathématiques: Résoudre l'équation {a}x + {b} = 0.")
    reponse = float(input("Quelle est la valeur de x:"))
    if reponse == x:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect, vous avez perdu.")
        print("La bonne réponse était", x)
        return False


####### nombres premiers #######

def est_premier(n):
    i = 2
    while i <= n and n%i != 0:
        i += 1
    if i == n:
        return True
    else:
        return False

def premier_plus_proche(n):
    if est_premier(n):
        return n
    return premier_plus_proche(n+1)

def  epreuve_math_premier():
    n = random.randint(10,20)
    solution = premier_plus_proche(n)
    print("Épreuve de Mathématiques: Trouver le nombre premier supérieur ou égal le plus proche de", n)
    reponse = int(input("Votre réponse: "))
    if reponse == solution:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect, vous avez perdu.")
        print("La bonne réponse était", solution)
        return False


####### roulette mathématique #######

import random
def epreuve_roulette_mathematique():
    n= [random.randint(1,20) for i in range(5)]
    print("Nombres sur la roulette :", n)
    operation = random.choice(['+','-','*'])
    if operation == '+':
        print("Calculez le résultat en combinant ces nombres avec une addition")
        solution = 0
        for i in n[1:]:
            solution += i
    elif operation == '-':
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
        solution = n[0]
        for i in n[1:]:
            solution -= i
    elif operation == '*':
        print("Calculez le résultat en combinant ces nombres avec une multiplication")
        solution = 1
        for i in n:
            solution *= i
    reponse = int(input("Votre réponse : "))
    if reponse == solution:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect, vous avez perdu.")
        print("La bonne réponse était", solution)
        return False


####### Epreuve de mathématique #######

def epreuve_math():
    epreuves = [epreuve_math_factorielle, epreuve_math_equation, epreuve_math_premier, epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)
    if epreuve():
        return True
    return False











