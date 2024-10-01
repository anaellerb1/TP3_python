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
