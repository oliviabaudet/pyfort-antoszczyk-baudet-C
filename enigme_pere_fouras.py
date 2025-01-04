import json

####### Père Fouras #######

def charger_enigmes(fichier):
    with open("data/"+fichier, 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)
    enigmes = []
    for elt in jeu_tv:
        enigmes.append([elt["question"],elt["reponse"]])
    return enigmes
