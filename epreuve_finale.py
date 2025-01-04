import json
import random

####### Salle de trésor #######

def salle_de_tresor():
    essais = 3
    with open('data/indicesSalle.json', 'r', encoding='utf-8') as f:
        enigmes = json.load(f)
    annee = str(2023 - random.randint(0,8))
    liste = []
    for i in enigmes:
        enigmes = enigmes[i][annee]
    for i in enigmes:
        liste.append(enigmes[i])
    emission = liste[random.randint(0,len(liste)-1)]
    mot = emission["MOT-CODE"]
    indices = emission["Indices"]
    rep = False
    for i in range(3):
        print(indices[i])
    while essais > 0 and not rep:
        reponse = input("Quelle est votre réponse : ")
        if reponse.upper() == mot:
            rep = True
        else:
            if essais != 1:
                print(indices[6-essais])
            essais -=1
    if not rep :
        print("Vous avez perdu. La réponse était", mot)
    else:
        print("Bravo vous avez trouvé le mot clé !")

