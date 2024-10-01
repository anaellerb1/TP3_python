#coding: utf-8
"""
Fonctionsutiles TP3
Auteur : Anaëlle ROBIN
Date : 01/10/2024

TODO:
    -
"""

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
    
        
