# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 09:02:44 2024

@author: loric
"""


# Ouverture du fichier en lecture et du fichier en écriture
with open('testEntree.csv', 'r') as entree, open('testSortie.csv', 'w') as sortie:
    
    #Lire la première ligne pour l'ignorer
    entree.readline()
    
    # Création du titre de la colonne dans le fichier de sortie
    sortie.write("login\n")

    # Pour chaque ligne du fichier d'entrée
    for ligne in entree:
        # Suppression du caractère de saut de ligne à la fin
        ligne = ligne.strip()

        # Séparation des valeurs de la ligne
        valeurs = ligne.split(';')

        # Extraction du prénom et du nom
        prenom = valeurs[0]
        nom = valeurs[1]

        # Création du login en concatenant la première lettre du prénom et le nom
        login = prenom[0] + nom

        # Conversion en minuscules
        login = login.lower()

        # Écriture du login dans le fichier de sortie suivi d'un saut de ligne
        sortie.write(login + "\n")

entree.close()
sortie.close()
