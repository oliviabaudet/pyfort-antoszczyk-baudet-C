from enigme_pere_fouras import *
from epreuve_finale import *
from epreuves_hasard import *
from epreuves_logiques import *
from epreuves_mathematiques import *
from fonctions_utiles import *

def jeu():
    introduction()
    liste_joueurs = composer_equipe()
    cles = 0
    while cles < 3:
        numero = menu_epreuves()
        joueur = choisir_joueur(liste_joueurs)
        if numero == 1:
            victoire = epreuve_math()
        elif numero == 2:
            victoire = epreuve_logique()
        elif numero == 3:
            victoire = epreuve_hasard()
        else:
            victoire = enigme_pere_fouras()
        if victoire:
            cles += 1
            joueur["cles_gagnees"] += 1
        print(f"Vous possédez {cles} clé(s).")
        #historique(victoire, numero, joueur)
    salle_de_tresor()

jeu()

