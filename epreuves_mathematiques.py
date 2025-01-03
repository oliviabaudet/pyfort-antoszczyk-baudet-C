###factorielle###
import random
from operator import truediv

def factorielle(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res
n = random.randint(1,10)
print(n)
print(factorielle(n))


###equation_linaire###
import random
def lineaire():
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = -b/a
    liste = [a,b,x]
    return liste

def equation():
    liste =  lineaire()
    print("Résoudre l'équation a*x + b = 0.")
    reponse = float(input("Quelle est la valeur de x:"))
    if reponse == x:
        return True
    else:
        return False


###nombres premiers###
import random
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
    print("trouver le nombre le plus proche de", n)
    reponse = int(input("entrer un nombre:"))
    if reponse == solution:
        return True
    else:
        return False

###roulette mathématique###
import random
def epreuve_roulette_mathematique():
    n= [random.randint(1,20) for i in range(5)]
    operation = random.choice(['+','-','*'])
    if operation == '+':
        solution = sum(n)
    elif operation == '-':
        solution = n[0]
        for i in n[1:]:
            solution -= n
    elif operation == '*':
        solution = 1
        for i in n:
            solution *= n
    print()
    reponse = int(input("entrer un nombre:"))
    if solution == reponse:
        return True
    else:
        return False











