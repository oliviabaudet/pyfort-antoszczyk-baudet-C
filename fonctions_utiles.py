####### Introduction #######

def introduction():
    print(" ")
    print("Bonjour et bienvenue sur le jeu Ford Boyard !\n")
    print("Voici les règles du jeu :")
    print("Le joueur doit accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")
    return None


####### Composition de l'équipe #######

def composer_equipe():
    liste_joueurs = []
    nombre_joueur = 4
    while nombre_joueur < 1 or nombre_joueur > 3:
        nombre_joueur = int(input("Choisissez le nombre de joueur : "))
        if nombre_joueur > 3:
            print("L'équipe peut comporter jusqu'à 3 joueurs.")
        if nombre_joueur < 1:
            print("Veuillez choisir un nombre entre 1 et 3.")
    print(" ")
    print("Veuillez entrer les informations suivantes : ")
    l = False
    for i in range(nombre_joueur):
        print(" ")
        dico_joueur = {"nom": "", "profession": "", "leader": False, "cles_gagnees": 0}
        dico_joueur["nom"] = input(f"Saisir le nom du joueur {i+1} : ")
        dico_joueur["profession"] = input(f"Saisir la profession de {dico_joueur["nom"]} : ")
        if not l:
            lead = input(f"{dico_joueur["nom"]} est il/elle le/la leader de ce groupe ? ('oui' ou 'non'): ").lower()
            if lead == 'oui':
                l = True
                dico_joueur["leader"] = True
        liste_joueurs.append(dico_joueur)
    if not l:
        print(f"Vous n'avez pas désigné de leader, {liste_joueurs[0]["nom"]} est désigné(e) automatiquement comme étant votre leader.")
        liste_joueurs[0]["leader"] = True
    return liste_joueurs

####### Menu des épreuves #######

def menu_epreuves():
    print(" ")
    print("Voici les différentes épreuves.\n")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du hasard")
    print("4. Énigme du Père Fouras\n")
    numero = 0
    while numero < 1 or numero > 4:
        numero = int(input("Choisissez le numéro de l'épreuve à laquelle vous voulez participer : "))
        if numero < 1 or numero > 4:
            print("Saisie incorrecte, veuillez réesseiller.")
    if numero == 1:
        print("Vous avez sélectionné l'épreuve de mathématiques.")
    if numero == 2:
        print("Vous avez sélectionné l'épreuve de logique.")
    if numero == 3:
        print("Vous avez sélectionné l'épreuve de hasard.")
    if numero == 4:
        print("Vous avez sélectionné l'énigme du Père Fouras.")
    return numero


####### Choix du joueur #######

def choisir_joueur(equipe):
    print(" ")
    for i in range(len(equipe)):
        leader = 'Membre'
        if equipe[i]["leader"]:
            leader = 'Leader'
        print(f"{i+1}. {equipe[i]["nom"]} ({equipe[i]["profession"]}) - {leader}")
    print(" ")
    joueur = 4
    while joueur < 1 or joueur > len(equipe):
        joueur = int(input("Choisissez un joueur pour participer à l'épreuve (1, 2 ou 3): "))
        if joueur < 1 or joueur > len(equipe):
            print("Saisie incorrecte, veuillez réesseiller.")
    if joueur == 1:
        print("Vous avez choisi", equipe[0]["nom"])
    if joueur == 2:
        print("Vous avez choisi", equipe[1]["nom"])
    if joueur == 3:
        print("Vous avez choisi", equipe[2]["nom"])
    return equipe[joueur - 1]


####### Historique #######

def historique(epreuve,choix,joueur):
    f = open("output/historique.txt","a",encoding="utf-8")
    if epreuve :
        reussite = "réussi"
    else:
        reussite = "raté"
    test = ["de Maths","de Logique","de Hasard","du Pere Fouras"]
    text = joueur["nom"]+" a "+reussite+" l'épreuve "+test[choix]+"\n"
    f.write(text)
    f.close()
