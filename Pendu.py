#coding: utf-8
"""
TP3 : Pendu
Auteur : Anaëlle ROBIN
Date : 01/10/2024

TODO:

"""
import random as r
import Fonctions_utiles as f #NE PAS METTRE .py SINON NE MARCHE PAS

play = True
score = 0
parties = 0
print(">>> Bienvenu dans le jeu du PENDU ! <<<")

while play == True :
    """Initialisations des variables"""
    Liste_de_mot = f.lire_txt('Mots.txt')
    solution = Liste_de_mot[r.randint(0,len(Liste_de_mot) -1)].lower()
    tentatives = 8
    affichage = solution[0] #extrait la premiere lettre
    lettres_justes = ""
    lettres_trouvees = ""
    for lettre in range(len(solution)-1) :
        affichage += " _"
   
    """Déroulement du jeu"""
    while tentatives != 0 :
        print(f"Mot à deviner :  {affichage}")
        lettre_joueur = str(input("Veuillez rentrer votre lettre : ")).lower()
        if lettre_joueur in lettres_trouvees:
            print(f"La lettre '{lettre_joueur}' à déjà été donnée. \nListe des lettres déjà essayées : {lettres_trouvees}")
        else :
            lettres_trouvees += lettre_joueur + " "
            if lettre_joueur in solution :
                print("-> Bien joué !")
                lettres_justes += lettre_joueur 
                affichage = f.afficher_mot(solution,lettres_justes)
            else :
                tentatives -= 1
                print(f"-> Raté ! Il vous reste {tentatives} tentatives.")
                if tentatives == 0:
                    print(f">>> Vous avez perdu ! Le mot était '{solution}. <<<")
        if "_" not in affichage :
            print(f">>> Félicitations ! Vous avez deviné le mot : {solution} <<<")
            break
    if tentatives > score:
        score = tentatives
    parties +=1
    print(f"Votre score : {score}")
    play = f.ask_rejouer()

print(f"Votre meilleur score est de {score} pour {parties} parties. ") 
print("*** FIN DU JEU ***")
