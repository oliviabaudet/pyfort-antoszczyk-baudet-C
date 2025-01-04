import json
import random

####### Père Fouras #######

def charger_enigmes(fichier):
    with open("data/"+fichier, 'r', encoding='utf-8') as f:
        enigmes = json.load(f)
    liste_enigmes = []
    for elt in enigmes:
        liste_enigmes.append([elt["question"],elt["reponse"]])
    return liste_enigmes


def enigme_pere_fouras():
    print(" ")
    print("Répondez correctement à l'énigme suivante pour gagner une clé.\n")
    enigmes = charger_enigmes("enigmesPF.json")
    enigme = enigmes[random.randint(0, len(enigmes))]
    essais = 3
    print(enigme[0])
    while essais > 0:
        reponse = input("Quel est votre réponse : ")
        if reponse.lower() == enigme[1].lower():
            print("Bravo, vous avez trouvé le bon mot. Vous remportez une clé")
            return True
        essais -= 1
        print(f"Mauvaise réponse. Il vous reste {essais} essais")
    print("Vous avez échoué. La réponse correcte était", enigme[1])
    return False
