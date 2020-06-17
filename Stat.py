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
                 print(f"Vous avez fait {resultat[1]} entrainement(s) de Cardio renforcement musculaire.")
            if resultat[0]==1:
                print(f"Vous avez fait {resultat[1]} entrainement(s) de Gainage.")
            if resultat[0]==3:
                print(f"Vous avez fait {resultat[1]} entrainement(s) de Renforcement musculaire.")
            if resultat[0]==4:
                print(f"Vous avez fait {resultat[1]} entrainement(s) du Challenge FBI.")
            if resultat[0]==5:
                print(f"Vous avez fait {resultat[1]} entrainement(s) de Travail Force à la poutre.")

def histo_part(participant):
    connection = sqlite3.connect("entrainements.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM training WHERE user_name = ? ORDER BY id_entrainement DESC LIMIT 3", [participant])
    resultats = cursor.fetchall()
    print(f"\nVoici vos trois derniers entrainements :")
    for resultat in resultats:
        if resultat[3] == 2:
            print(f"\nLe {resultat[2]} vous avez fait {resultat[4]} série(s) de Cardio renforcement musculaire"
                  f" au niveau {resultat[6]} \navec {resultat[5]}s"
                  f" de corde à sauter entre les exercices.")
            print("Récapitulatif des exercies effectués :")
            liste_exos = choix_diff(resultat[6])
            for exos, nbre in liste_exos.items():
                print(f"{nbre * resultat[4]} {exos}")
        if resultat[3] == 1:
            print(f"\nLe {resultat[2]} vous avez fait {resultat[4]} série(s) de Gainage"
                  f" au niveau {resultat[6]}.")
            print("Récapitulatif des exercies effectués :")
            liste_exos2 = choix_diff2(resultat[6])
            for exos, nbre in liste_exos2.items():
                print(f"{exos} pendant {nbre}s x{resultat[4]} série(s)")
        if resultat[3] == 3:
            print(f"\nLe {resultat[2]} vous avez fait {resultat[4]} série(s) de Renforcement musculaire"
                  f" au niveau {resultat[6]}.")
            print("Récapitulatif des exercies effectués :")
            liste_exos3 = choix_diff3(resultat[6])
            for exos, nbre in liste_exos3.items():
                print(f"{nbre * resultat[4]} {exos}")
        if resultat[3] == 4:
            print(f"\nLe {resultat[2]} vous avez fait le Challenge FBI 'AC/DC'")
        if resultat[3] == 5:
            print(f"\nLe {resultat[2]} vous avez fait un entrainement de Travail Force à la poutre")
            print("Récapitulatif des exercies effectués :")
            liste_exos4 = choix_diff4(1)
            for exos, nbre in liste_exos4.items():
                print(f"{nbre * resultat[4]} {exos}")
            liste_exos4 = choix_diff4(2)
            for exos, nbre in liste_exos4.items():
                print(f"{nbre * resultat[4]} {exos}")
            liste_exos4 = choix_diff4(3)
            for exos, nbre in liste_exos4.items():
                print(f"{nbre * resultat[4]} {exos}")




