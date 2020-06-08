from modules import *
from Exos import *
from datetime import date
from Historique import histo_part
from GraphPoids import graph_poids
from Record_sql import record_base

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print(f"Nous sommes le {d1}.")
print("___________              __        __")
print("\__    ___/___________  |__| ____ |__| ____    _____")
print("  |    |  \_  __ \__  \ |  |/    \|  |/    \  / ___ \ ")
print("  |    |   |  | \// __ \|  |   |  \  |   |  \/ /_/  >")
print("  |____|   |__|  /____  /__|___|  /__|___|  /\___  /")
print("                      \/        \/        \//_____/   by Ghost v2.0")
print("\n")

participant = input("Veuillez rentrer votre nom : ")
participant = participant.capitalize()

while 1:
    choix_menu = int(input(f"\n- Faites votre choix {participant} - \n 1- Faire un entrainement\n "
                          "2- Consulter mes derniers entrainement \n"
                          " 3- Consulter ma courbe de poids\n 4- Quitter \n> "))
    if choix_menu == 1:
        poids = float(input("Veuillez rentrer votre poids avec 1 chiffre apres le . : "))
        gras = float(input("Veuillez rentrer votre taux de graisse avec 1 chiffre apres le . : "))
        entrainement = int(input(f"\nQuel type d'entrainement souhaitez vous faire {participant} ?\n 1- Gainage"
                                 "\n 2- Cardio Renforcement musculaire\n> "
                                 ""))
        print(f"\nEchauffez vous bien {participant} l'entrainement va commencer.\n")
        if entrainement == 2:
            print("Matériel : Vous avez besoin d'un tapis de sol, d'une corde à sauter et d'une barre de traction.\n")
            tps_rope = int(input("Choisissez le temps de corde à sauter en seconde : "))
            print("Choisissez l'intensité : \n")
            level = int(input(f"1-Débutant: {choix_diff(1)}\n2-Intermédiaire: {choix_diff(2)}"
                              f"\n3-Confirmé: {choix_diff(3)}\n4-Expert: {choix_diff(4)}\n> "
                              f""))
            serie = int(input("Combien de serie(s) souhaitez-vous faire ? : 1,2,3...? : "))
            train = Training(nbre_serie=serie, tps_rope=tps_rope, level=level, participant=participant)
            train.cardio()
            record_base(participant, d1, entrainement, serie, tps_rope, level, poids, gras)
        if entrainement == 1:
            print("Matériel : Vous avez besoin d'un tapis de sol.\n")
            print("Choisissez le niveau d'intensité : \n")
            level = int(input(f"1-Débutant: {choix_diff2(1)}\n2-Intermédiaire: {choix_diff2(2)}\n>"))
            serie = int(input("Combien de serie(s) souhaitez-vous faire ? : 1,2,3...? : "))
            print(f"\nBienvenue {participant} l'entrainement va commencer.\n")
            tps_rope = 0
            train = Training(nbre_serie=serie, tps_rope=tps_rope, level=level, participant=participant)
            train.gain()
            record_base(participant, d1, entrainement, serie, tps_rope, level, poids, gras)
    if choix_menu ==2:
        histo_part(participant)
    if choix_menu ==3:
        graph_poids(participant)
    if choix_menu ==4:
        print(f"Merci pour votre visite {participant} à bientôt.")
        break




