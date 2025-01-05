Le projet est un simulateur inspiré du célèbre jeu télévisé Fort Boyard.

Ce projet a été réalisé par Olivia Baudet et Sara Antoszczyk. Olivia avait le rôle de chef, de répartir les tâches. Le rôle de Sara était de motiver et de faire en sorte que tout se passe bien.

Le projet contient donc plusieurs épreuves qui s'apparentent aux épreuves de Fort Boyart. Les épreuves sont classées par thème (logique, mathématique, hasard...). Une équipe de joueurs doit réussir plusieurs épreuves afin d'avoir trois clés pour ensuite participer à l'épreuve finale et tenter de débloquer la salle du trésor.

L'application PyCharm est un IDE fluide et simplifie la programmation. L'application permet de développer l'application python. Elle suggère des mots-clés qui permettent aux développeurs de gagner du temps et d'éviter les erreurs. Elle utilise également des couleurs pour faciliter la compréhension du code.

Le langage de programmation qui a été utilisé est Python. Les bibliothèques random et json ont été utilisées dans plusieurs épreuves.

Pour cloner le dépôt Git, il faut :
* Se connecter au compte GitHub.
* Créez un nouveau dépôt en cliquant sur le bouton "New Repository".
* Renseigner un nom pour le repository.
* Cliquer sur Create repository pour finaliser cette étape.
* Copier l'URL du dépôt distant pour cloner le dépôt.

Etapes pour configurer IDE:
* Faire une demande de licence gratuite auprès de JetBrains (ici de type éducation).
* Création d'un compte JetBrains en renseignant des informations.
* Après validation du compte, accéder aux produits JetBrains.

Instructions pour exécuter Pycharm:
* Se rendre sur le site JetBrains pour télécharger PyCharm.
* Exécuter le programme d'installation en acceptant les droits d'administration.
* Une fenêtre d'options apparait et cocher les 3 options puis installer PyCharm.

Algorithme du jeu:
* pour les épreuves de mathématiques, on a fait l'épreuve sur un papier comme si c'était un exercice puis on l'a codé.
* pour l'épreuve d'hasard par exemple, il y avait des pseudo-codes donc ça nous a aidé et on a codé directement.
* pour les épreuves de logiques, on y a joué sur papier et on a ensuite codé.
Les exemples pour les épreuves nous ont aussi aidé pour bien comprendre ce qui était demandé.

Liste des prototypes de fonctions:

* Pour les épreuves mathématiques: les différentes fonctions de ce fichier sont les suivantes: 
  - pour l'épreuve des factorielles: 
    -> factorielle(n): calcule la factorielle du nombre n
    -> epreuve_math_factorielle(): Choisi un nombre n aléatoire entre 1 et 10 puis vérifie si la réponse de l'utilisateur est correcte
  - pour l'épreuve de l'équation linéaire: 
    -> resoudre_equation_lineaire(): Génère deux nombres aléatoire et calcule le resultat de l'équation ax + b = 0
    -> epreuve_math_equation(): Vérifie que la réponse de l'utilisateur est correcte
  - pour l'épreuve des nombres premiers: 
    -> est_premier(n): Vérifie si le nombre n est premier
    -> premier_plus_proche(n): Cherche le nombre premier le plus proche de n (supérieur ou égal)
    -> epreuve_math_premier(): Génère un nombre n aléatoire et vérifie la réponse de l'utilisateur
  - pour l'épreuve de la roulette mathématique: 
    -> epreuve_roulette_mathematique(): Génère 5 nombres aléatoire et décide du calcul à appliquer. La fonction vérifie ensuite la réponse de l'utilisateur.
  - epreuve_math(): choisi aléatoirement une épreuve de mathématiques

