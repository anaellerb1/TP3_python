#coding: utf-8
"""
TP3 : Pendu
Auteur : Anaëlle ROBIN
Date : 01/10/2024

TODO:

"""

import random as r
import Fonctions_utiles as f #NE PAS METTRE .py SINON NE MARCHE PAS

Liste_de_mot = f.lire_txt('Mots.txt')
solution = Liste_de_mot[r.randint(0,len(Liste_de_mot) -1)].lower()
tentatives = 8
affichage = solution[0] #extrait la premiere lettre
lettre_trouvees = ""
for lettre in range(len(solution)-1) :
    affichage += " _"

print(">>> Bienvenu dans le jeu du PENDU ! <<<")

while tentatives != 0 :
    print(f"Mot à deviner :  {affichage}")
    lettre_joueur = str(input("Veuillez rentrer votre lettre : ")).lower(   )
    if lettre_joueur in solution :
        print("-> Bien joué !")
        lettre_trouvees += lettre_joueur 
        affichage = ""
        for index,lettre in enumerate(solution) :
            if lettre in lettre_trouvees:
                affichage += lettre + " "
            elif index == 0:
                affichage += solution[0] + " " 
            else:
                affichage += "_ "
    else :
        tentatives -= 1
        print(f"-> Raté ! Il vous reste {tentatives} tentatives.")
        if tentatives == 0:
             print(f">>> Vous avez perdu ! Le mot était {solution}. <<<")
    if "_" not in affichage :
        print(f">>> Félicitations ! Vous avez deviné le mot : {solution} <<<")
        break
print("*** FIN DU JEU ***")