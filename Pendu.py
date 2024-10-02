#coding: utf-8
"""
TP3 : Pendu
Auteur : Anaëlle ROBIN
Date : 01/10/2024

"""

import random as r
import tkinter as t
import Fonctions_utiles as f  # NE PAS METTRE .py SINON NE MARCHE PAS

# Variables globales
play = True
score = 0
parties = 0
Liste_de_mot = f.lire_txt('Mots.txt')

# Interface Tkinter
fenetre = t.Tk()
fenetre.title("Jeu du pendu by Anaëlle")

# Label 
label_mot = t.Label(fenetre, text="", font=("Helvetica", 18))
label_mot.pack(pady=20)

entree_lettre = t.Entry(fenetre)
entree_lettre.pack()

label_tentatives = t.Label(fenetre, text=f"Tentatives restantes : 8", font=("Helvetica", 12))
label_tentatives.pack(pady=10)

label_info = t.Label(fenetre, text="", font=("Helvetica", 12))
label_info.pack(pady=10)

label_score = t.Label(fenetre, text=f"Le score est de {score}", font=("Helvetica", 12))
label_score.pack(pady=10)

# Boutons
bouton_proposer = t.Button(fenetre, text="Proposer", command=lambda: f.proposer_lettre(label_score, parties, entree_lettre, label_info, score, label_mot, label_tentatives))
bouton_proposer.pack(side="left", padx=20)

bouton_exit = t.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_exit.pack(side="right", padx=20)


f.initialiser_partie(Liste_de_mot, label_mot, label_tentatives, entree_lettre, label_info, bouton_proposer)

fenetre.mainloop()
