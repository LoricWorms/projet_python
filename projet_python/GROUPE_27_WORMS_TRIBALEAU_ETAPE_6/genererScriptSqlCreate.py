# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:55:15 2024

@author: loric
"""

import re #fournit des opérations pour travailler avec les expressions régulières
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
    return "db" + generer_compte_mariadb(prenom, nom)

# Fonction pour générer les privilèges SQL
def generer_privileges():
    return "CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT"

# Fonction pour créer le script SQL
def generer_script_sql(nom_fichier_csv, nom_fichier_mdp, nom_fichier_sql):
    with open(nom_fichier_csv, 'r') as csv_file, open(nom_fichier_mdp, 'r') as mdp_file, open(nom_fichier_sql, 'w') as sql_file:
        lignes_csv = csv_file.read().splitlines()[4:]
        lignes_mdp = mdp_file.read().splitlines()[1:]

        # Boucle à travers chaque ligne des fichiers CSV
        for ligne, mdp_ligne in zip(lignes_csv, lignes_mdp):
            colonnes = ligne.split(';')
            nom_complet = colonnes[5].split()
            prenom = nom_complet[1]
            nom = nom_complet[0]
                
            compte_mariadb = generer_compte_mariadb(prenom, nom)
            nom_bdd = generer_nom_bdd(prenom, nom)
            mot_de_passe = mdp_ligne

            # Instructions SQL pour créer l'utilisateur et la base de données
            sql_file.write(f"CREATE USER '{compte_mariadb}'@'localhost' IDENTIFIED BY '{mot_de_passe}';\n")
            sql_file.write(f"CREATE DATABASE {nom_bdd};\n")
            sql_file.write(f"GRANT {generer_privileges()} ON {nom_bdd}.* TO '{compte_mariadb}'@'localhost';\n")
            sql_file.write("\n")

# Appel de la fonction pour générer le script SQL
generer_script_sql("usersToulouse.csv", "usersPassword.csv", "creerUsersBddAcces.sql")





