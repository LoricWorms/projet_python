# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:14:26 2024

@author: loric
"""

import re
from os import chdir

chdir('..\GROUPE_27_WORMS_TRIBALEAU_ETAPE_5')

# Fonction pour nettoyer les caractères spéciaux des noms
def nettoyer_nom(nom):
    return re.sub(r'\W', '', nom)

# Fonction pour générer le compte MariaDB
def generer_compte_mariadb(prenom, nom):
    return nettoyer_nom(prenom[0] + nom).lower()

# Fonction pour générer le nom de la base de données
def generer_nom_bdd(prenom, nom):
    return "db" + nettoyer_nom(prenom[0] + nom).lower()

# Fonction pour créer le script SQL de suppression
def generer_script_sql_drop(nom_fichier_csv, nom_fichier_sql):
    with open(nom_fichier_csv, 'r') as csv_file, open(nom_fichier_sql, 'w') as sql_file:
        lignes_csv = csv_file.read().splitlines()[4:]  # Ignorer les 4 premières lignes

        # Boucle à travers chaque ligne des fichiers CSV
        for ligne in lignes_csv:
            colonnes = ligne.split(';')

            nom_complet = colonnes[5].split()  
            prenom = nom_complet[1]
            nom = nom_complet[0] if len(nom_complet) > 1 else ""
                
            compte_mariadb = generer_compte_mariadb(prenom, nom)
            nom_bdd = generer_nom_bdd(prenom, nom)

            # Instructions SQL pour supprimer l'utilisateur et la base de données
            sql_file.write(f"DROP USER '{compte_mariadb}'@'localhost';\n")
            sql_file.write(f"DROP DATABASE {nom_bdd};\n")
            sql_file.write("\n")

# Appel de la fonction pour générer le script SQL de suppression
generer_script_sql_drop("usersToulouse.csv", "supprimerUsersBddAcces.sql")