* Pour les épreuves de logiques: les différentes fonctions de ce fichier sont les suivantes: 
  - pour le jeu des bâtonnets:
    -> affiche_batonnets(n): permet d'afficher le nombre de batônnets restants
    -> joueur_retrait(n): permet au joueur de retirer jusqu'à 3 bâtonnets à l'aide d'une saisie sécurisée
    -> maitre_retrait(n): permet au maître du jeu de retirer les bâtonnets de manière intéligente afin d'augmenter ses chances de victoire
    -> jeu_nim(): Permet de lancer le jeu en alternant entre le tour du maitre ou du joueur jusqu'à ce que l'un des deux gagne
  - pour le jeu du morpion:
    -> affiche_grille(grille): affiche la grille du jeu
    -> verifier_victoire(grille, symbole): permet de vérifier si l'un des joueurs a gagné
    -> coup_maitre(grille, symbole): choisi une position à jouer pour le maître du jeu pour soit gagner ou bloquer l'adversaire 
        ou joue aléatoirement si aucune des situation n'est présente.
    -> tour_joueur(grille): permet de simuler le tour du joueur en lui demandans la position où il souhaite jouer à l'aide d'une saisie sécurisée
    -> tour_maitre(grille): simule le tour du maître à l'aide de l'appel à la fonction coup_maitre(grille, symbole)
    -> grille_complete(grille): vérifie si la grille de jeu est complète ou non
    -> verifier_resultat(grille): vérifie si le joueur ou le maître gagne la partie ou si la grille est complete
    -> jeu_tictactoe(): permet de simuler le jeu du morpion à l'aide des fonctions implémentées citées ci-dessus
  - pour le jeu de la bataille navale:
    -> suiv(joueur): permet de passer au joueur suivant
    -> grille_vide(): permet d'initialiser une grille vide pour la bataille navale
    -> affiche_grille_bateau(grille, message): permet d'afficher la grille du jeu dans la console
    -> demande_position(): permet de demander au joueur une position (pour placer un bateau ou pour tirer)
    -> init(): permet au joueur d'initialiser la position de ces deux bateaux
    -> tour(joueur,grille_tirs_joueur,grille_adversaire): permet de demander à l'utilisateur une position où tirer 
        ou de générer un position aléatoire pour le maître du jeu puis indique si c'est touché ou dans l'eau.
    -> gagne(grille_tirs_joueur): vérifie la victoire du joueur ou du maître en vérifiant si il a coulé les deux bateaux adverses
    -> jeu_bataille_navale(): Simule le jeu de la bataille navale en alternant le tour du joueur et du maître du jeu grace aux fonctions implémentées
  - epreuve_logique(): choisi aléatoirement une épreuve de logique
  
* Pour les épreuves de hasard:
  - épreuve du bonneteau
    -> bonneteau(): simule le jeu du bonneteau en choisissant aléatoirement entre le bonneteau A, B ou C puis vérifie si la réponse du joueur est identique. 
        L'épreuve se répète une seconde fois si le joueur n'as pas trouvé.
  - épreuve du lancé de dés
    -> jeu_lance_des(): simule des lancés de dés deux dés sont lancés à tour de role entre le joueur et le maitre. 
        Le premier a obtenir un six en trois essais maximums gagne, si personne n'obtient un six au bout de trois essais il y a égalité.

* Pour l'énigme du père Fouras:
  - charger_enigmes(fichier): permet d'extraire les enigmes et leur solution du fichier.
  - enigme_pere_fouras(): demande au joueur la réponse à l'énigme après l'avoir écrit dans la console puis compare ensuite la réponse du joueur à la solution.

* Pour l'épreuve finale:
  - salle_de_tresor(): extrait l'énigme d'un fichier puis donne trois mots au joueurs et lui demande de trouver le mot correspondant.
      Le joueur a trois essais et après chaque essais raté un mot supplémentaire est donné pour l'aider à trouver.

Entrées et erreurs:

Les valeurs en Python sont des nombres, des caractères, un booléen, un mot, une phrase. Pour les intervalles, on utilise souvent la fonction range() qui va créer des intervalles de nombres.
Sur PyCharm, il y a un code intelligent donc souvent les intervalles ou les valeurs sont déjà pré-rempli ce qui peut créer des erreurs. Par exemple, on veut des nombres aléatoires entre 1 et 20 et la machine nous propose entre 1 et 10. 
De plus, des saisies intéligentes permettent de limiter les bugs redemandant ainsi à l'utilisateur une nouvelle saisie jusqu'à ce qu'elle soit correcte.

Liste de bugs connus:

* Syntaxe (exemple: oublier les deux points à la fin de la définition d'une fonction ou encore oublier des parenthèses).
* Identation.
* Indices (exemple: accéder à un élèment qui n'est pas dans la liste).
* Nous avons créer un historique comme fonction bonus mais nous l'avons commenté car il faut créer un fichier supplémentaire et cela fait buguer le programme s'il n'est pas déjà présent donc nous avons préféré la bonne fonctionnalité du programme même si nous avons codé la fonction historique qui etait en bonus

Chronologie du projet :

On travaillait le projet quand on avait le temps mais les dates pour déposer le projet étaient assez rapprochées. On a donc rencontrer un problème de temps et d'organisation mais dans l'ensemble ça était.

Repartition des tâches :

Chacune a pris l'épreuve qui lui paraissait la plus simple et on mettait en commun. Olivia a d'abord travaillé sur les épreuves de logique et l'enigme du père Fouras. Sara a fait les épreuves de mathématiques et de hasard.
Celle qui avait le plus de facilités aidait l'autre.

Stratégie de test:

Cas de test spécifiques et résultats:

Pour vérifier le bon fonctionnement des fonctions créées il est important de les tester chacunes plusieurs fois en essayant de faire buguer la machine par une saisie incorrecte afin de savoir où améliorer le code afin qu'il soit le plus optimal et fonctionnel possible.

Captures d'écran montrant les tests en action:

Nous ne pouvons pas intégrer de capture d'écran ici mais tout le code fonctionne quand nous l'avons testé.


