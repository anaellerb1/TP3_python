#coding: utf-8
"""
Fonctionsutiles TP3
Auteur : Anaëlle ROBIN
Date : 01/10/2024

TODO:
    -
"""
import random as r
import tkinter as t

def lire_txt(fichiertxt):
    """
    Fonction qui lit un fichier texte et retourne une liste
    Variables :
        fichiertxt : str
    Sortie :
        liste : liste
    """
    with open(fichiertxt, 'r', encoding='utf-8') as fichier:
        liste = [ligne.strip() for ligne in fichier.readlines() if ligne.strip()] # Lire lignes et supprimer les espaces blancs
    return liste

def afficher_mot(solution,lettre_trouvees):
    """
    Fonction qui réecrit l'affichage d'un mot en fonction des lettres trouvés
    Variables :
        affichage : str
        lettre_trouvees : str
        solution : str
    Sortie :
        affichage : str
    """
    affichage = ""
    for index,lettre in enumerate(solution) :
        if lettre in lettre_trouvees:
            affichage += lettre + " "
        elif index == 0:
            affichage += solution[0] + " " 
        else:
            affichage += "_ "
    return affichage

def ask_rejouer():
    """
    Fonction qui demande si le joueur veux rejouer
    Variables :
        rejouer : str
    Sortie :
        True / False
    """
    rejouer = ""
    while rejouer != ('oui' or 'non'):
        rejouer = input("Voulez vous rejouer ? (oui/non): ").lower()
        if rejouer == 'oui':
            return True
        if rejouer == 'non':
            return False
        else :
            print("Veuillez répondre par 'oui' ou 'non'")

def initialiser_partie(Liste_de_mot, label_mot, label_tentatives, entree_lettre, label_info,bouton_proposer):
    global solution, lettres_justes, lettres_trouvees, tentatives, affichage
    solution = Liste_de_mot[r.randint(0,len(Liste_de_mot) - 1)].lower()
    tentatives = 8
    affichage = solution[0] #extrait la premiere lettre
    lettres_justes = ""
    lettres_trouvees = ""
    for lettre in range(len(solution)-1) :
        affichage += " _"
    
    label_mot.config(text=affichage)
    label_tentatives.config(text=f"Tentatives restantes : {tentatives}")
    label_info.config(text=f"Bienvenue dans le jeu du Pendu.")
    bouton_proposer.config(state=t.NORMAL)
    entree_lettre.delete(0, t.END)

def proposer_lettre(label_score, parties, entree_lettre, label_info, score, label_mot, label_tentatives):
    global lettres_justes, lettres_trouvees, tentatives, affichage, solution, bouton_proposer
    lettre_joueur = entree_lettre.get().lower()

    if lettre_joueur in lettres_trouvees:
        label_info.config(text=f"La lettre '{lettre_joueur}' à déjà été donnée. \nListe des lettres déjà essayées : {lettres_trouvees}")
    else :
        lettres_trouvees += lettre_joueur + " "
        if lettre_joueur in solution :
            label_info.config(text=f"-> Bien joué !")
            lettres_justes += lettre_joueur 
            affichage = afficher_mot(solution,lettres_justes)
            label_mot.config(text=affichage)
        else :
            tentatives -= 1
            label_info.config(text=f"-> Raté ! ")
            label_tentatives.config(text=f"Tentative(s) restante : {tentatives}")
            if tentatives == 0:
                label_info.config(text=f">>> Vous avez perdu ! Le mot était '{solution}. <<<")
                bouton_proposer.config(state=t.DISABLED)
                parties += 1
                if tentatives > score:
                    score = tentatives
                label_score.config(text=f"Votre score est de {score} sur {parties} parties.")
                #ask_rejouer()
    if "_" not in affichage :
        label_info.config(text=f">>> Félicitations ! Vous avez deviné le mot : {solution} <<<")
        bouton_proposer.config(state=t.DISABLED)
    
    entree_lettre.delete(0, t.END)
 
