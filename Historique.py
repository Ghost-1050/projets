import sqlite3
from Exos import *

def histo_part(participant):
        connection = sqlite3.connect("entrainements.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM training WHERE user_name = ? ORDER BY id_entrainement DESC LIMIT 3", [participant])
        resultats = cursor.fetchall()
        print(f"Bonjour {participant} voici vos derniers entrainements :")
        for resultat in resultats:
            if resultat[3]==2:
                print(f"\nLe {resultat[2]} vous avez fait {resultat[4]} série(s) de Cardio renforcement musculaire"
                      f" au niveau {resultat[6]} \navec {resultat[5]}s"
                      f" de corde à sauter entre les exercices.")
                print("Récapitulatif des exercies effectués :")
                liste_exos = choix_diff(resultat[6])
                for exos, nbre in liste_exos.items():
                    print(f"{nbre * resultat[4]} {exos}")
            if resultat[3]==1:
                print(f"\nLe {resultat[2]} vous avez fait {resultat[4]} série(s) de Gainage"
                      f" au niveau {resultat[6]}.")
                print("Récapitulatif des exercies effectués :")
                liste_exos2 = choix_diff2(resultat[6])
                for exos, nbre in liste_exos2.items():
                    print(f"{exos} pendant {nbre}s x{resultat[4]} série(s)")

