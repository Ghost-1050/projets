import sqlite3
from Exos import *

def stat_poids(participant):
        connection = sqlite3.connect("entrainements.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM training WHERE user_name = ? ORDER BY id_entrainement ASC LIMIT 1", [participant])
        resultats = cursor.fetchall()
        for resultat in resultats:
                return resultat[7]

def stat_entrainement(participant):
        connection = sqlite3.connect("entrainements.db")
        cursor = connection.cursor()
        cursor.execute("SELECT entrainement, COUNT(*) FROM training WHERE user_name = ? GROUP BY entrainement ", [participant])
        resultats = cursor.fetchall()
        for resultat in resultats:
            if resultat[0]==2:
                 print(f"Vous avez fait {resultat[1]} entrainements de Cardio renforcement musculaire.")
            if resultat[0]==1:
                print(f"Vous avez fait {resultat[1]} entrainements de Gainage.")
            if resultat[0]==3:
                print(f"Vous avez fait {resultat[1]} entrainements de renforcement musculaire.")


